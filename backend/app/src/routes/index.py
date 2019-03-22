from flask import Blueprint, request, jsonify
import requests

from settings import ES_HOST

index = Blueprint('index', __name__)


@index.route('', methods=["POST"])
def create_index():
    response = requests.put('{0}/{1}'.format(ES_HOST, 'reviews'))
    return response
