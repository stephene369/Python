from stegano import lsb

# Ouverture de l'image à cacher le texte
image = "image.jpg"

# Texte à cacher
text = "Ceci est un texte caché dans l'image \n"*10

# Cacher le texte dans l'image
secret_image = lsb.hide(image, text)

# Sauvegarder l'image secrète
secret_image.save("secret_image.png")

# Extraire le texte de l'image
extracted_text = lsb.reveal("secret_image.png")

# Afficher le texte extrait
print(extracted_text)