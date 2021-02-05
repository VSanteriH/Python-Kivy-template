from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
import app
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

class ScrollElement(GridLayout):
    pass

class Article(BoxLayout):
    label_title = StringProperty()
    label_text = StringProperty()
    le = 0

class TextContent(BoxLayout):
    articlesList = []
    length = len(articlesList)
    articles = loadarticles(length, articlesList)
    articlesList = articles 
    def __init__(self, **kwargs):
        super(TextContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        for file in self.articlesList:
            lbl = Article() 
            
            lbl.label_title = file['title']
            lbl.label_text = file['text']

            self.add_widget(lbl)
        self.len = len(self.articlesList)
        app.MainWindow.SiteLenght(self,self.len)
