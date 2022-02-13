from available_colors import *

avail_colors = get_available_colors('dict')
print(avail_colors)
def color2name(new_colors):
    for i in new_colors:
        print(avail_colors[i])

color2name([(170, 127, 46)])
