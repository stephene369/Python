from pyautogui import size
from PIL import Image, ImageDraw,ImageFilter


width = size().width # x
height = size().height # y



im1 = Image.open("image2.jfif")
h = im1.height
w = im1.width 
p = (height-h)/height
h_ = int((height*p)+h)
w_ = w+int(height*p)//2
im1 = im1.resize((w_,h_))



im2 = Image.open("image1.jfif")
h = im2.height
w = im2.width 
p = (height-h)/height
h_ = int((height*p)+h)
w_ = w+int(height*p)//2
im2 = im2.resize((w_,h_))



image = Image.new("RGBA",(width,height) , im1.getpixel((0,0)) )
image_center = im1



for y in range(image_center.height) :
    pix  = image_center.getpixel((image_center.width-1,y))
    a = int((y/image_center.height)*255)
    #pix+=(255,)
    for x_ in range(0,width//2) :
        image.putpixel((x_,y),pix)

image_center = im2
for y in range(image_center.height) :
    pix  = image_center.getpixel((0,y))
    a = int((y/image_center.height)*255)
    #pix+=(255,)
    for x_ in range(width//2,width) :
        image.putpixel((x_,y),pix)

image.show()

image2 = image.filter(ImageFilter.GaussianBlur(8))
image2.paste(im1,(0,0))
image2.paste(im2,(image.width-im2.width,0))
image2.show()
image2.save("back4.png")