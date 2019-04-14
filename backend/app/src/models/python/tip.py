"""Packed tip object"""
from commons import format_date
from models import TipElastic


class Tip(object):
    """
    See elastic/tip.py
    """
    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.business_id = kwargs['business_id']
        self.text = kwargs['text']
        self.date = format_date(kwargs['date'])
        self.compliment_count = kwargs['compliment_count']

    def dehydrate(self) -> dict:
        """Serialize back to ES flat dict"""
        # If we needed to massage it would go here
        return self.serialize()

    def serialize(self) -> dict:
        """
        Serialize self to dict for JSON transmission
        :return dict
        """
        return self.__dict__

    @staticmethod
    def hydrate(es_model: TipElastic):
        """
        Hydrate model as needed
        :param es_model:
        :return: Tip
        """
        return Tip(**es_model.to_dict())
