"""Packed Checkin object"""
from models import TipElastic


class Checkin(object):
    """
    See elastic/checkin.py
    """
    def __init__(self, business_id: str = None, date: str = None):
        self.business_id = business_id
        self.date = date

    def dehydrate(self) -> dict:
        """Serialize self back to ES flat dict"""

    def serialize(self) -> dict:
        """Serialize object back to ES flat dict"""
        return self.__dict__

    @staticmethod
    def hydrate(es_model: TipElastic):
        """
        Hydrate model by building compliment sub-object
        :param es_model: Document representing ES Model
        :return: Tip
        """
        return Checkin(**es_model.to_dict())
