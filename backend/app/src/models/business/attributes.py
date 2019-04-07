from elasticsearch_dsl import InnerDoc, Boolean


class Attributes(InnerDoc):
    """
    TODO: Remove this and flatten into business
    !!! THIS IS NOT A COMPLETE LIST OF ATTRIBUTES !!!
    Attributes are highly variable, sometimes not present, sometimes present with
    null values.  Therefore, pre-processing will handle most categorization for now.
    """
    HasTV = Boolean()
    RestaurantsDelivery = Boolean()
    BikeParking = Boolean()
    OutdoorSeating = Boolean()
    ByAppointmentOnly = Boolean()

