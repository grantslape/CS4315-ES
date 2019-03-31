"""Misc functions"""
from elasticsearch_dsl import Index


def set_up(name: str, class_name, create: bool = False):
    """Register mappings with index, optionally delete and create the index"""
    index = Index(name)
    index.document(class_name)

    if create:
        index.delete(ignore=404)
        index.create()
