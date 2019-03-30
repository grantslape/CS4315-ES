"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from commons import GenericException
from models import User, Review, Tip, Checkin
from settings import ES_HOST, ES_PORT
from commons.responses import json_response, build_response

index = Blueprint('index', __name__)
INDEX_URI = '{0}:{1}/{2}?pretty'


@index.route('', methods=["POST"])
def create_index(name: str):
    """Create an index for reviews"""
    if name == 'reviews':
        return build_response({'message': Review.set_up(create=True)})
    elif name == 'users':
        return build_response({'message': User.set_up(create=True)})
    elif name == 'tips':
        return build_response({'message': Tip.set_up(create=True)})
    elif name == 'checkins':
        return build_response({'message': Checkin.set_up(create=True)})
    else:
        raise GenericException(message='Not implemented', status_code=404)


@index.route('', methods=["DELETE"])
def delete_index(name: str):
    """Delete the index"""
    # TODO: Use Helper Library here
    resp = requests.delete(INDEX_URI.format(ES_HOST, ES_PORT, name))
    return json_response(resp.text, resp.status_code)
