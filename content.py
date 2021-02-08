from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
import app
import random

from kivy.lang import Builder
#from kivy.uix.widget import Widget
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



class Article(BoxLayout):
    label_title = StringProperty()
    label_text = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    le = 0
    sizeY = 140 #Sets height of article

#Gets X ammount of Article classes and make 1 element of those
class TextContent(BoxLayout):
    articlesList = []
    startpos = len(articlesList)
    articles = loadarticles(startpos, articlesList) #Gets aricles from 0 to 10 and add those to oldList and returns that
    articlesList = articles 

    def updateList(title, text):
        #super(TextContent, self).__init__(**kwargs)
        lbl = Article()       
        lbl.label_title = title
        lbl.label_text = text
        print(TextContent)
       # TextContent.add_widget(lbl)#add articles to TextContent 
        #TextContent.articlesList.append(lbl)
        
        #print( TextContent.articlesList)
        pass

    def doList(self, **kwargs):
        print(self)
        super(TextContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        for file in self.articlesList:
            lbl = Article()       
            lbl.label_title = file['title']
            lbl.label_text = file['text']
            lbl.r = round(random.uniform(.5, .7), 1)
            lbl.b = round(random.uniform(.5, .9), 1)
            lbl.g = round(random.uniform(.2, .8), 1)

            print(lbl.r)

            self.add_widget(lbl)#add articles to TextContent   
        self.len = len(self.articlesList)
       # app.MainWindow.SiteLenght(self,self.len)
        
    def __init__(self, **kwargs):
        self.doList()
        
        