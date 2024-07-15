from PIL import Image , ImageEnhance
from pathlib import Path
import pathlib

file_ = list(Path('amvimage/msg').glob("*"))
H = int( 1200*1 )
W = int (720*1)
#left = (itachi.width - W)//2
#top = (itachi.height - H)//2
#right = left+W
#bottom = top+H


for file in file_ :
    img = Image.open(file)
    image = Image.new("RGB",(W,H))
    image.paste(img , ((W - img.width) // 2, (H - img.height) // 2) )
    image = ImageEnhance.Color(image).enhance(2)
    image.save(f"imageChange/{file.stem + file.suffix}")
