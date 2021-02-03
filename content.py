from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
def loadarticles(lenght ,articlesList):
    data1 = JsonStore('content.json')
    data = data1.get('rows')
    oldList = articlesList
 
    for file in data[lenght: lenght+3]:
        title = str(file['title'])
        text = str(file['text'])
        
        article = {
        "title": title,
        "text": text,
        } 
        oldList.append(article)
    
    return oldList
    
class Article(Label):
    label_title = Label()
    label_text = Label()

class TextContent(Screen):
    articlesList = []
    length = len(articlesList)
    articles = loadarticles(length, articlesList)
    articlesList = articles
    print(articlesList)
    def __init__(self, **kwargs):
        super(TextContent, self).__init__(**kwargs)
        for file in self.articlesList:
            lbl = Article() 
            lbl.label_title.text = file['title']
            lbl.label_text.text = file['text']
            print(lbl.label_title.text)
            self.add_widget(lbl)
            
            
