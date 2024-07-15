from PIL import Image

def compare(*args) :
    larg,haut = zip(*(i.size for i in args))

    larg_tt = sum(larg)
    hauteur_max = max(haut)

    image_composite = Image.new("RGB" , (larg_tt , hauteur_max))

    offset_x = 0 
    for im in args :
        image_composite.paste(im , (offset_x , 0))
        offset_x+=im.size[0]

    image_composite.show()

im1 = Image.open("image1.jpg")
im2 = Image.open("Image3.jpg")
im3 = Image.open("Image5.jpg")
compare(im1, im2 , im3)