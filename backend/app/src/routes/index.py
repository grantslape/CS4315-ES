from flask import Blueprint, request, jsonify
import requests

from settings import ES_HOST

index = Blueprint('index', __name__)


@index.route('', methods=["POST"])
def create_index():
    # TODO now that this works, make it better
    response = requests.put('http://{0}:9200/{1}?pretty'.format(ES_HOST, 'reviews'))
    return str(response)
