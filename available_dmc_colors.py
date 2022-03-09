import json

color_dict = {}

f = open('color_dict.json')

data = json.load(f)

for key,value in data.items():
    json_list = json.loads(key)
    rgb = (int(json_list[0]),int(json_list[1]),int(json_list[2]))
    color_dict[rgb] = value

def get_available_colors(arg):

    if arg == 'list':
        color_rgb = []
        for color in color_dict:
            color_rgb.append(color)
        return(color_rgb)
      
    elif arg == 'dict':
        return color_dict




