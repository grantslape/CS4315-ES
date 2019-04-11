from elasticsearch_dsl import Document, Keyword, Date, Text, Short

INDEX_NAME = 'tips'


class TipElastic(Document):
    user_id = Keyword()
    business_id = Keyword()
    text = Text()
    date = Date(default_timezone='UTC', format='date_hour_minute_second')
    compliment_count = Short()

    class Index:
        name = INDEX_NAME
