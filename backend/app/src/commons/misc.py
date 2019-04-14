"""Misc functions"""
import arrow
from elasticsearch_dsl import Index


def set_up(name: str, class_name, create: bool = False):
    """Register mappings with index, optionally delete and create the index"""
    index = Index(name)
    index.document(class_name)

    if create:
        index.delete(ignore=404)
        index.create()


def format_date(date: str) -> str:
    """
    Take a date and reformat it
    :param date: date as a str
    :return: date as a formatted str
    """
    return arrow.get(date).format('YYYY-MM-DDTHH:mm:ss')
