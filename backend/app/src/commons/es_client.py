"""static for getting es client"""
from flask import g
from elasticsearch import Elasticsearch

from settings import ES_HOST, ES_PORT


def get_client():
    """Get ES client or create"""
    client = g.es if g.es else None
    if client is None:
        client = g.es = Elasticsearch(
            hosts=[{'host': ES_HOST, 'port': ES_PORT}]
        )

    return client
