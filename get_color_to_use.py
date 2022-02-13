import math
from get_colors_from_img import *
from available_colors import *

#pic_size = 48
avail_colors = get_available_colors('list')

def closest_colors(img_color):
    r,g,b = img_color
    lowest_val = 10000
    closest_match = ''
    for color in avail_colors:
        ra,ga,ba = color
        #print(color)
        result = math.sqrt(abs(r - ra) + abs(g - ga) + abs(b - ba))
        if result < lowest_val:
            lowest_val = result
            closest_match = color
    return(closest_match)

def new_colors(x,y):
    img_color = closest_colors(get_colors(x,y))
    return img_color

# new_colors = []
# for x in range(48):
#     for y in range(48):
#         img_color = closest_colors(get_colors(x,y))
#         new_colors.append(img_color)


