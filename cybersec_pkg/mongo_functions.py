"""
Module contains functions that handle MongoDB operations.
"""

from typing import List

from pymongo.collection import Collection


def select_label_01(
    collection: Collection, obtain: int = 1, skip: int = 0
) -> List[dict]:
    """
    Returns list of `obtain` documents from `collection` with "label" field
    set to 0 or 1, starting from `skip` + 1.

    Keyword arguments:
    collection -- name of collection to get documents from
    obtain -- number of documents to obtain
    skip -- number of documents to skip
    """
    return list(collection.find({"label": {"$ne": -1}}).skip(skip).limit(obtain))


def insert_documents(collection: Collection, docs: List[dict]) -> list:
    """
    Uploads documents from the list `docs` to defined `collection`.

    WARNING: documents already existing in collection cause error!

    Keyword arguments:
    collection -- name of collection to insert documents to
    docs -- list of documents to insert
    """

    if collection.name == "cybersec":
        raise KeyError("Cannot insert to collection `cybersec`")
    result = collection.insert_many(docs)
    return result.inserted_ids
