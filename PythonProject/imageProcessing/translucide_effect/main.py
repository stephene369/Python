from PIL import Image , ImageFilter
from pyautogui import screenshot

size = screenshot().size
im = Image.open("itachi1.png")
im = Image.eval(im , lambda x: x/1.5)
im = im.filter(ImageFilter.GaussianBlur(radius=5) )
im = im.resize(size)
im.save("ITACHY.png")

