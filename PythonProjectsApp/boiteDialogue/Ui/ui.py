from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
from pathlib import Path
from modules.recentDir import recent
from modules.Verification import Verification
from modules.Dialogue import boiteDialogue
from modules.File import *



"""from win32api import GetSystemMetrics , GetUserName
WIDTH_ = GetSystemMetrics(0)
HEIGHT_ = GetSystemMetrics(1)
USER = GetUserName()
PATH_ = ''

X = int(WIDTH_/5)
Y = int(HEIGHT_/5)
W = int(WIDTH_-(2*X))
H = int(HEIGHT_-(1.5*Y))"""

X,Y,W,H = 100,80,1100,600

IMAGE_SUFFIX = ['.png' , '.jpeg','.jpg','.gif','.bmp','.tiff','.svg','.ico','.webp','.raw',
                '.exif','.psd','.ai','.eps','.xcf','.indd']



class Ui_MainWindow(object) :
    def __init__(self):
        self.liste_file3 = []
        self.extension = ''


    def setupUi(self , MainWindow:QWidget): 
        MainWindow.resize(QSize())
        MainWindow.setGeometry(X,Y,W,H)
        MainWindow.setMinimumSize(QSize(850,500))
        #MainWindow.setMaximumSize(QSize(W,H))
        #MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setWindowTitle("Easer Mark")

    
        self.central = QWidget(MainWindow)
        self.VBox0 = QVBoxLayout(MainWindow)
        self.VBox0.addWidget(self.central)

        self.frame0 = QFrame(self.central)
        self.frame1 = QFrame(self.central)
        self.status = QLabel(self.central)
        
        self.VBox1 = QVBoxLayout(self.central)
        self.VBox1.addWidget(self.frame0)
        self.VBox1.addWidget(self.frame1)
        self.VBox1.addWidget(self.status,0,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

# rfame 0
        self.hBox0 = QHBoxLayout(self.frame0)
        self.hSapce = QSpacerItem(40,20,
        QSizePolicy.Expanding , QSizePolicy.Minimum)
        self.close = QPushButton()
        self.logo = QLabel(self.frame0)


        self.hBox0.addWidget(self.logo)
        self.hBox0.addSpacerItem(self.hSapce)


## Frame1 
        self.frame1.setSizePolicy(QSizePolicy.Minimum,
                                  QSizePolicy.Expanding) 
        self.VBox_frame1 = QVBoxLayout(self.frame1)
        self.frame1_0 = QFrame(self.frame1)
        self.frame1_1 = QFrame(self.frame1)
        self.frame1_2 = QFrame(self.frame1)
        self.VBox_frame1.addWidget(self.frame1_0)
        self.VBox_frame1.addWidget(self.frame1_1)
        self.VBox_frame1.addWidget(self.frame1_2)

    ## FRAME 1.0
        self.VBox_frame1_0 = QVBoxLayout(self.frame1_0)
        self.LOGO = QLabel(self.frame1_0)
        self.VBox_frame1_0.addWidget(self.LOGO,0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.LOGO.setStyleSheet("""font: italic 70pt "Palace Script MT";border-radius:35px;background:rgba(12,12,12,50)""")
        self.LOGO.setText("LOGO")

    ## FRAME 1.1
        self.HBox_frame1_1 = QHBoxLayout(self.frame1_1)
        self.frame1_1_0 = QFrame(self.frame1_1)
        self.frame1_1_1 = QFrame(self.frame1_1)
        self.grid0 = QGridLayout(self.frame1_1_0 )
        self.grid1 = QGridLayout(self.frame1_1_1 )
        [(grid.setContentsMargins(40,40,40,0),grid.setSpacing(40)) 
        for grid in [self.grid0,self.grid1]]
        self.lab1 = QLabel(self.frame1_1_0) ; self.lab1.setText('1')
        self.lab2 = QLabel(self.frame1_1_0) ; self.lab2.setText('2')
        self.lab3 = QLabel(self.frame1_1_1) ; self.lab3.setText('3')
        self.lab4 = QLabel(self.frame1_1_1) ; self.lab4.setText('4')
        
        self.charger = QPushButton(self.frame1_1_0)
        self.verificaton = QPushButton(self.frame1_1_0)
        self.start = QPushButton(self.frame1_1_1)
        self.chargeListe = QPushButton(self.frame1_1_1)

        self.HBox_frame1_1.addWidget(self.frame1_1_0)
        self.HBox_frame1_1.addWidget(self.frame1_1_1)

        self.grid0.addWidget(self.lab1,0,0,1,1,Qt.AlignRight)
        self.grid0.addWidget(self.lab2,1,0,1,1,Qt.AlignRight)
        self.grid0.addWidget(self.charger,0,1,1,4)
        self.grid0.addWidget(self.verificaton,1,1,1,4)

        self.grid1.addWidget(self.lab3,0,0,1,1,Qt.AlignRight)
        self.grid1.addWidget(self.lab4,1,0,1,1,Qt.AlignRight)
        self.grid1.addWidget(self.chargeListe,0,1,1,4)
        self.grid1.addWidget(self.start,1,1,1,4)

        self.charger.setText("Charger Données")
        self.verificaton.setText("Verifier Données")
        self.chargeListe.setText("Charger Liste")
        self.start.setText("Demarrer")

        self.verificaton.setEnabled(False)
        self.chargeListe.setEnabled(False)
        self.start.setEnabled(False)

        self.dialog = QFileDialog()
        self.popUp = QMessageBox()

    ## FRAME 1.2
        self.VBox_frame1_2 = QVBoxLayout(self.frame1_2)
        self.label = QLabel(self.frame1_2)
        self.progresse = QProgressBar(self.frame1_2)
        
        self.VBox_frame1_2.addWidget(self.label)
        self.VBox_frame1_2.addWidget(self.progresse,0,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.progresse.setFixedWidth(900)
        self.progresse.setFixedHeight(30)
        self.label.setStyleSheet("""font: 8pt "MV Boli";""")
        self.progresse.setHidden(True)
        
        
        #self.VBox_frame1_2.addWidget(self.progresse,0,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


    ## STYLE
        self.progresse.setRange(0,100)
        self.frame0.setStyleSheet("background-color:rgba(0,0,255,170)")
        self.logo.setText("   Easy  Mark  ")
        self.logo.setStyleSheet("""font: italic 25pt "Monotype Corsiva";background:transparent;color:white;""")
        self.close.setHidden(True)
        LABEL = [self.lab1,self.lab2,self.lab3,self.lab4]
        [lab.setStyleSheet("""font:20pt "MS Serif";""") for lab in LABEL]
        BUTTON = [self.charger,self.verificaton,self.chargeListe,self.start]
        [btn.setStyleSheet("""font: 25pt "MingLiU_HKSCS-ExtB";""") for btn in BUTTON]
        self.status.setStyleSheet('''font: 15pt "MingLiU_HKSCS-ExtB";color:rgba(0,0,0,250) ''')
        #self.central.setStyleSheet("background-color:rgba(0,0,255,70)")



    ## CONNECTION
        self.charger.clicked.connect(lambda :self.dialConn(dial='file') ) 
        self.chargeListe.clicked.connect(lambda: self.dialConn(dial='xls'))
        self.verificaton.clicked.connect(lambda: self.verify())
        Process = choiceListe()

        self.start.clicked.connect(lambda : Process.process(self.liste_noms, self.liste_file3))


    def dialConn(self , dial:str):

        if dial=='xls' :    
            boi = boiteDialogue(dialog=self.dialog,
                                lab=self.label,verif=self.verificaton,start=self.start,
                                status=self.status,progress=self.progresse,
                                chargeListe=self.chargeListe,liste_file2=self.listeFile2)


        elif dial=='file' :  
            boi = boiteDialogue(dialog=self.dialog,
                                lab=self.label,verif=self.verificaton,start=self.start,
                                status=self.status,progress=self.progresse,
                                chargeListe=self.chargeListe)
            
        
        boi.Boite(typ=dial)
        match dial :
            case 'file':
                self.file_path = boi.file_path 
            case 'xls' :
                self.xls_file = boi.xls_file
                self.liste_noms=boi.list_noms
                print('\ndzerzerzerzerzerezr', self.liste_noms, '\n')
        


    def verify(self) :
        ver = Verification(pop=self.popUp,lab=self.label,start=self.start,
            file_path=self.file_path,status=self.status,
            chargeList=self.chargeListe,progress=self.progresse)
        ver.Verify()
        
        self.listeFile2 = ver.liste_file2
        self.liste_file3 = ver.liste_file3
        print("liste 3",self.liste_file3)
        
        

