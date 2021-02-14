from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
import app
import random

from kivy.lang import Builder

def loadarticles(lenght ,articlesList):
    data1 = JsonStore('content.json')
    data = data1.get('rows')
    oldList = articlesList
 
    for file in data[lenght: lenght+10]:
        title = str(file['title'])
        text = str(file['text'])
        
        article = {
            "title": title,
            "text": text,
        } 
        oldList.append(article)
    return oldList

class FirstLoad():
    first_load = True  
    textcont = ObjectProperty

class Article(BoxLayout):
    title = StringProperty()
    text = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    sizeY = 140 # Sets height of single article

class TextContent(BoxLayout): 
    articlesList = []
    startpos = len(articlesList)
    articles = loadarticles(startpos, articlesList) # Gets aricles from 0 to 10 and add those to oldList and returns that
    articlesList = articles 
    newtitle = StringProperty()
    newtext = StringProperty()
 
    
    def update_list(self):
        print("Add to List")
        super(TextContent, self).__init__()
        FirstLoad.textcont.orientation = "vertical" 
        arti = Article()       
        arti.title = self.newtitle
        arti.text = self.newtext
        FirstLoad.textcont.height = FirstLoad.textcont.height + Article.sizeY # Updates TextContent height.
        FirstLoad.textcont.add_widget(arti,app.MainWindow.article_ammount) # add articles to TextContent copy and local view
       
    
    def do_list(self):
        print("Do list")
        super(TextContent, self).__init__()
        self.orientation = "vertical"
        self.size_hint_y=None
        self.height=0
        for file in self.articlesList:
            arti = Article()       
            arti.title = file['title']
            arti.text = file['text']
            
            # Random colors for article background
            arti.r = round(random.uniform(.5, .7), 1)
            arti.b = round(random.uniform(.5, .9), 1)
            arti.g = round(random.uniform(.2, .8), 1)
            self.height = self.height + Article.sizeY
            self.add_widget(arti) # add articles to TextContent  

    def __init__(self, **kwargs):
        if FirstLoad.first_load == True:
            self.do_list()
            FirstLoad.first_load = False 
            FirstLoad.textcont = self # Adds first TextContent class to textcont ObjectProperty so data can be added to list later
        else:
            self.update_list()
        
