# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open('C:/Users/dolan/Desktop/lego_portrait/uncropped_images/batman2.jpg')
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
crop_dist= (width - height)/2
#crop_dist= (height - width)/2
 
# Setting the points for cropped image
left = crop_dist
top = 0
right = width - crop_dist
bottom = height #- crop_dist
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

im1.save('C:/Users/dolan/Desktop/lego_portrait/cropped_images/cropped_batman2.png')

 
# Shows the image in image viewer
#im1.show()