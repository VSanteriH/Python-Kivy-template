# Code by Santeri Hartikainen
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Size and position for testing
Window.size = (360, 640) # Samsung s5 size
Window.left = 1500 # Right side of screen

Window.clearcolor = (.94, 1, 1, 1)

import changecolor # Change color of files in icons folder
import content # Articless of the app(Mid section)

class MainWindow(Screen):
    articleammount = 10
    articleheight = 140 

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
        # Adds title and text to TextContent class StringObjects
        content.TextContent.newtitle = title
        content.TextContent.newtext = text
        content.TextContent() # Calls TextContent class whoms __init__ that calls updateList()

if __name__ == "__main__":
    # changecolor.find_files()   #Use this to change your projects black icons to white in icons folder.
    app = MainApp()
    app.run()
