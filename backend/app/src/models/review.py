from elasticsearch_dsl import Document, Text, Date, Keyword, Short

INDEX_NAME = 'reviews'


class Review(Document):
    business_id = Keyword()
    cool = Short()
    date = Date(default_timezone='UTC', format='date_hour_minute_second')
    funny = Short()
    review_id = Keyword()
    stars = Short()
    text = Text()
    useful = Short()
    user_id = Keyword()

    class Index:
        name = INDEX_NAME
