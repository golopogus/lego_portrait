import requests
from bs4 import BeautifulSoup
import json


URL = "http://my.crazyartzone.com/dmc.asp"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table_row = soup.find_all("tr")[1:]

color_dict = {}
for row in table_row:
    values = row.find_all("td", class_="ntd")
    color_code = values[1].string
    red = values[3].string
    green = values[4].string
    blue = values[5].string

    rgb = (int(red),int(green),int(blue))
    rgb = json.dumps(rgb)

    color_dict[rgb] = color_code

with open("color_dict.json", "w") as outfile:
    json.dump(color_dict, outfile)
    



