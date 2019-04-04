from elasticsearch_dsl import Document, Keyword, Date, Index

INDEX_NAME = 'checkins'


class Checkin(Document):
    # TODO: this should be nested in business
    business_id = Keyword()
    date = Date(default_timezone='UTC', format='date_hour_minute_second')

    class Index:
        name = INDEX_NAME
