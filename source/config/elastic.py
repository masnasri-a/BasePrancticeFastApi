"""
    ELASTIC CONFIG MODULE
"""

from elasticsearch import Elasticsearch

def connect() -> Elasticsearch:
    es = Elasticsearch("http://192.168.29.86:9200/")
    return es
