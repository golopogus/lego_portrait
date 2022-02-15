from email.mime import base
from PIL import Image


# base_width = 96
# base_height = 96

def pixelate_img(img_name, base_width, base_height):

    crop_path = "C:/Users/dolan/Desktop/lego_portrait/cropped_images/cropped_" + img_name + ".png"

    img = Image.open(crop_path)

    img = img.resize((base_width,base_height),resample=Image.BILINEAR)

    result = img.resize(img.size,Image.NEAREST)

    save_path = "C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_" + img_name + ".png"

    img.save(save_path)

    return
