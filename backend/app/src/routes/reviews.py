"""Endpoints for indexing and retrieving documents"""
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


@reviews.route('', methods=["POST"])
def create_document():
    """Add a document"""
    data = request.get_json()
    try:
        doc_id = data['id']
    except KeyError:
        raise GenericException('id is required', status_code=400, payload=data)

    resp = requests.put(
        INDEX_URI.format(ES_HOST, doc_id),
        data=json.dumps(data),
        headers=HEADERS
    )
    return json_response(resp.text, resp.status_code)
