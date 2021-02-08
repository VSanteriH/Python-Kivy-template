#Code by Santeri Hartikainen
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.clearcolor = (.7, .9, .8, 1)

#Window.clearcolor = (.94, 1, 1, 1)
#size and position for testing
Window.size = (360, 640)#Samsung s5 size
Window.left = 1500

#external py code files
import popup
import changecolor
import content

class MainWindow(Screen):
    articleammount = 10 
    articleheight = 140 

class AddNew(Widget):
    def AddToList(title, text):
        print(title, text)
        content.TextContent.updateList(title, text)
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
    def AddToList(self,title, text):
        
        AddNew.AddToList(title, text)

if __name__ == "__main__":
    #changecolor.FindFiles()#Use this to change your projects black icons to white in icons folder.
    app = MainApp()
    app.run()
    
    
    

#Builder.load_file("main.kv")#Needed for popup
    
