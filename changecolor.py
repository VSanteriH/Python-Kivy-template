#Changes black pixels to white
#This is usefull if we have black icons and want them to be white so icon color manupalation would be possible inside kv file.
import os
from PIL import Image #https://pillow.readthedocs.io/en/stable/

#Finds all png images in icons folder and chages those images black pixels to white
def FindFiles():
    directory = os.fsencode( "icons/")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".png"): 
            ChangeColor("icons/" + filename)
            continue
        else:
            continue
def ChangeColor(image):
    newimage = Image.open(image)

    for x in range(newimage.size[0]):
        for y in range(newimage.size[1]):
            r,g,b,a = newimage.getpixel((x,y))
            if r == 0 and g == 0 and b == 0 and a > 0: #Changes black pixels to white
                newimage.putpixel((x,y), (255,255,255,a)) 
           # if r == 255 and g == 255 and b == 255 and a > 0: #Changes white pixels to black
                #newimage.putpixel((x,y), (0,0,0,a)) 
                
    newimage.save(image)#saves a file over the old one.

            

