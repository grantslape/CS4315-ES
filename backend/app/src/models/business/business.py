from elasticsearch_dsl import Document, Keyword, Text, Short, GeoPoint, Nested, Boolean

from models.business.attributes import Attributes
from models.business.hours import Hours

INDEX_NAME = 'businesses'


class Business(Document):
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
    attributes = Nested(Attributes)
    categories = Keyword()
    hours = Nested(Hours)

    class Index:
        name = INDEX_NAME
