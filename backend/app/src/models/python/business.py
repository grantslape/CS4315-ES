"""Packed business object"""
from models import BusinessElastic

ATTRIBUTES = (
    'AcceptsInsurance', 'AgesAllowed', 'Alcohol', 'Ambience', 'BYOB', 'BYOBCorkage',
    'BestNights', 'BikeParking', 'BusinessAcceptsBitcoin', 'BusinessAcceptsCreditCards',
    'BusinessParking', 'ByAppointmentOnly', 'Caters', 'CoatCheck', 'Corkage',
    'DietaryRestrictions', 'DogsAllowed', 'DriveThru', 'GoodForDancing', 'GoodForKids',
    'GoodForMeal', 'HairSpecializesIn', 'HappyHour', 'HasTV', 'Music', 'NoiseLevel',
    'Open24Hours', 'OutdoorSeating', 'RestaurantsAttire', 'RestaurantsCounterService',
    'RestaurantsDelivery', 'RestaurantsGoodForGroups', 'RestaurantsPriceRange2',
    'RestaurantsReservations', 'RestaurantsTableService', 'RestaurantsTakeOut',
    'Smoking', 'WheelchairAccessible', 'WiFi'
)


class Business(object):
    """
    See elastic/business.py
    """
    def __init__(self, **kwargs):
        self.business_id = kwargs['business_id']
        self.name = kwargs['name']
        self.address = kwargs['address']
        self.city = kwargs['city']
        self.state = kwargs['state']
        self.postal_code = kwargs['postal_code']
        self.location = kwargs['location']
        self.stars = kwargs['stars']
        self.review_count = kwargs['review_count']
        self.is_open = kwargs['is_open']
        self.categories = kwargs['categories']
        self.hours = kwargs['hours']
        self.attributes = kwargs['attributes']

    def dehydrate(self) -> dict:
        """
        Serialize back to ES flat dict
        :return: dict
        """
        payload = self.serialize()
        hours = payload.pop('hours')
        attributes = payload.pop('attributes')
        return {**payload, **hours, **attributes}

    def serialize(self) -> dict:
        """
        Serialize self to dict for JSON transmission
        :return dict
        """
        return self.__dict__

    @staticmethod
    def hydrate(es_model: BusinessElastic):
        """
        hydrate model by building sub object
        TODO: eval sub objects
        :param es_model:
        :return: Business
        """
        model_dict = es_model.to_dict()
        attributes = {}
        hours = {}

        for key in list(model_dict.keys()):
            key_list = key.split('_')
            if key_list[0] == 'open' and key_list[1] == 'period':
                hours[key] = model_dict.pop(key)
            elif key in ATTRIBUTES:
                attributes[key] = model_dict.pop(key)

        model_dict['attributes'] = attributes
        model_dict['hours'] = hours

        return Business(**model_dict)
