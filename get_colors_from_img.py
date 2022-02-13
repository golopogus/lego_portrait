from PIL import Image

def get_colors(x,y):
    img = Image.open('C:/Users/dolan/Desktop/lego_portrait/pixelated_images/pixelated_batman2.png')

    pix = img.load()

    color = pix[x,y]

    return color
