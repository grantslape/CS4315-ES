"""Packed review object"""
from commons import format_date
from models import ReviewElastic


class Review(object):
    """
    See elastic/review.py
    """
    def __init__(self, **kwargs):
        self.business_id = kwargs['business_id']
        self.cool = kwargs['cool']
        self.date = format_date(kwargs['date'])
        self.funny = kwargs['funny']
        self.review_id = kwargs['review_id']
        self.stars = kwargs['stars']
        self.text = kwargs['text']
        self.useful = kwargs['useful']
        self.user_id = kwargs['user_id']

    def dehydrate(self) -> dict:
        """serialize object back to ES"""
        return self.serialize()

    def serialize(self) -> dict:
        """
        Serialize self to dict for JSON transmission
        :return dict
        """
        return self.__dict__

    @staticmethod
    def hydrate(es_model: ReviewElastic):
        """
        Hydrate model by building compliment sub-object
        :param es_model: Document representing ES Model
        :return: Review
        """
        return Review(**es_model.to_dict())
