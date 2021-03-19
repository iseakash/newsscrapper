import pymongo
import pandas as pd
import json


class main_functions():

    def __init__(self):
        pass

    def store_raw_news(self, db_name, collection, json):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        table.insert_many(json)
        return True
        # news = db[collection].find({})
        # mongoClient = MongoDBManagement(username='new_db_123', password='new_db_123')
        # mongoClient.createCollection(collection_name=collection, db_name=db_name)
        # mongoClient.insertRecords(db_name=db_name, collection_name=collection, records=self.json)

    def read_raw_news(self, db_name, collection):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        response = table.find()
        result = [i for i in response]
        return result

    def clean_database(self, db_name, collection):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        table.remove()
        return True

    def store_news(self, db_name, collection, json):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        table.insert_many(json)
        return True

    def get_news(self, db_name, collection):
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn[db_name]
        table = db[collection]
        response = table.find()
        result = [i for i in response]
        return result