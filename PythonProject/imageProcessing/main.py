# rennormons les image dans notre dossier courant
import os , pathlib
liste_file = os.listdir()

for i , j in zip(liste_file,range(len(liste_file))) :
    if not pathlib.Path(i).suffix == ".py" :
        pathlib.Path(i).rename( f"image{j}"+".jpg")




# remove background
# Importing Required Modules
from rembg import remove
from PIL import Image

im = Image.open("images.jpg") ; im.save("log.png")
input_path = "log.png"
output_path = "logo.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)



# cree ouvrir une image

from PIL import Image
im = Image.new("RGB" , (1920 , 1080) , (25,55,5))
im.show()

# pour ouvrir une image
im = Image.open("image1.jpg")
im.show()

# sauvegarder une image
im = Image.open("image2.jpg")
im.save("image2_save.jpg")

# convertion des image
im = Image.open("image4.jpg")
im.convert("RGB").save("image5_save.jpg")

# Convertion d'image en changant l ' arriere plan du im rmbg
im = Image.open("image7_rmbg.png")
im_png = Image.new("RGB" , im.size , (255,0,0))
im_png.paste(im , im)
im_png.show()
im.split()[3].show() # afficher la couche alpha

# retourner une image
im = Image.open("image7.jpg")
im.rotate(95 , expand=True , fillcolor="black").show()




# Filtre sur image
from PIL import ImageEnhance 
from outils import compare

im = Image.open("Image4.jpg")
im_filtre  = ImageEnhance.Color(im).enhance(0)
im_filtre.show()
im_filtre.split()[0].show()

image=  []
for i in range(10) :
    im_filtre = ImageEnhance.Color(im).enhance(i/2)
    image.append(im_filtre)

compare(*image)



# Manipulation sur image avec plus de controle
from PIL import Image 
from outils import compare 

im = Image.open("images.jpg")
im1 = im.convert("L")
im1.show()




# creation de filtre instagram 
from PIL import Image

image = Image.open("images.jpg")
gradient = Image.open("images7.jpg")
gradient = gradient.resize(image.size)

Image.blend(image,gradient , 0.5).show()



## creation d;un effet sepia 
from PIL import Image 
from PIL import ImageOps
from PIL import ImageEnhance

im = Image.open("images8.jpg").convert("L")
im1 = ImageOps.colorize(im , (255, 0 , 0) , (0, 255,0))
im1 = ImageEnhance.Contrast(im).enhance(4)

im1.show()
im1.split()[0].show()



## optimisation d;
from PIL import Image

im  = Image.open('images7.jpg')
facteur = 2
t = im.size
t_reduit = (int(t[0]/facteur) , int(t[1]/facteur))
im.resize(t_reduit).show()



#vignette poour les image
from PIL import Image

im = Image.open("images8.jpg")
im.thumbnail(im.size)
im.show()


# comment identifier une image
from PIL import Image

logo = Image.open("logo.png").convert("RGBA")
im = Image.open("image3.jpg").convert("RGBA")

def copyright(images , position="hg" ,marge=20) :
    largeur,  hauteur  = image.size 
    log_lar , log_haut = logo.size 
    coord = {
        "hd":(0+marge , 0+marge) ,
        "bg":(0+marge , hauteur-marge-log_haut),
        "hd":(largeur-marge-log_lar , hauteur -marge-log_haut),
        "bd":(largeur-marge-log_lar , hauteur - marge - log_haut)
    }
    im.paste(logo , coord.get("hg") , logo)
    im.show()

copyright(im , "hd" , 20)
im.show()
im.save("image4_tager.png")



# comment ajouter un watermarke
from PIL import Image
import PIL.JpegImagePlugin
from PIL import ImageDraw
from PIL import ImageFont
import tqdm
from time import sleep

im = Image.open("image0.jpg")
font_path  = "National Cartoon.ttf"

def copyright(image:PIL.JpegImagePlugin.JpegImageFile , texte , opacity =1.0 , rotation =30) :
    image = image.convert("RGBA")
    texte_image = Image.new("RGBA" , image.size, (255,255,255,0))

    fontsize = 1
    font = ImageFont.truetype(font_path,fontsize)
    while font.getbbox(texte)[0] < image.size[0] :
        fontsize += 1
        font = ImageFont.truetype(font_path , fontsize)
        
    text_haut = font.getbbox(texte)[1]
    pos = (0, image.size[1] / 2) - text_haut /2 

    d = ImageDraw.Draw(texte_image)
    d.text(pos , "texte" , fill=(255,255,255,round(opacity*255)) , font=font)
    
    texte_image = texte_image.rotate(rotation)
    combined = Image.alpha_composite(image , texte_image)

    return Image.alpha_composite(image , texte_image)


im_copyright = copyright(im , "ken" , 0.3)
im_copyright.show()





#Recuperation des metadonnes
from PIL import Image
import piexif
from pprint import pprint

im = Image.open("dami.jpg")
#exif_dict = piexif.load(im.info["exif"])
exif = piexif.load("dami.jpg")
pprint(exif)



## TRaiter les images en fonctino des donnes gps
from PIL import Image
import piexif
import requests

im = Image.open("gps/image0.jpg")
pprint(piexif.load("gps/image1.jpg"))
liste = requests.get(f"http://stephenebucket.s3.amazonaws.com/classemates.txt")

