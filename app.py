# doing necessary imports
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
from urllib.request import Request
from MongoDBOperations import MongoDBManagement
from news_scrapper import news_scrapped
from functionss import main_functions
from RepositoryForObject import ObjectRepository
import pymongo
import json


# This is the flask object
app = Flask(__name__)  # initialising the flask app with the name 'app'

#http://localhost:8000 + /
@app.route('/',methods=['GET']) # route with allowed methods as GET
def index():
    if request.method == 'GET':
        try:
            collection = "news_titles"
            db_name = 'news_DB'

            # Fetching News Titles & Articles From Web Scraping
            news_obj = news_scrapped()
            news = news_obj.news_titl()

            # Calling the functionss.py functions
            store = main_functions()

            # Storing Raw Scraped News Into MongoDB
            store.store_raw_news(db_name = db_name, collection = collection, json = news)

            # Pulling Raw Scrapped News From MongoDb
            read_news = store.read_raw_news(db_name = db_name, collection = collection)

            # Cleaning the Database
            store.clean_database(db_name = db_name, collection = collection)

            # Updating The Mongodb Database With New Cleaned News
            store.store_news(db_name = db_name, collection = collection, json = news)

            # Pulling Cleaned News From MongoDb
            store.get_news(db_name = db_name, collection = collection)

            return render_template('results.html', news=read_news)
        except:
            return 'something is wrong'

if __name__ == "__main__":
    app.run(port=5000, debug=True)  # running the app on the local machine on port 8000

            # mongoClient = MongoDBManagement(username='new_db_123', password='new_db_123')
            # # dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
            #
            # if mongoClient.isCollectionPresent(collection_name=searchString, db_name=db_name):
            #     response = mongoClient.findAllRecords(db_name=db_name, collection_name=searchString)
            #     news = [i for i in response]
            #     # reviews.count() > 0:  # if there is a collection with searched keyword and it has records in it
            #     return render_template('results.html', news = news)
            #
            # else:

                # mongoClient.createCollection( collection_name = searchString, db_name = db_name)
                # mongoClient.insertRecords( db_name = db_name, collection_name = searchString, records = news)
