import json
import ast
import arrow
from arrow import Arrow
from threading import Thread
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


def parse_sub_obj(obj: dict, doc_type: str) -> dict:
    """Parse subdicts of the given dict and return new dict"""
    if doc_type == 'businesses':
        return parse_business(obj)
    if doc_type == 'users':
        return parse_user(obj)
    if doc_type == 'checkins':
        return parse_checkins(obj)
    if doc_type == 'reviews':
        return parse_reviews(obj)
    if doc_type == 'tips':
        # Only date for now
        return parse_reviews(obj)
    return obj


def parse_user(obj: dict) -> dict:
    """Parse out user specific stuff"""
    obj['friends'] = obj['friends'].split(', ')
    obj['elite'] = obj['elite'].split(',')

    if len(obj['elite']) == 0 or obj['elite'][0] == '':
        obj.pop('elite')

    obj['yelping_since'] = parse_date(obj['yelping_since'])
    return obj


def parse_reviews(obj: dict) -> dict:
    """Parse out review specific stuff"""
    obj['date'] = parse_date(obj['date'])
    return obj


def parse_date(date: str) -> Arrow:
    return arrow.get(date, 'YYYY-MM-DD HH:mm:ss').format('YYYY-MM-DDTHH:mm:ss')


def parse_checkins(obj: dict) -> dict:
    """Parse out checkin specific dates"""
    raw_dates = obj['date'].split(', ')
    obj['date'] = []
    for d in raw_dates:
        obj['date'].append(parse_date(d))
    return obj


def parse_dict(obj: dict, key: str) -> dict:
    """Attempt to parse sub dicts that may not exist"""
    if obj is not None:
        try:
            entry = obj[key]
            obj[key] = ast.literal_eval(entry)
        except KeyError:
            pass
    return obj


def parse_hours(obj: dict) -> dict:
    """Parse a dict of business hours represented as OPEN-CLOSE into times"""
    payload = {}
    for k, v in obj.items():
        open_period = payload['open_period_{}'.format(k.lower())] = {}
        time_str = v.split('-')
        open_period['gte'] = arrow.get(time_str[0], 'H:m').datetime
        close_time = arrow.get(time_str[1], 'H:m')
        if close_time.hour < 6:
            # Next day for close time
            close_time = close_time.shift(days=+1)
        open_period['lte'] = close_time.datetime

    return payload


def parse_business(obj: dict) -> dict:
    """Parse subdicts for business and cast attributes as needed"""
    if obj['categories'] is not None:
        obj['categories'] = obj['categories'].split(', ')
    obj['is_open'] = bool(obj['is_open'])
    obj['location'] = '{},{}'.format(obj.pop('latitude'), obj.pop('longitude'))

    # Parse sub-objects from strings to dicts
    # TODO: refactor this into some methods
    attributes = obj['attributes']
    # attributes = parse_dict(attributes, 'GoodForMeal')
    # attributes = parse_dict(attributes, 'Ambience')
    # attributes = parse_dict(attributes, 'BusinessParking')

    # There are a lot of nullable bools saved as strings in this dataset
    if attributes is not None:
        attributes = {k: v for k, v in attributes.items() if v is not None}
        for k, v in attributes.items():
            if type(v) == str:
                if v[-1] == "'":
                    if v[0] == 'u':
                        # Extract unicode string
                        attributes[k] = v[2:-1]
                    else:
                        # other double string
                        attributes[k] = v[1:-1]

                lower = v.lower()
                if lower == 'true' or lower == 'false':
                    attributes[k] = bool(lower)
                elif lower == 'none':
                    # This dataset has None for false sometimes which ES can't handle
                    attributes[k] = False

        obj = {**obj, **attributes}
        obj.pop('attributes')

    hours = obj['hours']
    if type(hours) == dict:
        obj = {**obj, **parse_hours(hours)}
        obj.pop('hours')

    return obj


def file_iterable(path: str, name: str) -> dict:
    """File iterable to return pre-processed, indexable docs"""
    with open(path, 'r') as file:
        counter = 1
        for line in file:
            doc = parse_sub_obj(json.loads(line), name)
            meta = {
                "_id": counter,
                "_index": name,
                "_type": "doc"
            }
            payload = {**meta, **doc}
            counter += 1
            yield payload


def index_documents(path: str, name: str):
    """Use the streaming bulk API to index some documents"""
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 49200}])
    for ok, result in streaming_bulk(
            es,
            file_iterable(path, name)
    ):
        action, result = result.popitem()
        doc_id = '/%s/doc/%s' % (name, result['_id'])
        # process the information from ES whether the document has been
        # successfully indexed
        if not ok:
            print('Failed to %s document %s: %r' % (action, doc_id, result))
        else:
            print(doc_id)


if __name__ == '__main__':
    Thread(target=index_documents, args=('review.json', 'reviews',)).start()
    Thread(target=index_documents, args=('business.json', 'businesses',)).start()
    Thread(target=index_documents, args=('user.json', 'users',)).start()
    Thread(target=index_documents, args=('tip.json', 'tips',)).start()
    Thread(target=index_documents, args=('checkin.json', 'checkins',)).start()
