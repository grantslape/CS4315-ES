"""Endpoints for searching documents on a given index"""
from flask import Blueprint, request
from helpers import generic_search, hydrate_models
from commons import build_response, get_logger

search = Blueprint('search', __name__)

logger = get_logger(__name__)


@search.route('', methods=["GET"])
def get():
    query = request.args.get('q')
    offset = int(request.args.get('offset'))
    results = generic_search(query, offset=offset)
    return build_response(hydrate_models(results.hits))
