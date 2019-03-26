"""
Endpoints for indexing and retrieving review documents
This is almost a POC for generic flask endpoints, a better solution would use
the ES helper library
"""
from flask import Blueprint, request, json
import requests

from commons.GenericException import GenericException
from commons.responses import json_response, build_response
from settings import ES_HOST

reviews = Blueprint('reviews', __name__)

INDEX_URI = '{0}/reviews/_doc/{1}?pretty'
HEADERS = {'Content-Type': 'application/json'}


@reviews.route('/<int:doc_id>', methods=["GET"])
def get(doc_id: int):
    """Get a document by ID"""
    resp = requests.get(INDEX_URI.format(ES_HOST, doc_id))

    if resp.status_code == 200:
        return build_response(resp.json()['_source']), 200
    elif resp.status_code == 404:
        message = 'document not found'
    else:
        message = 'something went horribly wrong'

    raise GenericException(
        message=message,
        status_code=resp.status_code,
        payload={'id': doc_id}
    )


@reviews.route('/<int:doc_id>', methods=["PUT"])
def create_document(doc_id: int):
    """Add a document"""
    data = request.get_json()
    resp = requests.put(
        INDEX_URI.format(ES_HOST, doc_id),
        data=json.dumps(data),
        headers=HEADERS
    )

    if resp.status_code >= 300:
        return json_response(resp.text, resp.status_code)

    data = resp.json()
    return build_response({'message': data['result'], 'id': data['_id']}), resp.status_code
