"""Endpoints for searching documents on a given index"""
from flask import Blueprint, request

from commons import error_response

search = Blueprint('search', __name__)


@search.route('', methods=["GET"])
def get():
    query = request.args.get('q')
    return error_response(404, 'not implemented')
