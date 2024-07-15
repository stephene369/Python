from audioSegment import Segment 
from recongnizer import Reconnaisseur , Path

folder = "Dax"
filename = "dax.mp3"

s = Segment(folder=folder,filename=filename,sec=10)
s.segment()

r = Reconnaisseur(folder=folder )
TEXTE = r.reconnaisseur()

with open("texte.txt",'w') as f :
    f.write(str(TEXTE))

