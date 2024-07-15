import os 
from pathlib import Path
from PIL import Image



liste_file = os.listdir()

for file in liste_file :
    im = Image.open(file)
    im = im.resize((300,168))
    im.save("m_"+file)
    im.close()

