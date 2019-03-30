"""Misc functions"""
from elasticsearch_dsl import Index


def set_up(name: str, class_name: str, create: bool = False):
    index = Index(name)
    index.document(class_name)

    if create:
        index.delete(ignore=404)
        index.create()
