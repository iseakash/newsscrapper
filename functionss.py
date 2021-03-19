import pymongo
import pandas as pd
import json


class main_functions():

    def __init__(self):
        pass

    def store_raw_news(self, json, db_name, collection):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        table.insert_many(json)
        # news = db[collection].find({})
        # mongoClient = MongoDBManagement(username='new_db_123', password='new_db_123')
        # mongoClient.createCollection(collection_name=collection, db_name=db_name)
        # mongoClient.insertRecords(db_name=db_name, collection_name=collection, records=self.json)

    def read_raw_news():
        return True

    def store_news(json):
        return True

    def get_news():
        return True