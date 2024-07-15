from modules.recentDir import recent
from PySide6.QtWidgets import QFileDialog , QLabel,QPushButton , QProgressBar
from pathlib import Path
from modules.File import *


class boiteDialogue :
    def __init__(self , dialog:QFileDialog ,lab:QLabel , 
                 verif:QPushButton, start:QPushButton,status:QLabel,
                 progress:QProgressBar,chargeListe:QPushButton,
                 liste_file2:list=[]) -> None:
        self.dialog = dialog
        self.label = lab
        self.verificaton = verif
        self.start = start
        self.status = status
        self.progress=progress
        self.chargeList = chargeListe
        self.liste_file2 = liste_file2
        self.list_noms = ''
        print(self.liste_file2)

        pass


    def Boite(self , typ:str):
        if typ == 'xls' :
            path = recent().read_()
            self.xls_file ,_ = self.dialog.getOpenFileName(None,"Liste",path,'*.xls')
            
            print(self.xls_file)
            if self.xls_file == '' :
                self.progress.setValue(0)
                self.start.setEnabled(False) 

            else :
                self.start.setEnabled(True)            
                self.progress.setValue(0)
                self.status.setText("Vous pouvez passer à l'étape 4 ")
                choix = choiceListe()
                choix.choice_liste(path=self.xls_file , liste_file2=self.liste_file2)
                # Recuperation de la liste des noms de chaque sheet
                self.list_noms = choix.names
        
        elif typ =='file' :
            path = recent().read_()
            self.dialog.setFileMode(QFileDialog.FileMode.AnyFile)
       
            self.file_path,_ = self.dialog.getOpenFileNames( None,"fichiers ",path)
            print(self.file_path)
            self.label.setText(str(self.file_path))
            if self.file_path != [] : 
                recent().write_(str(Path(self.file_path[0]).parent)) 
                print("done") 
                self.progress.setHidden(True)
                self.progress.setValue(0)
                self.status.setText("Vous pouvez passé à l'étape 2")
                self.verificaton.setEnabled(True) ; self.start.setEnabled(False) 
                self.chargeList.setEnabled(False)
               
            else : 
                self.verificaton.setEnabled(False) ; self.start.setEnabled(False) 
                self.chargeList.setEnabled(False)
                self.status.setText("Étape 1 ")
            
        elif typ =="image" :
            self.dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            self.dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.gif  *.bmp *.tiff *.svg *.icon *.webp *.raw *.exif *.psd *.ai *.eps *.xcf *.indd)")
            self.dialog.setFileMode(QFileDialog.ExistingFiles)
            self.dialog.exec_()
            self.file_path = self.dialog.selectedFiles()
            self.label.setText(str(self.file_path))
            
            if self.file_path != [] : self.verificaton.setEnabled(True) ; self.start.setEnabled(False)
            else : self.verificaton.setEnabled(False) ; self.start.setEnabled(False)

