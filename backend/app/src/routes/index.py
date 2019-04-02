"""Endpoints for routes to update the cluster or index itself"""
from flask import Blueprint
import requests

from commons import GenericException
from commons.misc import set_up
from models import User, Review, Tip, Checkin, Business
from settings import ES_HOST, ES_PORT
from commons.responses import json_response, build_response

index = Blueprint('index', __name__)
INDEX_URI = '{0}:{1}/{2}?pretty'


@index.route('', methods=["POST"])
def create_index(name: str):
    """Create an index for reviews"""
    if name == 'reviews':
        set_up(name, Review, create=True)
    elif name == 'users':
        set_up(name, User, create=True)
    elif name == 'tips':
        set_up(name, Tip, create=True)
    elif name == 'checkins':
        set_up(name, Checkin, create=True)
    elif name == 'businesses':
        set_up(name, Business, create=True)
    else:
        raise GenericException(message='Not implemented', status_code=404)

    return build_response({'acknowledged': True})


@index.route('', methods=["DELETE"])
def delete_index(name: str):
    """Delete the index"""
    # TODO: Use Helper Library here
    resp = requests.delete(INDEX_URI.format(ES_HOST, ES_PORT, name))
    return json_response(resp.text, resp.status_code)
