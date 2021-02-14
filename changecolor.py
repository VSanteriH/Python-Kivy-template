'''
Change color
==============

This file is used for changing icons color from black to white, so icon color could be 
changed in code.

'''

import os
from PIL import Image # https://pillow.readthedocs.io/en/stable/

def find_files():
    # Gets folder wher icons are located
    directory = os.fsencode( "icons/")

    # Gets every file from folder
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        # Gets png image files and calls ChangeColor
        if filename.endswith(".png"): 
            change_color("icons/" + filename)
            continue
        else:
            continue
        
# Changes black pixels to white
def change_color(image):
    newimage = Image.open(image)
    # Goes trought every pixel from image and changes them to white
    for x in range(newimage.size[0]):
        for y in range(newimage.size[1]):
            r,g,b,a = newimage.getpixel((x,y))
            if r == 0 and g == 0 and b == 0 and a > 0: 
                newimage.putpixel((x,y), (255,255,255,a))

    newimage.save(image) # Saves a file over the old one.
