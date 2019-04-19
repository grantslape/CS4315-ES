"""Endpoints for indexing and retrieving documents"""
from elasticsearch import TransportError
from flask import Blueprint, request

from commons import GenericException, build_response
from models import CheckinElastic, BusinessElastic, TipElastic, UserElastic, ReviewElastic
from models.python import Tip, Checkin, User, Business, Review


document = Blueprint('document', __name__)


@document.route('', methods=["GET"])
def get(name: str, doc_id: int):
    """Get a document by ID"""
    try:
        if name == 'businesses':
            resp = Business.hydrate(BusinessElastic.get(id=doc_id, index=name))
        elif name == 'tips':
            resp = Tip.hydrate(TipElastic.get(id=doc_id, index=name))
        elif name == 'users':
            resp = User.hydrate(UserElastic.get(id=doc_id, index=name))
        elif name == 'checkins':
            resp = Checkin.hydrate(CheckinElastic.get(id=doc_id, index=name))
        elif name == 'reviews':
            resp = Review.hydrate(ReviewElastic.get(id=doc_id, index=name))
        else:
            raise GenericException('unknown index {}'.format(name), 400)
    except TransportError as e:
        raise GenericException(
            message='error getting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    return build_response(resp.serialize())


@document.route('', methods=["PUT"])
def create_document(name: str, doc_id: int):
    """Add a document"""
    data = request.get_json()

    if name == 'businesses':
        business = Business(**data)
        doc = BusinessElastic(**business.dehydrate())
    elif name == 'tips':
        tip = Tip(**data)
        doc = TipElastic(**tip.dehydrate())
    elif name == 'checkins':
        checkin = Checkin(**data)
        doc = CheckinElastic(**checkin.dehydrate())
    elif name == 'users':
        user = User(**data)
        doc = UserElastic(**user.dehydrate())
    elif name == 'reviews':
        review = Review(**data)
        doc = ReviewElastic(**review.dehydrate())
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
            BusinessElastic.get(id=doc_id, index=name).delete(index=name)
        elif name == 'tips':
            TipElastic.get(id=doc_id, index=name).delete(index=name)
        elif name == 'checkins':
            CheckinElastic.get(id=doc_id, index=name).delete(index=name)
        elif name == 'users':
            UserElastic.get(id=doc_id, index=name).delete(index=name)
        elif name == 'reviews':
            ReviewElastic.get(id=doc_id, index=name).delete(index=name)
        else:
            raise GenericException('unknown index {}'.format(name), 400)
    except TransportError as e:
        raise GenericException(
            message='error deleting document {}'.format(doc_id),
            status_code=e.status_code,
            payload=e.info
        )

    build_response({'acknowledged': True})
