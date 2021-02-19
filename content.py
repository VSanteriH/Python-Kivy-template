from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from dotenv import load_dotenv
import operations
load_dotenv()

class Data():
    articles_list = []
    data = []
    offset = 0
    limit = 500

class Article(BoxLayout):
    """ Handless article generation. """
    title = StringProperty()
    text = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    article_height = 140 # Sets height of single article

class ArticlesContainerCopy():
    """ Copy of ArticlesContainer that is used to store ArticlesContainer data after app starts. """
    first_load = True  
    articles_container_copy = ObjectProperty # ArticlesContainer is saved to this object

class ArticlesContainer(BoxLayout): 
    """ Called at the start and every time user scrolls at the bottom."""
    startpos = len(Data.articles_list)
    articles = operations.load_articles() # Gets aricles from 0 to 10 and add those to oldList and returns that
    Data.articles_list = articles 
    newtitle = StringProperty()
    newtext = StringProperty()
   
    def __init__(self, **kwargs):
        """ Called at the start of app and when data is added from popup. """
        if ArticlesContainerCopy.first_load == True:
            operations.do_list(self)
            ArticlesContainerCopy.first_load = False 
            ArticlesContainerCopy.articles_container_copy = self # Adds first ArticlesContainer class to articles_container_copy ObjectProperty so data can be added to list later
        else:
            operations.add_to_list(self)
        
