from elasticsearch_dsl import Document, Keyword, Text, Short, Date, Float

INDEX_NAME = 'users'


class User(Document):
    user_id = Keyword()
    name = Text(fields={'raw': Keyword()})
    review_count = Short()
    yelping_since = Date(default_timezone='UTC', format='date_hour_minute_second')
    useful = Short()
    funny = Short()
    cool = Short()
    # Array of year tags
    elite = Date(default_timezone='UTC', format='year')
    # Array of user IDs
    friends = Keyword()
    fans = Short()
    average_stars = Float()
    compliment_hot = Short()
    compliment_more = Short()
    compliment_profile = Short()
    compliment_cute = Short()
    compliment_list = Short()
    compliment_note = Short()
    compliment_plain = Short()
    compliment_cool = Short()
    compliment_funny = Short()
    compliment_writer = Short()
    compliment_photos = Short()

    class Index:
        name = INDEX_NAME
