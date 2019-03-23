"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from settings import ES_HOST
from commons import json_response

index = Blueprint('index', __name__)
INDEX_URI = '{0}/reviews?pretty'


@index.route('', methods=["POST"])
def create_index():
    """Create an index for reviews"""
    response = requests.put(INDEX_URI.format(ES_HOST))
    return json_response(response.text, response.status_code)


@index.route('', methods=["DELETE"])
def delete_index():
    """Delete the index"""
    response = requests.delete(INDEX_URI.format(ES_HOST))

    return json_response(response.text, response.status_code)
