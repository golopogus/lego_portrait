from email.mime import base
from PIL import Image

base_unit = 96
img = Image.open("C:/Users/dolan/Desktop/lego_portrait/cropped_images/cropped_batman2.png")

img = img.resize((base_unit,base_unit),resample=Image.BILINEAR)

result = img.resize(img.size,Image.NEAREST)

img.save("C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_batman2.png")
