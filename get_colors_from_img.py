from PIL import Image
import os

def get_colors(x,y,img_name):
    cwd = str(os.getcwd())
    img_path = os.path.join(cwd,"pixelated_images","pixelated_" + img_name + ".png")
    #img_path = "C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_" + img_name + ".png"
    img = Image.open(img_path)

    pix = img.load()

    color = pix[x,y]

    return color
