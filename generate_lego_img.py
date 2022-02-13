from PIL import Image
from get_color_to_use import *

size = 96
img = Image.open('C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_batman2.png')

pix = img.load()

for x in range(size):
    for y in range(size):
        pix[x,y] = new_colors(x,y)

img.save("C:/Users/dolan/Desktop/lego_portrait/lego_img/lego_batman2.png")