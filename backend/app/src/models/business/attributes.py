from elasticsearch_dsl import InnerDoc, Boolean


class Attributes(InnerDoc):
    """
    Attributes are highly variable, sometimes not present, sometimes present with
    null values.  Therefore, pre-processing will handle most categorization for now.
    """
    HasTV = Boolean()
    RestaurantsDelivery = Boolean()
    BikeParking = Boolean()
    OutdoorSeating = Boolean()
    ByAppointmentOnly = Boolean()

