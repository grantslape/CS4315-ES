from elasticsearch_dsl import Document, Keyword, Text, Short, GeoPoint, Boolean


INDEX_NAME = 'businesses'


class BusinessElastic(Document):
    business_id = Keyword()
    name = Text()
    address = Text()
    city = Text(fields={'raw': Keyword()})
    state = Text(fields={'raw': Keyword()})
    postal_code = Text()
    location = GeoPoint()
    stars = Short()
    review_count = Short()
    is_open = Boolean()
    categories = Keyword()
    Ambience = Text()
    BusinessParking = Text()
    GoodForMeal = Text()


    class Index:
        name = INDEX_NAME
