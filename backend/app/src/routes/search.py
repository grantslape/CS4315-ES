"""Endpoints for searching documents on a given index"""
from flask import Blueprint, request
from helpers import generic_search, hydrate_models
from commons import build_response, get_logger

search = Blueprint('search', __name__)

logger = get_logger(__name__)


@search.route('', methods=['GET'])
def get():
    query = request.args.get('q')
    offset = int(request.args.get('offset', default=0))
    page_size = int(request.args.get('page_size', default=10))
    results = generic_search(query, offset=offset, page_size=page_size)
    return build_response(hydrate_models(results.hits))
