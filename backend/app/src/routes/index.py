"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from settings import ES_HOST
from commons import json_response, build_response

index = Blueprint('index', __name__)


@index.route('', methods=["POST"])
def create_index():
    """Create an index for reviews"""
    response = requests.put('http://{0}:9200/{1}?pretty'.format(ES_HOST, 'reviews'))
    # Getting a success response, but not returning properly.
    return response.raw.read, response.status_code, response.headers.items()
