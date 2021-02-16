# Code by Santeri Hartikainen
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.core.window import Window
import time
# Size and position for testing
Window.size = (360, 640) # Samsung s5 size
Window.left = 1500 # Right side of screen

Window.clearcolor = (.94, 1, 1, 1)

import changecolor # Change color of files in icons folder
import content # Articless of the app

class MainWindow(Screen):
    article_ammount = 0
    distance = 0 
    def scrolls(self , scroll):
        """ Called every time scoll starts. Checks if we have reached bottom of the screen.
        If so, calls ArticlesContainer.load_more in content.py that loads 1000 rows more.
        After the load is done, scrolls to the previous scroll_y. 
        """
        if(scroll.scroll_y <= MainWindow.distance):
            content.ArticlesContainer.load_more(self)  
            scroll.scroll_to(content.ArticlesContainerCopy.articles_container_copy.children[1000] , padding=0, animate=True)

class SecondWindow(Screen):
    pass

class DownLWindow(Screen):
    pass

class DownRWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):   
        pass

    def AddToList(self,title, text):
        """ Called from kv file popup MainApp section. Gets title and text and add those to ArticleContainer class.
        After that calls ArticleContainer class.
        """
        content.ArticlesContainer.newtitle = title
        content.ArticlesContainer.newtext = text
        content.ArticlesContainer() # Calls ArticlesContainer class whoms __init__ that calls updateList()

if __name__ == "__main__":
    app = MainApp()
    app.run()
