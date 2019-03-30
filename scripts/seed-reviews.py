import requests
import json
import os
from pathlib import Path
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


def file_iterable(path, name):
    """File iterable to index reviews"""
    with open(path, 'r') as file:
        counter = 1
        for line in file:
            payload = {
                "_id": counter,
                "_index": name,
                "_type": "doc",
                "doc": json.loads(line)
            }
            counter += 1
            yield payload


def index_reviews():
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 49200}])
    print(es)
    for ok, result in streaming_bulk(
            es,
            file_iterable('review.json', 'reviews')
    ):
        action, result = result.popitem()
        doc_id = '/%s/doc/%s' % ('reviews', result['_id'])
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
    index_reviews()
