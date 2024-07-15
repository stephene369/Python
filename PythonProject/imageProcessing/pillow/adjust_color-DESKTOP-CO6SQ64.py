from PIL import Image , ImageEnhance
from pathlib import Path
from pyautogui import screenshot

image_ = 'jad.jpg'
im = Image.open(image_)


bmp_ = f'{Path(image_).stem}.bmp'
im.save(bmp_)


im_ = Image.open(bmp_)

for x in range(im_.size[0]):
    
    for y in range(im_.size[1]):
        r, g, b = im_.getpixel((x, y))
        im_.putpixel((x, y), (int(r/2), 
                               int(g/2), 
                               int(b)))
im_.show()

im_h_ = ImageEnhance.Color(im)


im.show()
im_.show()
im_h_.enhance(2).show()
#capture = screenshot()
#capture.save("capture.jpg")

