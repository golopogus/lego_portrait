from PIL import Image
from get_color_to_use import *

# width = 96
# height = 96

def color_count(lego_color,buy_color_code):
    if lego_color in buy_color_code:
        buy_color_code[lego_color] += 1
    else:
        buy_color_code[lego_color] = 1
    return buy_color_code


def lego_img(img_name,width,height):
    img_path = "C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_" + img_name + ".png"
    img = Image.open(img_path)

    pix = img.load()
    buy_color_code = {}
    for x in range(width):
        for y in range(height):
            lego_color = new_colors(x,y,img_name) 
            buy_color_code = color_count(lego_color, buy_color_code)
            pix[x,y] = lego_color
            
    save_path = "C:/Users/dolan/Desktop/lego_portrait/lego_img/lego_" + img_name + ".png"
    img.save(save_path)
    return buy_color_code
