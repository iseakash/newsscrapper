# doing necessary imports
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
from urllib.request import Request

class news_scrapped():

    def __init__(self):
        print("Empty")

    def news_titl(self):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        news_url = 'https://economictimes.indiatimes.com/'
        uClient = uOpen(Request(news_url, headers=header))  # requesting the webpage from the internet
        newsPage = uClient.read()  # reading the webpage
        uClient.close()  # closing the connection to the web server
        news_html = bs(newsPage, "html.parser")  # parsing the webpage as HTML
        bigboxes = news_html.findAll('ul', {"class": "newsList clearfix"})  # searching for appropriate tag to get news titles
        box = bigboxes[0].contents  # taking the first iteration (for demo)
        del box[10:]  # deleting news more than 10 counts
        news = []  # initializing an empty list for news title

        for b in box:
            topicLink = "https://economictimes.indiatimes.com/" + b.a['href']  # extracting the actual product link
            topicRes = uOpen(Request(topicLink, headers=header))  # getting the product page from server

            topic_html = bs(topicRes, "html.parser")  # parsing the product page as HTML
            title_content = topic_html.findAll('div', {"class": "topPart clearfix tac fixedOnLoad"})  # searching for appropriate tag to get news titles
            body_content = topic_html.findAll('div',{"class": "artSyn bgPink"})  # searching for appropriate tag to get news article

            title = title_content[0].h1.text
            content = body_content[0].h2.text

            my_dict = {"Title": title, "Article": content}
            # fns = main_functions()
            # fns.store_raw_news(collection = collection, db_name = db_name, json = my_dict)
            news.append(my_dict)
        return news
