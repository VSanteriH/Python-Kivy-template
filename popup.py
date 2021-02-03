#PopUp
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import app
PUopen = False
show = app.P()#This "P" contains FloatLayout that is in main.kv file.
popupWindow = Popup(title="Add new", content=show, size_hint=(None,None), size=(300,400))

#To open PopUp calls "OpenPopup" function inside "MainWindow" Class.
#Closes this popup by calling "ClosePopp insede "P" Class.
#These Functions give "PUopen" Boolean parameter witch decides if Popup will open or close.
def show_popup(PUopen):
    if PUopen == False:    
        popupWindow.open() 
     
    else:    
        popupWindow.dismiss()