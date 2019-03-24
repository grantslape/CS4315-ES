"""Endpoints for indexing and retrieving documents"""
from flask import Blueprint, request, json
import requests

from commons import error_response, json_response
from settings import ES_HOST

reviews = Blueprint('reviews', __name__)

INDEX_URI = '{0}/reviews/_doc/{1}?pretty'
HEADERS = {'Content-Type': 'application/json'}


@reviews.route('/<int:doc_id>', methods=["GET"])
def get(doc_id: int):
    """Get a document by ID"""
    resp = requests.get(INDEX_URI.format(ES_HOST, doc_id))
    return json_response(resp.text, resp.status_code)


@reviews.route('', methods=["POST"])
def create_document():
    """Add a document"""
    data = request.get_json()
    try:
        doc_id = data['id']
    except KeyError:
        return error_response(400, 'id is required: {}'.format(data))

    resp = requests.put(INDEX_URI.format(ES_HOST, doc_id), data=json.dumps(data), headers=HEADERS)
    return json_response(resp.text, resp.status_code)
