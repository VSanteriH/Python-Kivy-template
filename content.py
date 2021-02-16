from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView

from sqlalchemy import create_engine, text
import time
import os
import app
import random
from kivy.lang import Builder
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL'] # Postgres database URL
db = create_engine(DATABASE_URL) # Connect to db

class Data():
    articlesList = []
    data = []
    last_row = 0
    offset = 0

def get_db_data():

    limit = 1000
    offset = Data.offset
    sql = text('SELECT * from Articless LIMIT (:limit) OFFSET (:offset)')
    results = db.execute(sql , {'limit':limit, 'offset':offset})
    line = 0
    data = []
    Data.offset += 1000
    for row in results:
        r = [row['title'],row['text']]
        data.insert(line, r)
        line +=1
    return data

def load_articles():
    all_articles = Data.articlesList
    Data.data = get_db_data() 
    new_articles = [] 
    
    for file in Data.data:
        title = str(file[0])
        text = str(file[1])
        
        article = {
            "title": title,
            "text": text,
        } 
        app.MainWindow.article_ammount += 1
        all_articles.append(article)
        new_articles.append(article)
    Data.last_row = Data.last_row + len(all_articles)
    print( Data.last_row)
    return new_articles

class Article(BoxLayout):
    title = StringProperty()
    text = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    article_height = 140 # Sets height of single article

class ArticlesContainerCopy():
    first_load = True  
    articles_container_copy = ObjectProperty # ArticlesContainer is saved to this object

class ArticlesContainer(BoxLayout): 
    
    startpos = len(Data.articlesList)
    articles = load_articles() # Gets aricles from 0 to 10 and add those to oldList and returns that
    Data.articlesList = articles 
    newtitle = StringProperty()
    newtext = StringProperty()
   
    def add_to_list(self):
        print("Add to List")  
        arti = Article()       
        arti.title = self.newtitle
        arti.text = self.newtext
        ArticlesContainerCopy.articles_container_copy.height = ArticlesContainerCopy.articles_container_copy.height + Article.article_height # Updates ArticlesContainer height.
        ArticlesContainerCopy.articles_container_copy.add_widget(arti, app.MainWindow.article_ammount) # Add articles to ArticlesContainer copy and local view
        app.MainWindow.article_ammount += 1

    def load_more(self):
        print("Load more")  
        articles = load_articles()
        for file in articles:
            arti = Article()       
            arti.title = file['title']
            arti.text = file['text']
            
            # Random colors for article background
            arti.r = round(random.uniform(.5, .7), 1)
            arti.b = round(random.uniform(.5, .9), 1)
            arti.g = round(random.uniform(.2, .8), 1)
            
            ArticlesContainerCopy.articles_container_copy.height = ArticlesContainerCopy.articles_container_copy.height + Article.article_height # Updates ArticlesContainer height.
            ArticlesContainerCopy.articles_container_copy.add_widget(arti) # Add articles to ArticlesContainer copy and local view 


    def do_list(self):
        print("Do list")
        super(ArticlesContainer, self).__init__()
        self.orientation = "vertical"
        self.size_hint_y=None
        self.height=0
        for file in Data.articlesList:
            arti = Article()       
            arti.title = file['title']
            arti.text = file['text']
            
            # Random colors for article background
            arti.r = round(random.uniform(.5, .7), 1)
            arti.b = round(random.uniform(.5, .9), 1)
            arti.g = round(random.uniform(.2, .8), 1)
            self.height = self.height + Article.article_height
            self.add_widget(arti) # add articles to ArticlesContainer  

    def __init__(self, **kwargs):
        if ArticlesContainerCopy.first_load == True:
            self.do_list()
            ArticlesContainerCopy.first_load = False 
            ArticlesContainerCopy.articles_container_copy = self # Adds first ArticlesContainer class to articles_container_copy ObjectProperty so data can be added to list later
        else:
            self.add_to_list()
        
