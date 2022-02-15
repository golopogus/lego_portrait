# Importing Image class from PIL module
from PIL import Image

def crop_image(img_name):
# Opens a image in RGB mode
    img_path = "C:/Users/dolan/Desktop/lego_portrait/uncropped_images/" + img_name + ".jpg"
    im = Image.open(img_path)
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    crop_dist= (width - height)/2 # square
    #crop_dist = (width - (.5 * height))/2 # double height than width


    
    # Setting the points for cropped image
    left = crop_dist
    top = 0
    right = width - crop_dist
    bottom = height 
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    save_path = "C:/Users/dolan/Desktop/lego_portrait/cropped_images/cropped_" + img_name + ".png"

    im1.save(save_path)

    return 


 
# Shows the image in image viewer
#im1.show()