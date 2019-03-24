"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from settings import ES_HOST
from commons.responses import json_response

index = Blueprint('index', __name__)
INDEX_URI = '{0}/{1}?pretty'


@index.route('', methods=["POST"])
def create_index(name: str):
    """Create an index for reviews"""
    resp = requests.put(INDEX_URI.format(ES_HOST, name))
    return json_response(resp.text, resp.status_code)


@index.route('', methods=["DELETE"])
def delete_index(name: str):
    """Delete the index"""
    resp = requests.delete(INDEX_URI.format(ES_HOST, name))
    return json_response(resp.text, resp.status_code)
