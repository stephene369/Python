from pyautogui import size
from PIL import Image, ImageDraw,ImageFilter

width = size().width # x
height = size().height # y

image = Image.new("RGBA",(width,height) , 'white')
image_center = Image.open("image.png")

h = image_center.height
w = image_center.width 

p = (height-h)/height
h_ = int((height*p)+h)
w_ = w+int(height*p)//2

image_center = image_center.resize((w_,h_))

## pixel orignial 
for y in range(image_center.height) :
    pix  = image_center.getpixel((0,y))
    a = int((y/image_center.height)*255)
    pix+=(255,)
    for x_ in range(0,width//2) :
        image.putpixel((x_,y),pix)

for y in range(image_center.height) :
    pix  = image_center.getpixel((image_center.width-1,y))
    a = int((y/image_center.height)*255)
    pix+=(255,)
    for x_ in range(width//2,width) :
        image.putpixel((x_,y),pix)
image.show()

for y in range(image_center.height) :
    pix  = image_center.getpixel((0,y))
    a = int((y/image_center.height)*255)
    #pix+=(255,)
    for x_ in range(0,width) :
        image.putpixel((x_,y),pix)


## collage de l'image
image2 = image.filter(ImageFilter.GaussianBlur(10))
image2.paste(image_center ,  (image.width-image_center.width, 0))
image2.show()