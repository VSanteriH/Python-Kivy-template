# Code by Santeri Hartikainen
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.camera import Camera
# Size and position for testing
Window.size = (360, 640) # Samsung s5 size
Window.left = 1500 # Right side of screen

Window.clearcolor = (.94, 1, 1, 1)

import changecolor # Change color of files in icons folder
import content # Articless of the app(Mid section)

class MainWindow(Screen):
    article_ammount = 10
    def scrolls(self , scroll): # Called after scroll is relased
        if(scroll.scroll_y <= 0.001): # When scroll position is at   
            content.ArticlesContainer.load_more(self)
            scroll.scroll_to(content.ArticlesContainerCopy.articles_container_copy.children[10] , padding=0, animate=False)
 
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

    # Called from kv files popup button.
    def AddToList(self,title, text):
        # Adds title and text to ArticlesContainer class StringObjects
        content.ArticlesContainer.newtitle = title
        content.ArticlesContainer.newtext = text
        content.ArticlesContainer() # Calls ArticlesContainer class whoms __init__ that calls updateList()

if __name__ == "__main__":
    # changecolor.find_files()   # Use this to change your projects black icons to white in icons folder.
    app = MainApp()
    app.run()
