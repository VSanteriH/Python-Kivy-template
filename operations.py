from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import os
import random
import time
import content
import app
DATABASE_URL = os.environ['DATABASE_URL'] # Postgres database URL
db = create_engine(DATABASE_URL) # Connect to db
Session = sessionmaker(bind=db)

Base = declarative_base()

class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String(255))
    time = Column(Float(255))

def __get_session():
    """ Returns current database session """
    return Session()

def get_db_data():
    """ 
    Loads X ammount of rows from db and returns object with that data. 
    After data is loaded adds limit ammount to offset,
    so app will load new data instead of old when called.
    """ 
    limit = content.Data.limit
    offset = content.Data.offset
    sql = __get_session().query(Articles).order_by(Articles.time.desc())[offset:offset+limit]
    """ Gets all data between offset and limit ordered by time. """
    print(offset)
    line = 0
    data = []
    content.Data.offset += limit
    for row in sql:
        r = [row.title,row.text]
        data.insert(line, r)
        line +=1
    return data

def load_articles():
    """ Global funtion that is used to make articless. """
    content.Data.data = get_db_data() 
    new_articles = [] 
    
    for file in content.Data.data:
        title = str(file[0])
        text = str(file[1])
        
        article = {
            "title": title,
            "text": text,
        } 
        app.MainWindow.article_ammount += 1
        new_articles.append(article)
    return new_articles

def load_more():
    """ 
    Called from app.py MainWindow when user have scrolled to the bottom.
    Gets X ammount of new articles by using load_articles and add those to articles_container_copy.
    """ 
    articles = load_articles()
    for file in articles:
        arti = content.Article()       
        arti.title = file['title']
        arti.text = file['text']
        
        # Random colors for article background
        arti.r = round(random.uniform(.5, .7), 1)
        arti.b = round(random.uniform(.5, .9), 1)
        arti.g = round(random.uniform(.2, .8), 1)
        container = content.ArticlesContainerCopy.articles_container_copy
        container.height = container.height + content.Article.article_height # Updates ArticlesContainer height.
        container.add_widget(arti) # Add articles to ArticlesContainer copy and local view 


def add_to_list(self):
    """ Called from app.py MainApp when user adds article with data from popup."""
    time_unix = time.time() # Get unix time
    arti = content.Article()       
    arti.title = content.ArticlesContainer.newtitle
    arti.text = content.ArticlesContainer.newtext

    container = content.ArticlesContainerCopy.articles_container_copy

    container.height = container.height + content.Article.article_height # Updates ArticlesContainer height.
    container.add_widget(arti, app.MainWindow.article_ammount) # Add articles to ArticlesContainer copy and local view
    app.MainWindow.article_ammount += 1
    new_row = Articles(title=arti.title, text=arti.text, time=time_unix)
    db = __get_session()
    db.add(new_row)
    db.commit()
    db.close()

def do_list(self):
    """ 
    Adds widgets to ArticlesContainer that contain article title and text. 
    Also adds every added article height to the ArticlesContainer, so app scaless right way.
    """
    super(content.ArticlesContainer, self).__init__()
    self.orientation = "vertical"
    self.size_hint_y=None
    self.height=0
    for file in content.Data.articles_list:
        arti = content.Article()       
        arti.title = file['title']
        arti.text = file['text']
        
        # Random colors for article background
        arti.r = round(random.uniform(.5, .7), 1)
        arti.b = round(random.uniform(.5, .9), 1)
        arti.g = round(random.uniform(.2, .8), 1)
        self.height = self.height + content.Article.article_height
        self.add_widget(arti) # add articles to ArticlesContainer  