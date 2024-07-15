from modules.File import *

def process(list_image):
	# import librairies
	print('\n-----------import librairies------------')
	import dill
	import cv2 
	import numpy as np
	import pandas as pd

	# Faire appel à la variale contenant la liste des noms par sheet

	var = choiceListe()
	names = var.names

	print('\n-----------Liste des noms------------')
	for t in names:
		print(t)

	#

	tabNotesAll = []

	image_number = 1

	for image, iname, iid in zip(list_image, names, list(range(1,len(names)+1))):

		print('\n')
		print(iname[iid])
		
		print("---------------------", "Image", str(image_number), "processing","----------------------")

		# 1.1
		print("---------------1.1------------------")
		
		with open('tools/processing', 'rb') as file:
			processing = dill.load(file)

		# 1.2
		print("---------------1.2------------------")

		img = image
		job = processing.etape3(img)
		count_y = job[0]
		bin_img = job[1]

		# 1.3
		print("---------------1.3------------------")

		indices2_y = processing.etape422(count_y, expectedcol=6)
		indices2_y.sort()
		indices2_y

		# 1.4
		print("---------------1.4------------------")

		good_indices_col, differences_obtenues = processing.good_tuples(indices2_y)
		good_indices_col

		# 1.5
		print("---------------1.5------------------")

		extracted_y = processing.extractColv2(good_indices_col, bin_img)
		len(extracted_y)

		# 1.6
		print("---------------1.6------------------")

		rang_a1 = extracted_y[0][:,40:110]

		#### 1.7
		print("---------------1.7------------------")

		job = processing.etape1(img)
		count_x = job[0]
		bin_img = job[1]
		
		# 1.8
		print("---------------1.8------------------")

		indices2 = processing.etape2(count_x, seuil=400)

		# 1.9
		print("---------------1.9------------------")

		extracted_x = processing.extractLinesv2(rang_a1,indices2)
		len(extracted_x)

		# 1.10
		print("---------------1.10------------------")

		extracted_x2 = []

		for i in range(1, len(extracted_x),2):
		    a = extracted_x[i]
		    extracted_x2.append(a)
	    
		# inserton du dernier fragment
		a = extracted_x[len(extracted_x)-1]
		extracted_x2.append(a)
		len(extracted_x2)

		# 1.11
		print("---------------1.11------------------")

		extracted_x2a = []

		for i in extracted_x2:
		    # obtention de tous les indices colonne
		    count_ya = processing.cropcol(i)[0]
		    
		    # Filtrer les indices colonnes précédemment obtenus et renvoyer les optimaux
		    indices = processing.etape422a(count_ya, expectedcol=6)
		    
		    # extraction après rognage
		    ex = processing.extractColv3(i, indices)
		    
		    # enregistrement
		    extracted_x2a.append(ex[0])
	    
		len(extracted_x2a)

		# 1.12
		print("---------------1.12------------------")

		for i in range(0, len(extracted_x2a)):
			extracted_x2a[i] = processing.crop(extracted_x2a[i])

	    # 1.13
	    # 1.13.1
		print("---------------1.13.1------------------")

		cases_a1 = []

		for i in extracted_x2a:
		    couple_cases = []
		    
		    case1 = i[:22, :]
		    case2 = i[22:, :]
		    
		    couple_cases.append(case1)
		    couple_cases.append(case2)
		    
		    cases_a1.append(couple_cases)

		# 1.13.2
		print("---------------1.13.2------------------")

		sum_pixels_case = []

		for i in range(0, len(cases_a1)):
		    
		    # sous liste pour stocker les sommes des deux cases par étudiant
		    s_list = []
		    
		    # on calcule la somme des pixels cntenus dans chaque case
		    s1 = np.sum(cases_a1[i][0])
		    s_list.append(s1)
		    
		    s2 = np.sum(cases_a1[i][1])
		    s_list.append(s2)
		    
		    # on enregistre la liste précédente dans une liste globale
		    sum_pixels_case.append(s_list)

		# 1.13.3
		print("---------------1.13.3------------------")

		digits_gauche = []

		for i in sum_pixels_case:
		    if i[0] > i[1]:
		        digit = 0
		    else:
		        digit = 1
		    
		    digits_gauche.append(digit)
		    
		digits_gauche

		# 2
		# 2.1
		print("---------------2.1------------------")

		rang_a2 = extracted_y[0][:,130:]

		# 2.2
		print("---------------2.2------------------")

		extracted_xx = processing.extractLinesv2(rang_a2,indices2)
		len(extracted_xx)

		# 2.3
		print("---------------2.3------------------")

		extracted_xx2 = []

		for i in range(1, len(extracted_xx),2):
		    a = extracted_xx[i]
		    extracted_xx2.append(a)
		    
		# inserton du dernier fragment
		a = extracted_xx[len(extracted_xx)-1]
		extracted_xx2.append(a)
		len(extracted_xx2)

		# 2.4
		print("---------------2.4------------------")

		extracted_xx2a = []

		for i in extracted_xx2:
		    # obtention de tous les indices colonne
		    count_ya = processing.cropcol(i)[0]
		    
		    # Filtrer les indices colonnes précédemment obtenus et renvoyer les optimaux
		    indices = processing.etape422a(count_ya, expectedcol=1)
		    
		    # extraction après rognage
		    ex = processing.extractColv32(i, indices)
		    
		    # enregistrement
		    extracted_xx2a.append(ex[0])
		    
		len(extracted_xx2a)

		# 2.5
		print("---------------2.5------------------")

		for i in range(0, len(extracted_xx2a)):
			extracted_xx2a[i] = processing.crop(extracted_xx2a[i])

	    # 2.6
	    # 2.6.1
		print("---------------2.6.1------------------")

		cases_a2 = []

		for i in extracted_xx2a:
		    
		    hautdeb = 0
		    hautfin = 22
		    intervalh = 22
		    
		    couple_cases = []
		    
		    for j in range(1,11):
		    
		        case_i = i[hautdeb:hautfin, :]

		        hautdeb = hautfin +5
		        hautfin = hautdeb + intervalh

		        couple_cases.append(case_i)

		    cases_a2.append(couple_cases)
		    
		len(cases_a2)

		# 2.6.2
		print("---------------2.6.2------------------")

		sum_pixels_case_a2 = []

		for i in range(0, len(cases_a2)):
		    
		    # sous liste pour stocker les sommes des 10 cases par étudiant
		    s_list = []
		    
		    # on calcule la somme des pixels cntenus dans chaque case
		    
		    for u in range(0, len(cases_a2[i])):
		        s = np.sum(cases_a2[i][u])
		        s_list.append(s)
		    
		    # on enregistre la liste précédente dans une liste globale
		    sum_pixels_case_a2.append(s_list)
		    
		sum_pixels_case_a2 = np.array(sum_pixels_case_a2)

		# 2.6.3
		print("---------------2.6.3------------------")

		digits_droit = []

		for i in sum_pixels_case_a2:
		    maxi = np.max(i)
		    indexi = np.where(i == maxi)[0][0]
		    digits_droit.append(indexi)
		    
		digits_droit

		# 2.6.4
		print("---------------2.6.4------------------")

		liste_etudiants = iname[iid]

		tabNotes = []

		for i,j,k in zip(liste_etudiants, digits_gauche, digits_droit):
		    f = {}
		    f['Noms'] = i
		    f['Note 1'] = str(j) + str(k)
		    #f['Note 1'] = int(f['Note 1'])
		    tabNotes.append(f)

		    
		# exportation en csv
		import pandas as pd

		tabNotes = pd.DataFrame(tabNotes)

		tabNotesAll.append(tabNotes)

		# go to next image
		image_number += 1

	#########################################
	# on sort de la boucle

	# assembler les donnees de chaque page
	j = 0

	tab = pd.concat([tabNotesAll[j], tabNotesAll[j+1]])
	j = 1

	while j < len(tabNotesAll)-1:
		tab = pd.concat([tab, tabNotesAll[j+1]])
		j += 1

	export to csv
	tab.to_csv('tab.csv', index=False)

	print('\n')
	print("--------------------END-----------------------")