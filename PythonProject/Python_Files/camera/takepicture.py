liste='6.47 7.02 7.15 7.22 7.44 6.99 7.47 7.61 7.32 7.22 7.52 6.92 7.28 6.69 7.24 7.19 6.97 7.52 6.22 7.13 7.32 7.67 7.24 6.21'
liste=liste.split(' ') 
liste = [float(i) for i in liste ]
liste

moyen = sum(liste) / len(liste)
len(liste)
sqn = (len(liste))**0.5
div=(moyen-7.3)/0.38
sqn*div