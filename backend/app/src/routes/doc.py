"""Endpounts for indexing and retrieving business documents"""
from elasticsearch import TransportError
from flask import Blueprint, request

from commons import GenericException, build_response
from models import Business, Tip, User, Checkin, Review

document = Blueprint('document', __name__)


@document.route('', methods=["GET"])
def get(name: str, doc_id: int):
    """Get a document by ID"""
    try:
        if name == 'businesses':
            resp = Business.get(id=doc_id, index=name)
        elif name == 'tips':
            resp = Tip.get(id=doc_id, index=name)
        elif name == 'users':
            resp = User.get(id=doc_id, index=name)
        elif name == 'checkins':
            resp = Checkin.get(id=doc_id, index=name)
        elif name == 'reviews':
            resp = Review.get(id=doc_id, index=name)
        else:
            raise GenericException('unknown index {}'.format(name), 400)
    except TransportError as e:
        raise GenericException(
            message='error getting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    return build_response(resp.to_dict())


@document.route('', methods=["PUT"])
def create_document(name: str, doc_id: int):
    """Add a document"""
    data = request.get_json()

    if name == 'businesses':
        doc = Business(**data)
    elif name == 'tips':
        doc = Tip(**data)
    elif name == 'checkins':
        doc = Checkin(**data)
    elif name == 'users':
        doc = User(**data)
    elif name == 'reviews':
        doc = Review(**data)
    else:
        raise GenericException('unknown index {}'.format(name), 400)

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


@document.route('', methods=["DELETE"])
def delete_document(name: str, doc_id: int):
    try:
        if name == 'businesses':
            Business.get(id=doc_id, index=name).delete(index=name)
        elif name == 'tips':
            Tip.get(id=doc_id, index=name).delete(index=name)
        elif name == 'checkins':
            Checkin.get(id=doc_id, index=name).delete(index=name)
        elif name == 'users':
            User.get(id=doc_id, index=name).delete(index=name)
        elif name == 'reviews':
            Review.get(id=doc_id, index=name).delete(index=name)
        else:
            raise GenericException('unknown index {}'.format(name), 400)
    except TransportError as e:
        raise GenericException(
            message='error deleting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    build_response({'acknowledged': True})
