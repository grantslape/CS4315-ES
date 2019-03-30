"""
Endpoints for indexing and retrieving review documents
This is almost a POC for generic flask endpoints, a better solution would use
the ES helper library
"""
from elasticsearch import TransportError
from flask import Blueprint, request

from commons.GenericException import GenericException
from commons.responses import build_response
from models.review import Review

reviews = Blueprint('reviews', __name__)


@reviews.route('/<int:doc_id>', methods=["GET"])
def get(doc_id: int):
    """Get a document by ID"""
    try:
        resp = Review.get(id=doc_id, index='reviews')
    except TransportError as e:
        raise GenericException(
            message='error getting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    return build_response(resp.to_dict())


@reviews.route('/<int:doc_id>', methods=["PUT"])
def create_document(doc_id: int):
    """Add a document"""
    data = request.get_json()
    doc = Review(**data)
    doc.meta.id = doc_id

    try:
        doc.save()
    except ValueError as e:
        raise GenericException(
            message=str(e),
            status_code=400,
            payload=request.get_json()
        )

    return build_response(doc.to_dict())
