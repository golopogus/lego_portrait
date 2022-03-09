from crop_image import *
from pixelate_image import *
from generate_lego_img import *
from available_dmc_colors import *
import json
import os

img = "mj"

height = 128
width = 128

crop_image(img)

pixelate_img(img,width,height)

buy_colors = lego_img(img,width,height)

color_map = get_available_colors('dict')

#print(buy_colors)

buy_names = dict([(color_map.get(key), value) for key, value in buy_colors.items()])

f = open("buy_these_round_plates.json","w")
json.dump(buy_names,f)
f.close()

# total = 0
# for key in buy_colors:
#     total += buy_colors[key]

# print(total)



