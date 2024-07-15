from PySide6.QtWidgets import QDialog , QMessageBox , QLabel , QPushButton , QProgressBar
from pathlib import Path
import os
from time import sleep
IMAGE_SUFFIX = ['.png' , '.jpeg','.jpg','.gif','.bmp','.tiff','.svg','.ico','.webp','.raw',
                '.exif','.psd','.ai','.eps','.xcf','.indd']


class Verification :
    def __init__(self , pop:QMessageBox , 
                 lab:QLabel,start:QPushButton , 
                file_path:list,status:QLabel,chargeList:QPushButton,
                progress:QProgressBar) -> None:
        
        self.status = status
        self.lab = lab
        self.popUp = pop
        self.label = lab
        self.start = start
        self.file_path = file_path
        self.chargeListe = chargeList
        self.progress = progress
        self.prog = 0

    def Verify(self) :
        self.progress.setHidden(False)
        # condition pour que le dossier ne contienne que des images
        cond1 = 0

        # recuparation de la liste des fichiers du dossiers
        self.list_file = os.listdir( Path(self.file_path[0]).parent )
        print(self.list_file)
        
        # Liste des fichiers contenu dans le dossiers sans l'extension 
        self.liste_file2 = [ Path(name).stem for name in self.list_file  ]

        # recuperation de l'extension des fichiers images
        self.extension = Path(self.list_file[0]).suffix
        
        # Verifier que tous les fichiers sont des images
        liste_extensions = []
        Message = []
        for file in self.list_file :
            
            extension = Path(file).suffix
            #liste_extensions.append(extension)
            if extension not in IMAGE_SUFFIX:
                cond1 += 1
                print("Le dossier ne doit contenir que des images !")
                # POP up a implementer 

                Message.append("type")
                break
            
            self.prog+=1
            self.progress.setValue((self.prog/len(self.list_file))*100) ; sleep(0.07)
            self.label.setText(file)
        # on verifie si les fichiers sont bien renommés avec des caractères chiffres
        # (uniquement si tous les fichiers sont des images) 

        if cond1 == 0:
            # on essaie de convertir les noms de fichier en entiers
            # (si la conversion marche, on continue le programme)
            try:
                for j in range(0, len(self.liste_file2)):
                    self.liste_file2[j] = int(self.liste_file2[j])

                # on suppose que la conversion a marché et donc le programme continue

                # on recupere le nombre de fichiers presents dans le dossier
                self.lenList_File2 = len(self.liste_file2)

                # On s'assure que le nom de chaque fichier excepté l'extension est égale a 1 ou 2 ou 3 ou ...

                # on doit ordonner les noms de fichiers de manière croissante 
                # car l'ordre dans la liste ici peut différer à tort de l'ordre dans le dossier

                self.liste_file2.sort()
                print('Liste ordonnée :', self.liste_file2)
                
                # initialiser un compteur de fichiers mal renommés
                self.fichier_mal_renommer = 0

                for i in range(0,self.lenList_File2) :
                    if self.liste_file2[i] != i+1 :
                        self.fichier_mal_renommer+=1

                # si le compteur est > 0 alors il y a des fichiers mal renommés
                if self.fichier_mal_renommer > 0 :
                    print("Les fichiers n'ont pas été renommés dans l'ordre")
                    # Pop up a implement
                    Message.append("name")

                else :
                    print("Données vérifiées")
                    # Pop up à implémenter
                    Message.append("data")

                    # constituer la liste des chemins d'accès aux images ordonnées
                    chemin_dossier = Path(self.file_path[0]).parent

                    # Reinitialiser pour prevenir les doublons
                    self.liste_file3 = []

                    for i in self.liste_file2:
                        self.liste_file3.append(os.path.join(chemin_dossier, str(i)+self.extension))
                        print( "les ex",i , self.extension)

                    # afficher nbre de fichiers à traiter
                    print('\n')
                    print('Nombre de fichiers à traiter', len(self.liste_file3))

            except:
                # la conversion des noms de fichier en entiers n'a pas marché 
                print("Les fichiers n'ont pas été renommés avec des caractères numériques")
                # popup
                Message.append("ordre")
                
       

        set(Message)
        for message in Message:
            if message == 'name' :
                self.popUp.setText("Fichier mal renommer")
                self.popUp.setIcon(QMessageBox.Icon.Information)
                self.popUp.setStandardButtons(QMessageBox.Ok)
                self.popUp.show()
                btn = self.popUp.button(QMessageBox.Ok)
                btn.clicked.connect(self.popUp.accept)
                self.progress.setValue(0)
                self.progress.setHidden(False)
                self.label.setText("Les fichers doivent etre renommés de 1 à N")

            elif message == 'type' :
                self.popUp.setText("Le dossier le doit contenir que des images")
                self.popUp.setIcon(QMessageBox.Icon.Information)
                self.popUp.setStandardButtons(QMessageBox.Ok)
                self.popUp.show()
                btn = self.popUp.button(QMessageBox.Ok)
                #self.label.setText("Choisissez un dossier contenant uniquement des images ")
                btn.clicked.connect(self.popUp.accept)
                self.progress.setValue(0)
                self.progress.setHidden(False)
            elif message =='data' :
                self.popUp.setText("Données vérifiées")
                self.popUp.setIcon(QMessageBox.Icon.Information)
                self.popUp.setStandardButtons(QMessageBox.Ok)
                self.popUp.show()
                btn = self.popUp.button(QMessageBox.Ok)
                btn.clicked.connect(self.popUp.accept)    
                self.chargeListe.setEnabled(True)     
                self.status.setText("Vous pouvez passé à l'étape 3")
                self.progress.setValue(100)
                self.progress.setHidden(False)
            elif message == 'ordre' :
                self.popUp.setText("Les fichiers n'ont pas été renommés avec des caractères numériques")
                self.popUp.setIcon(QMessageBox.Icon.Information)
                self.popUp.setStandardButtons(QMessageBox.Ok)
                self.popUp.show()
                btn = self.popUp.button(QMessageBox.Ok)
                #self.label.setText("Nommés les fichiers avec des caractères numériques")
                btn.clicked.connect(self.popUp.accept)
                self.progress.setValue(0)
                self.progress.setHidden(True)


