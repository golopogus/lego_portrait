from email.mime import base
from PIL import Image
import os

# base_width = 96
# base_height = 96

def pixelate_img(img_name, base_width, base_height):

    cwd = str(os.getcwd())
    crop_path = os.path.join(cwd,"cropped_images","cropped_" + img_name + ".png")
    
    #crop_path = "C:/Users/dolan/Desktop/lego_portrait/cropped_images/cropped_" + img_name + ".png"

    img = Image.open(crop_path)

    img = img.resize((base_width,base_height),resample=Image.BILINEAR)

    result = img.resize(img.size,Image.NEAREST)


    save_path = os.path.join(cwd,"pixelated_images","pixelated_" + img_name + ".png")
    #save_path = "C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_" + img_name + ".png"

    result.save(save_path)

    return
