class markProcessing:
    def __init__(self, **kwargs):
        import os
        
    def etape1(self, img):
        import cv2
        import numpy as np
        
        ##########
        src_img= cv2.imread(img, 1)
        #imshow(src_img)

        # step 1
        copy = src_img.copy()
        height = src_img.shape[0]
        width = src_img.shape[1]

        # step 2
        src_img = cv2.resize(copy, dsize =(1320, int(1320*height/width)), interpolation = cv2.INTER_AREA)

        # step 3
        height = src_img.shape[0]
        width = src_img.shape[1]

        # step 4
        grey_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
        #imshow(grey_img)

        # step 5 : Applying Adaptive Threshold with kernel :- 21 X 21
        bin_img = cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
        #bin_img1 = bin_img.copy()
        #bin_img2 = bin_img.copy()

        #imshow(bin_img,cmap='gray')

        # step 6 : Lines detection
        count_x = np.zeros(shape= (height))
        #count_x.shape

        count_x = np.zeros(shape= (height))
        for y in range(height):
            for x in range(width):
                if bin_img[y][x] == 255 :
                    count_x[y] = count_x[y]+1

        t = np.arange(0,height, 1)
        #plt.plot(t, count_x[t])

        return [count_x, bin_img]
    
    def etape2(self, count_x, seuil):
        indices = []

        for t in range(0,len(count_x)-1):
            if count_x[t] > seuil:
                indices.append(t)

        # print(indices)

        indices2 = []
        for i,j in zip(range(0, len(indices)-2), range(1, len(indices)-1)):
            if indices[j]-indices[i]>10:
                indices2.append(indices[i])
                #indices2.append(indices[j])
        indices2.append(indices[len(indices)-1])

        # indices2

        return indices2

    def extractLines(self, indices2):
        # extraction fragments
        extracted = []

        for i in range(0, len(indices2)-1):
            a = bin_img[indices2[i]:indices2[i+1]]
            extracted.append(a)

        return(extracted)
    
    def extractLinesv2(self, extract0,indices2):
        # extraction fragments
        extracted = []

        for i in range(0, len(indices2)-1):
            #a = extract0[indices2[i]:indices2[i+1], :]
            # ici j'ajoute et retranche quelques pixels comme marge afin que le trait n'apparaisse pas
            a = extract0[indices2[i]+6:indices2[i+1]-5, :]
            extracted.append(a)

        return(extracted)
    
    def etape3(self, img):
        import cv2
        import numpy as np
        
        src_img= cv2.imread(img, 1)
        #imshow(src_img)

        # step 1
        copy = src_img.copy()
        height = src_img.shape[0]
        width = src_img.shape[1]

        # step 2
        src_img = cv2.resize(copy, dsize =(1320, int(1320*height/width)), interpolation = cv2.INTER_AREA)

        # step 3
        height = src_img.shape[0]
        width = src_img.shape[1]

        # step 4
        grey_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
        #imshow(grey_img)

        # step 5 : Applying Adaptive Threshold with kernel :- 21 X 21
        bin_img = cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
        #bin_img1 = bin_img.copy()
        #bin_img2 = bin_img.copy()

        #imshow(bin_img,cmap='gray')

        # step 6 : Lines detection
        count_y = np.zeros(shape= (width))
        #count_y.shape

        count_y = np.zeros(shape= (width))
        for x in range(width):
            for y in range(height):
                if bin_img[y][x] == 255 :
                    count_y[x] = count_y[x]+1

        t = np.arange(0,width, 1)
        #plt.plot(t, count_y[t])

        return [count_y, bin_img]
    
    def etape4(self, seuil=500):
        indices_y = []

        for t in range(0,len(count_y)-1):
            if count_y[t] > seuil:
                indices_y.append(t)


        indices2_y = []
        for i,j in zip(range(0, len(indices_y)-2), range(1, len(indices_y)-1)):
            if indices_y[j]-indices_y[i]>10:
                indices2_y.append(indices_y[i])
                #indices2.append(indices[j])
        indices2_y.append(indices_y[len(indices_y)-1])

        # indices2_y

        return indices2_y
    
    def etape41(self, seuil=500):
        indices_y = []

        new_count_y = np.array(count_y)

        # on suppose 4 pices

        # elimination pic 1

        maxi = np.max(new_count_y)

        indexi = np.where(new_count_y == maxi)[0][0]

        indices_y.append(indexi[0][0])

        new_count_y = np.delete(new_count_y, indexi)


        indices2_y = indices_y


        return indices2_y
    
    def etape42(self, expectedcol=4):
        indices2_y = []

        new_count_y = np.array(count_y)

        # on suppose 4 pics

        # elimination pics

        for i in range(1, expectedcol+1):
            # on identifie la valeur max du tableau numpy
            maxi = np.max(new_count_y)

            # on identifie l'indice correspondant à ce max
            indexi = np.where(new_count_y == maxi)[0][0]

            # on insère cet indice dans la liste des indices
            indices2_y.append(indexi)

            # on supprime le max précédemment identifié du tableau numpy
            new_count_y = np.delete(new_count_y, indexi)

        return indices2_y
    
    def extractCol(self, indices2_y):
        # extraction fragments
        extracted = []

        for i in range(0, len(indices2_y)-1):
            #a = bin_img[:, indices2_y[i]:indices2_y[i+1]]
            # ici j'ajoute et retranche quelques pixels comme marge afin que le trait n'apparaisse pas
            a = bin_img[:, indices2_y[i]+6:indices2_y[i+1]-5]
            extracted.append(a)

        #for i in range(0, len(indices2_y)-1):
            #print(str(indices2_y[i]) + ' - ' + str(indices2_y[i+1]))
            #a = bin_img[:, indices2_y[i]-35:indices2_y[i+1]]
            #extracted.append(a)

        return(extracted)
    
    def etape422(self, count_y, expectedcol=4):
        
        # - cest une fonction de filtrage 
        # - expectedcol est le nbre de fragments colonnes qu'on veut extraire réellement
        # - indices2_y contiendra les indices rigoureusement retenu après le filtrage ie les indices correspondant aux fragments à extraire
        # - indices2_y sera passé en argument à la fonction extractCol
        
        import numpy as np
        
        ##########

        indices2_y = []

        new_count_y = count_y.copy()

        # on suppose 4 pics

        # elimination pics

        for i in range(1, expectedcol+1):
            # on identifie la valeur max du tableau numpy
            maxi = np.max(new_count_y)

            # on identifie l'indice correspondant à ce max
            indexi = np.where(new_count_y == maxi)[0][0]

            # on insère cet indice dans la liste des indices
            indices2_y.append(indexi)

            # on remplace le max précédemment identifié par 0 pour qu'il ne soit pas identifié 2 fois et pour maintenir la structure du tableau
            new_count_y[indexi] = 0

        return indices2_y
    
    def good_tuples(self, indices_initiaux):
        
        # creation d'une fonction qui crée toutes les permutations de tuples (2 éléments) possiles et renvoie celles ayant environ le seuil précédent 
    
        differences_obtenues = []
        good_indices_col = []

        for a in range(0, len(indices_initiaux)-2):
            for i in range(a+1, len(indices_initiaux)-1):
                differences_obtenues.append(indices_initiaux[i] - indices_initiaux[a])

                # on recherche ici les fragments dont la largeur mesure environ 181
                # donc appartenant à l'intervalle [178,195]

                if indices_initiaux[i] - indices_initiaux[a] > 178 and indices_initiaux[i] - indices_initiaux[a] < 195:
                    good_indices_col.append((indices_initiaux[a],indices_initiaux[i]))

        return good_indices_col,differences_obtenues
    
    def extractColv2(self, good_indices_col, bin_img):
        # Fonction pour extraire tous les fragments de colonnes de Rang A
        
        # extraction fragments
        extracted = []

        for i in range(0, len(good_indices_col)):
            a = bin_img[:, good_indices_col[i][0]:good_indices_col[i][1]]
            extracted.append(a)

        return(extracted)
    
    def cropcol(self, img):
        import numpy as np
        
        #################
        
        # Fonction pour identifier les indices colonnes pour le rognage
        
        width = img.shape[1]
        height = img.shape[0]

        count_y = np.zeros(shape= (width))
        for x in range(width):
            for y in range(height):
                if img[y][x] == 255 :
                    count_y[x] = count_y[x]+1

        t = np.arange(0,width, 1)
        #plt.plot(t, count_y[t])
        return [count_y]
    
    def etape422a(self, count, expectedcol=4):
        
        # Fonction pour Filtrer les indices colonnes précédemment obtenus et renvoyer les indices optimaux pour le rognage

        # - cest une fonction de filtrage 
        # - expectedcol est le nbre de fragments colonnes qu'on veut extraire réellement
        # - indices2_y contiendra les indices rigoureusement retenu après le filtrage ie les indices correspondant aux fragments à extraire
        # - indices2_y sera passé en argument à la fonction extractCol
        
        import numpy as np
        
        ####################

        indices2_y = []

        new_count_y = count.copy()

        # on suppose 4 pics

        # elimination pics

        for i in range(1, expectedcol+1):
            # on identifie la valeur max du tableau numpy
            maxi = np.max(new_count_y)

            # on identifie l'indice correspondant à ce max
            indexi = np.where(new_count_y == maxi)[0][0]

            # on insère cet indice dans la liste des indices
            indices2_y.append(indexi)

            # on remplace le max précédemment identifié par 0 pour qu'il ne soit pas identifié 2 fois et pour maintenir la structure du tableau
            new_count_y[indexi] = 0

        return indices2_y
    
    def extractColv3(self, img, indices):
        # Fonction d'extraction des frag Rang A1 après rognage
        
        # extraction fragments
        extracted = []

        for i in range(0, len(indices)-1):
            a = img[:, indices[i]:indices[i+1]]

            # on selectionne le fragment ayant une largeur > 10 pixels 
            if a.shape[1] > 10:
                extracted.append(a)

        return(extracted)
    
    def crop(self, image):
        # Define crop function
        import numpy as np
        
        #####################
        
        height = image.shape[0]
        width = image.shape[1]

        # comptage nbre de pixels differents de 0 sur chaque ligne
        count_x = np.zeros(shape= (image.shape[0]))

        for y in range(height):
            for x in range(width):
                if image[y][x] > 0 :
                    count_x[y] = count_x[y]+1

        # 1er indice hauteur

        h1 = []

        for t in range(0,len(count_x)-1):
            if count_x[t] > 0:
                h1.append(t)

        h1 = h1[0]

        # 2eme indice hauteur

        h2 = []

        for t in range(len(count_x)-1, 0, -1):
            if count_x[t] > 0:
                h2.append(t)

        h2 = h2[0]

        # comptage nbre de pixels differents de 0 sur chaque colonne
        count_y = np.zeros(shape= 64)

        for x in range(width):
            for y in range(height):
                if image[y][x] > 0 :
                    count_y[x] = count_y[x]+1

        # 1er indice ligne

        x1 = []

        for t in range(0,len(count_y)-1):
            if count_y[t] > 0:
                x1.append(t)

        x1 = x1[0]

        # 2e indice ligne

        x2 = []

        for t in range(len(count_y)-1, 0, -1):
            if count_y[t] > 0:
                x2.append(t)

        x2 = x2[0]

        return image[h1:h2,x1:x2]
    
    def extractColv32(self, img, indices):
        # Fonction d'extraction des frag Rang A2 après rognage

        # extraction fragments
        extracted = []

        a = img[:, indices[0]:]

        extracted.append(a)

        return(extracted)