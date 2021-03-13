"""db connection example"""
from pymongo import MongoClient

client = MongoClient(host="147.135.208.243",
                     port=27017,
                     username="cybersecuser",
                     password="SdajhfsdaiFSD",
                     authSource="cybersec")

mydb = client["cybersec"]
mycol = mydb["cybersec"]

mydict = {"name": "John", "address": "Highway 37"}
x = mycol.insert_one(mydict)
print(x)
