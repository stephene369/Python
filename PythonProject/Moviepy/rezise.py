
# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open("image1.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

 
# Setting the points for cropped image
"""left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (880, 1080)"""

im = im.resize((880,1080))
# Shows the image in image viewer
im.show()


## Others way

for i in range(1,4) :
    image = f"image{i}.png"
    im  = Image.open(image)
    im = im.resize((880 ,1080 ))
    im.save(image)

"""    im.show()"""
    