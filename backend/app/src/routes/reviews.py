"""Endpoints for indexing and retrieving documents"""
from flask import Blueprint, request
import requests

from commons import error_response, json_response
from settings import ES_HOST

reviews = Blueprint('reviews', __name__)
INDEX_URI = '{0}/reviews/_doc/{1}?pretty'


@reviews.route('', methods=["POST"])
def create_document():
    """Add a document"""
    if 'id' not in request.args:
        return error_response(400, 'id is required: {}'.format(request.get_json()))

    # Lol actually send the data dumbass
    response = requests.put(INDEX_URI.format(ES_HOST, request.args['id']))
    return json_response(response.text, response.status_code)
