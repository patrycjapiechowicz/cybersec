"""
Module contains functions that handle MongoDB operations.
"""

from typing import List

from pymongo.collection import Collection


def select_label_01(
    collection: Collection, obtain: int = 1, skip: int = 0
) -> List[dict]:
    """
    Return list of `obtain` documents from `collection` with "label" field
    set to 0 or 1, starting from `skip` + 1.

    Keyword arguments:
    collection -- name of collection to get documents from
    obtain -- number of documents to obtain
    skip -- number of documents to skip
    """
    return list(collection.find({"label": {"$ne": -1}}).skip(skip).limit(obtain))
