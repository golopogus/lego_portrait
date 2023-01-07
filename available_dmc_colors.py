import json

color_dict = {}

f = open('color_dict.json')

data = json.load(f)
color_list = ["891","326","3847","938","3865"]#["720","606","444","307","740","677"]#["05","3733","33","502","3809","803","310"]
for key,value in data.items():
    if value in color_list:
        #print(key)
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




