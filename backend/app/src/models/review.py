from elasticsearch_dsl import Document, Text, Date, Keyword, Short, Index


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
        name = 'reviews'

    @staticmethod
    def set_up(create: bool = False):
        """Set up the index"""
        reviews = Index('reviews')

        # register document with index
        reviews.document(Review)

        if create:
            reviews.delete(ignore=404)
            reviews.create()
