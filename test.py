"""pylint test"""
from pymongo import MongoClient
from cybersec_pkg.mongo_functions import select_label_01, insert_documents


def test_select_label_01():
    """Test function"""
    client = MongoClient(
        "mongodb://cybersec:cybersec2021@146.59.3.95:27017/?authSource=cybersec"
    )
    test_db = client.cybersec
    col = test_db.cybersec
    cursor_list = select_label_01(col, 100)
    id_doc_100th = cursor_list[99]["_id"]

    assert id_doc_100th == select_label_01(col, 1, 99)[0]["_id"]


def test_insert_documents():
    """Test function"""
    client = MongoClient(
        "mongodb://cybersec:cybersec2021@146.59.3.95:27017/?authSource=cybersec"
    )
    test_db = client.cybersec
    col = test_db.test
    test_db.drop_collection(col)
    cursor_list = [
        {"_id": 1, "val": 1},
        {"_id": 2, "val": 2},
        {"_id": 3, "val": 3},
    ]
    inserted_documents = insert_documents(col, cursor_list)

    assert len(inserted_documents) == 3
    assert inserted_documents == [1, 2, 3]
