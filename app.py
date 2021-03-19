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
            # Fetching News Titles & Articles From Web Scraping
            news_obj = news_scrapped()
            news = news_obj.news_titl()

            # String Raw Scraped News into MongoDB
            store = main_functions()
            store.store_raw_news(json = news, db_name = db_name, collection = collection)

            #

                # mongoClient.createCollection( collection_name = searchString, db_name = db_name)
                # mongoClient.insertRecords( db_name = db_name, collection_name = searchString, records = news)


            return render_template('results.html', news=news)
        except:
            return 'something is wrong'


if __name__ == "__main__":
    app.run(port=5000,debug=True) # running the app on the local machine on port 8000