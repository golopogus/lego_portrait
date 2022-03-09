# color_codes = ['FFFFFF','A0A5A9','9BA19D','6D6E5C','6C6E68','05131D','720E0F','C91A09','352100','582A12','958A73','E4CD9E','AA7D55','A95500','FE8A18','F8BB3D','F2CD37','FFF03A','DFEEA5','C7D23C','BBE90B','9B9A5A','237841','4B9F4A','008F9B','0A3463','0055BF','36AEBF','6074A1','3F3691','923978','C870A0','E4ADC8','FCFCFC','FF800D','F08F1C','F5CD2F','F8F184','D9E4A7','84B68D','0020A0','CFE2F7','AEEFEC','A5A5CB','DF6695','9CA3A8','898788','575857','AA7F2E']
# color_names = ['White','Light Bluish Gray','Light Gray','Dark Gray','Dark Bluish Gray','Black','Dark Red','Red','Dark Brown','Reddish Brown','Dark Tan','Tan','Medium Nougat','Dark Orange','Orange','Bright Light Orange','Yellow','Bright Light Yellow','Yellowish Green','Medium Lime','Lime','Olive Green','Green','Bright Green','Dark Turquoise','Dark Blue','Blue','Medium Azure','Sand Blue','Dark Purple','Magenta','Dark Pink','Bright Pink','Trans-Clear','Trans-Neon Orange','Trans-Orange','Trans-Yellow','Trans-Neon Green','Trans-Bright Green','Trans-Green','Trans-Dark Blue','Trans-Medium Blue','Trans-Light Blue','Trans-Purple','Trans-Dark Pink','Pearl Light Gray','Flat Silver','Pearl Dark Gray','Pearl Gold']

# color_removed = ['583927'] #Brown

# def hex_to_rgb(value):
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# def get_available_colors(arg):

#     color_rgb = []

#     for color_code in color_codes:
#         color_rgb.append(hex_to_rgb(color_code))

#     color2name_dict = {}
#     for i in range(len(color_rgb)):
       
#         color2name_dict[color_rgb[i]] = color_names[i]

#     if arg == 'list':
#         return(color_rgb)
      
#     elif arg == 'dict':
#         return color2name_dict




