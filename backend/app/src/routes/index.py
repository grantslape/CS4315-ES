"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from models.review import Review
from settings import ES_HOST, ES_PORT
from commons.responses import json_response, build_response

index = Blueprint('index', __name__)
INDEX_URI = '{0}:{1}/{2}?pretty'


@index.route('', methods=["POST"])
def create_index(name: str):
    """Create an index for reviews"""
    if name == 'reviews':
        return build_response({'message': Review.set_up(create=True)})


@index.route('', methods=["DELETE"])
def delete_index(name: str):
    """Delete the index"""
    resp = requests.delete(INDEX_URI.format(ES_HOST, ES_PORT, name))
    return json_response(resp.text, resp.status_code)
