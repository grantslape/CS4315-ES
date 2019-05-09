"""Endpoints for searching documents on a given index"""
from flask import Blueprint, request
from elasticsearch import TransportError
from models import BusinessElastic
from helpers import generic_search, hydrate_models, business_reviews
from commons import build_response, get_logger, GenericException

search = Blueprint('search', __name__)

logger = get_logger(__name__)


@search.route('', methods=['GET'])
def get():
    query = request.args.get('q')
    offset = int(request.args.get('offset', default=0))
    page_size = int(request.args.get('page_size', default=10))
    results = generic_search(query, offset=offset, page_size=page_size)
    return build_response(hydrate_models(results.hits))


@search.route('/businesses/<int:doc_id>/reviews', methods=['GET'])
def get_business_reviews(doc_id: int):
    try:
        doc = BusinessElastic.get(id=doc_id, index='businesses')
    except TransportError as e:
        raise GenericException(
            message='error getting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    results = business_reviews(business_id=doc.business_id)
    return build_response(hydrate_models(results.hits))
