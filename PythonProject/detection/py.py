name = str(input('ENtrer le nom de votre fichier'))
texte = str(input('Entrer votre texte ici '))


with open (file=('exemple.txt'),mode='a' ) as file :
    file.write('kes\n')
    file.write('def')
    file.write('frf')
    file.write('fre')
    file.write('ftr')
    file.write('frg')
    file.close() 

print('le contenu a bien ete enregistrer')

