"""
Endpoints for indexing and retrieving review documents
This is almost a POC for generic flask endpoints, a better solution would use
the ES helper library
"""
from elasticsearch import NotFoundError
from flask import Blueprint, request, json
import requests

from commons.GenericException import GenericException
from commons.responses import json_response, build_response, error_response
from models.review import Review
from settings import ES_HOST, ES_PORT

reviews = Blueprint('reviews', __name__)

INDEX_URI = '{0}:{1}/reviews/doc/{2}?pretty'
HEADERS = {'Content-Type': 'application/json'}


@reviews.route('/<int:doc_id>', methods=["GET"])
def get(doc_id: int):
    """Get a document by ID"""
    try:
        resp = Review.get(id=doc_id, index='reviews')
    except NotFoundError as e:
        raise GenericException(
            message=e.error,
            status_code=e.status_code,
            payload={'id': doc_id}
        )
    return build_response(resp.to_dict())


@reviews.route('/<int:doc_id>', methods=["PUT"])
def create_document(doc_id: int):
    """Add a document"""
    data = request.get_json()

    doc = Review(**data)
    doc.meta.id = doc_id
    doc.save()

    return build_response(doc.to_dict())
