from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
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



class Article(BoxLayout):
    label_title = StringProperty()
    label_text = StringProperty()
    le = 0
    sizeY = 140 #Sets height of article

#Gets X ammount of Article classes and make 1 element of those
class TextContent(BoxLayout):
    articlesList = []
    startpos = len(articlesList)
    articles = loadarticles(startpos, articlesList)
    articlesList = articles 
    def Update(pp, **kwargs):
        super(TextContent, self).__init__(**kwargs)
        TextContent.articlesList = []
        TextContent.startpos = 10
        TextContent.articles = loadarticles(TextContent.startpos, TextContent.articlesList)
        print(TextContent.articles)
        TextContent.articlesList = TextContent.articles 
        TextContent.doList(TextContent, **kwargs)

    def doList(self, **kwargs):
        super(TextContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        for file in self.articlesList:
            lbl = Article() 
            
            lbl.label_title = file['title']
            lbl.label_text = file['text']

            self.add_widget(lbl)
            
        self.len = len(self.articlesList)
        app.MainWindow.SiteLenght(self,self.len)
    def __init__(self, **kwargs):
        self.doList()
        
    
