"""Packed user object"""
from commons import format_date
from models import UserElastic


class User(object):
    """
    See elastic/user.py
    """
    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.name = kwargs['name']
        self.review_count = kwargs['review_count']
        self.yelping_since = format_date(kwargs['yelping_since'])
        self.useful = kwargs['useful']
        self.funny = kwargs['funny']
        self.cool = kwargs['cool']
        self.elite = getattr(kwargs, 'elite', None)
        self.friends = kwargs['friends']
        self.fans = kwargs['fans']
        self.average_stars = kwargs['average_stars']
        self.compliment = kwargs['compliment']

    def dehydrate(self) -> dict:
        """Serialize object back to ES flat dict"""
        payload = self.serialize()
        compliment = payload.pop('compliment')

        for key, value in compliment.items():
            payload['compliment_{}'.format(key)] = value

        return payload

    def serialize(self) -> dict:
        """
        Serialize self to dict for JSON transmission
        :return dict
        """
        return self.__dict__

    @staticmethod
    def hydrate(es_model: UserElastic):
        """
        Hydrate model by building compliment sub-object
        :param es_model: Document representing ES Model
        :return: User
        """
        model_dict = es_model.to_dict()
        compliment = {}

        for key in list(model_dict.keys()):
            # key_items = ['compliment', 'foo']
            key_items = key.split('_')
            if key_items[0] == 'compliment':
                compliment[key_items[1]] = model_dict.pop(key)

        model_dict['compliment'] = compliment
        return User(**model_dict)
