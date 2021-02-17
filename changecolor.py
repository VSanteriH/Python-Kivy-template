'''
This file is used for changing icons color from black to white, so icon color could be 
changed in code.
Icon images are from https://github.com/iconic/open-iconic/tree/master/png
'''

import os
from PIL import Image # https://pillow.readthedocs.io/en/stable/

def find_files():
    """ Finds all files from icons folder that name ends with .png """
    directory = os.fsencode( "icons/") # Gets folder where icons are located
 
    for file in os.listdir(directory): # Gets every file from folder
        filename = os.fsdecode(file)
        if filename.endswith(".png"):
            change_color("icons/" + filename)
            continue
        else:
            continue
        
def change_color(image):
    """ Changes every black pixel to white from image that was send to it. Skips transperent pixels """
    newimage = Image.open(image)
    
    for x in range(newimage.size[0]):# Goes trought every pixel of image in X axis
        for y in range(newimage.size[1]): # In Y axis
            r,g,b,a = newimage.getpixel((x,y)) # Get pixels color in rgb
            if r == 0 and g == 0 and b == 0 and a > 0: # If pixel is black and not transparent.
                newimage.putpixel((x,y), (255,255,255,a)) # Change color to white. Keep transperency.

    newimage.save(image) # Saves a file over the old one.
