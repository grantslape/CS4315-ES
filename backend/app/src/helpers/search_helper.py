from elasticsearch_dsl import Search, Q

from commons import GenericException, get_logger
from models.python import Business, Review

FUZZY_FIELDS = ['text', 'city', 'state', 'name', 'categories']
INDICES = ['businesses', 'reviews']

logger = get_logger(__name__)


def generic_search(query: str, page_size: int = 10, offset: int = 0):
    """Search
{
    "query": {
        "multi_match": {
            "query": "Las Vegas pet spa",
            "fields": ["text", "city", "state", "name", "categories"]
        }
    },
    "indices_boost": [
        {"businesses": 2}
    ],
    "highlight": {
        "fields": {
            "text": {}
        }
    }
}
    """
    query = Q(
        'multi_match',
        query=query,
        fields=FUZZY_FIELDS
    )
    # Make query and highlight
    s = Search(index=INDICES).query(query).highlight_options(order='score').highlight('text')

    s = s.extra(indices_boost=[{"businesses": 2}])

    s = s[offset:offset + page_size]
    return s.execute()


def hydrate_models(models):
    payload = []
    for model in models:
        if model.meta.index == 'businesses':
            payload.append(Business.hydrate(model).serialize())
        elif model.meta.index == 'reviews':
            review = Review.hydrate(model)
            # dynamically adding a prop is a little smelly
            review.highlights = list(model.meta.highlight.text)
            payload.append(review.serialize())
        else:
            message = 'model not found for index: {}'.format(model.meta.index)
            logger.error(message)
            raise GenericException(message)

    return payload
