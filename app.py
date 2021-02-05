#Code by Santeri Hartikainen
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior

from kivy.uix.recycleview import RecycleView
Window.clearcolor = (.94, 1, 1, 1)
from kivy.app import runTouchApp
#size and position for testing
Window.size = (360, 640)#Samsung s5 size
Window.left = 1500
import popup
import changecolor
import content
import os
import re

#Classes that can be edited inside main.kv file.
class P(FloatLayout):
    def ClosePopup(self):
        popup.show_popup(True)      
    pass
class MainWindow(Screen, Widget):
    articleammount = 10
    def OpenPopup(self):
        popup.show_popup(False)
    def SiteLenght(self, siteLe):
        articleammount = siteLe 
    pass
class SecondWindow(Screen):
    pass

#Downbar buttons 
class DLWindow(Screen):
    pass
class DMWindow(Screen):
    pass
class DRWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):   
        pass

if __name__ == "__main__":
    #changecolor.FindFiles()#Use this to change your projects black icons to white in icons folder.
    
    app = MainApp()
    app.run()
     
    

#Builder.load_file("main.kv")#Needed for popup
    
