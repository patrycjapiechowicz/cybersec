from pymongo import MongoClient


def select_label_01(collection, n=1):
    """Return `n` documents from `collection` with "label" field set to 0 or 1.

    Keyword arguments:
    collection -- name of collection to get documents from
    n -- number of documents to obtain
    """
    return collection.find({"label": {"$ne": -1}}).limit(n)
