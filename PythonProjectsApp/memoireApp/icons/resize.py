from PIL import Image


ma = Image.open("icons/ma2.jpg")
s = ma.size
macd = Image.open("icons/macd2.png")

macd = macd.resize(s)
macd.save("icons/macd.png")

