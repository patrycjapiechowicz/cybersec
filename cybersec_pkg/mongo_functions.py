from pymongo import MongoClient
from pymongo.collection import Collection
from typing import List


def select_label_01(collection: Collection, n: int = 1, s: int = 0) -> List[dict]:
    """Return list of `n` documents from `collection` with "label" field set to 0 or 1, starting from `s` + 1.

    Keyword arguments:
    collection -- name of collection to get documents from
    n -- number of documents to obtain
    s -- number of documents to skip
    """
    return list(collection.find({"label": {"$ne": -1}}).skip(s).limit(n))
