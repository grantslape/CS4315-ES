import requests
import json
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


def file_iterable(path: str, name: str) -> dict:
    """File iterable to index reviews"""
    with open(path, 'r') as file:
        counter = 1
        for line in file:
            # TODO need to break apart comma separated strings into arrays.
            # user.friends, user.elite, business.categories
            # business need to figure out what to do with attribute subobjects
            # business need to parse hours into usable hours
            payload = {
                "_id": counter,
                "_index": name,
                "_type": "doc",
                "doc": json.loads(line)
            }
            counter += 1
            yield payload


def index_documents(path: str, name: str):
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 49200}])
    print(es)
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
    index_documents('review.json', 'reviews')
    index_documents('user.json', 'users')
    index_documents('tip.json', 'tips')
    index_documents('checkin.json', 'checkins')
