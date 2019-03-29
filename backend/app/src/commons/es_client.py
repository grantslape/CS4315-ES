"""static for getting es client"""
from flask import g
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections

from settings import ES_HOST, ES_PORT


# New way, use the DSL
def setup_conn():
    connections.create_connection(hosts=[ES_HOST], timeout=20)


def get_client() -> Elasticsearch:
    """
    deprecated
    Get ES client or create
    :return:
    """
    client = g.es if g.es else None
    if client is None:
        client = g.es = Elasticsearch(
            hosts=[{'host': ES_HOST, 'port': ES_PORT}]
        )

    return client
