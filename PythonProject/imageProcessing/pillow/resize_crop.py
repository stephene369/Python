from PIL import Image

itachi = Image.open("itachie.png")
itachi2 = Image.open("name.png")


new = Image.new("RGBA" , itachi.size)
new = Image.blend(itachi , itachi2 , 0.1)
new.show()


H = 1209
W = 720
left = (itachi.width - W)//2
top = (itachi.height - H)//2
right = left+W
bottom = top+H

it = itachi.crop((left,top,right,bottom))
it.show()

## redimensionner et completer
ita = Image.new("RGB",(W,H) )
ita.paste(itachi, ((W - itachi.width) // 2, (H - itachi.height) // 2))
ita.show()


