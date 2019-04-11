from elasticsearch_dsl import Document, Keyword, Text, Date, Float, Integer

INDEX_NAME = 'users'


class UserElastic(Document):
    user_id = Keyword()
    name = Text(fields={'raw': Keyword()})
    review_count = Integer()
    yelping_since = Date(default_timezone='UTC', format='date_hour_minute_second')
    useful = Integer()
    funny = Integer()
    cool = Integer()
    # Array of year tags
    elite = Date(default_timezone='UTC', format='year')
    # Array of user IDs
    friends = Keyword()
    fans = Integer()
    average_stars = Float()
    compliment_hot = Integer()
    compliment_more = Integer()
    compliment_profile = Integer()
    compliment_cute = Integer()
    compliment_list = Integer()
    compliment_note = Integer()
    compliment_plain = Integer()
    compliment_cool = Integer()
    compliment_funny = Integer()
    compliment_writer = Integer()
    compliment_photos = Integer()

    class Index:
        name = INDEX_NAME
