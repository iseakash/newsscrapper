# doing necessary imports
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
from urllib.request import Request
import pymongo


# This is the flask object
app = Flask(__name__)  # initialising the flask app with the name 'app'

# base url + /
#http://localhost:8000 + /
@app.route('/',methods=['GET']) # route with allowed methods as GET
def index():
    if request.method == 'GET':
        try:
            searchString = "news_titles"
            dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
            db = dbConn['newscrawlerDB'] # connecting to the database called crawlerDB
            news = db[searchString].find({}) # searching the collection with the name same as the keyword
            if news.count() > 0:  # if there is a collection with searched keyword and it has records in it
                return render_template('results.html', news=news)  # show the results to user
            else:
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
                news_url = 'https://economictimes.indiatimes.com/'
                uClient = uOpen(Request(news_url, headers = header)) # requesting the webpage from the internet
                newsPage = uClient.read() # reading the webpage
                uClient.close() # closing the connection to the web server
                news_html = bs(newsPage, "html.parser") # parsing the webpage as HTML
                bigboxes = news_html.findAll('ul', {"class": "newsList clearfix"}) # searching for appropriate tag to get news titles
                box = bigboxes[0].contents  # taking the first iteration (for demo)
                del box[10:] # deleting news more than 10 counts
                news = [] # initializing an empty list for news title

                table = db[searchString] # creating a collection with the same name as search string. Tables and Collections are analogous.

                for b in box:
                    topicLink = "https://economictimes.indiatimes.com/" + b.a['href']  # extracting the actual product link
                    topicRes = uOpen(Request(topicLink, headers = header))  # getting the product page from server

                    topic_html = bs(topicRes, "html.parser")  # parsing the product page as HTML
                    title_content = topic_html.findAll('div', {"class": "topPart clearfix tac"})  # searching for appropriate tag to get news titles
                    body_content = topic_html.findAll('div', {"class": "artSyn bgPink"})  # searching for appropriate tag to get news titles

                    title = title_content[0].h1.text
                    content = body_content[0].h2.text

                    my_dict = {"Title": title, "Article": content}
                    x = table.insert_one(my_dict)  # insertig the dictionary containing the news comments to the collection
                    news.append(my_dict)

            return render_template('results.html', news=news)
        except:
            return 'something is wrong'


if __name__ == "__main__":
    app.run(port=5000,debug=True) # running the app on the local machine on port 8000