import requests
import json
import os
import ast
import time
import arrow
from threading import Thread
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


def parse_sub_obj(obj: dict, type: str) -> dict:
    """Parse subdicts of the given dict and return new dict"""
    if type == 'businesses':
        return parse_business(obj)
    if type == 'users':
        return parse_user(obj)
    return obj


def parse_user(obj: dict) -> dict:
    """Parse out user specific stuff"""
    # user.friends, user.elite
    obj['friends'] = obj['friends'].split(', ')
    obj['elite'] = obj['elite'].split(', ')


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
    # Possible DayOpen, DayClose ?
    payload = {}
    for k, v in obj.items():
        time_str = v.split('-')
        payload['{}_open'.format(k)] = arrow.get(time_str[0], 'H:m').datetime
        close = arrow.get(time_str[1], 'H:m')
        if close.hour < 6:
            # Next day for close time
            close = close.shift(days=+1)
        payload['{}_close'.format(k)] = close.datetime

    return payload


def parse_business(obj: dict) -> dict:
    """Parse subdicts for business and cast attributes as needed"""
    if obj['categories'] is not None:
        obj['categories'] = obj['categories'].split(', ')
    obj['is_open'] = bool(obj['is_open'])
    obj['location'] = '{},{}'.format(obj.pop('latitude'), obj.pop('longitude'))

    # Parse sub-objects from strings to dicts
    attributes = obj['attributes']
    attributes = parse_dict(attributes, 'GoodForMeal')
    attributes = parse_dict(attributes, 'Ambience')
    attributes = parse_dict(attributes, 'BusinessParking')

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
                    # This dataset has None for false sometimes
                    attributes[k] = False

        obj['attributes'] = attributes

    hours = obj['hours']
    if hours is not None:
        obj['hours'] = parse_hours(hours)

    return obj


def file_iterable(path: str, name: str) -> dict:
    """File iterable to index reviews"""
    with open(path, 'r') as file:
        counter = 1
        for line in file:
            doc = parse_sub_obj(json.loads(line), name)
            payload = {
                "_id": counter,
                "_index": name,
                "_type": "doc",
                "doc": doc
            }
            counter += 1
            yield payload


def index_documents(path: str, name: str):
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


def ext_index_reviews():
    """Index reviews externally by hitting the flask API"""
    with open('review.json', 'r') as file:
        counter = 1
        url = 'http://localhost:45000/reviews/{}'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        for line in file:
            review = json.loads(line)
            resp = requests.put(url.format(counter), headers=headers, data=json.dumps(review))
            if resp.status_code > 201:
                print('failure: {}'.format(resp.json()))

            counter += 1


if __name__ == '__main__':
    Thread(target=index_documents, args=('review.json', 'reviews',)).start()
    Thread(target=index_documents, args=('user.json', 'users',)).start()
    Thread(target=index_documents, args=('tip.json', 'tips',)).start()
    Thread(target=index_documents, args=('checkin.json', 'checkins',)).start()
    Thread(target=index_documents, args=('business.json', 'businesses',)).start()
