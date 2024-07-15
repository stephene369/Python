from Ui.library import *
from Ui.Acceuil import Acceuil
from Ui.PageMa import Page2
from Ui.PageMacd import Page3
from Ui.maResult import Page2_1

from win32api import GetSystemMetrics , GetUserName
from Ui.PageChoix import Page1

WIDTH_ = GetSystemMetrics(0)
HEIGHT_ = GetSystemMetrics(1)
USER = GetUserName()

X = int(WIDTH_*0.20)
Y = int(HEIGHT_*0.20)
W = WIDTH_  - (2*X)
H = HEIGHT_ - (2*Y) 

class Ui_MainWindow(object) :
    def __init__(self,MainWindow : QMainWindow) :
        self.MainWindow = MainWindow 
        self.MainWindow.setGeometry(X,Y,W,H)

        self.Stacked = QStackedWidget(self.MainWindow)

        self.policy = QSizePolicy(QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Expanding )
        
        self.MainWindow.setCentralWidget(self.Stacked)
        self.Stacked.setContentsMargins(0, 0, 0, 0)

    def setupUi(self) :        
        ## Acceuil
        Acc = Acceuil(self.Stacked)
        self.PageAcceuil , self.button = Acc.setupUi()
        self.Stacked.addWidget(self.PageAcceuil)  
        self.PageAcceuil.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        ## PAge 1 
        self.Page = Page1(self.Stacked)
        self.Page1 , self.maBtn , self.macdBtn = self.Page.setupUi()
        self.Stacked.addWidget(self.Page1)

        ## PAge 2 : PROFIL PARAMETRE STRETEGY MOUVING AVERAGE
        self.Page = Page2(self.Stacked)
        self.Page2,self.btn = self.Page.setupUi()
        self.Stacked.addWidget(self.Page2)
        self.btn.clicked.connect(lambda: 4)

        ## PAGE 2_1 PROCESSING PAGE
        self.Page_ = Page2_1(self.Stacked,"data\\AMAZON.csv")
        self.Page2_1 = self.Page_.setupUi()
        self.Stacked.addWidget(self.Page2_1)
        self.btn.clicked.connect(lambda: self.Stacked.setCurrentWidget(self.Page2_1))
        self.btn.clicked.connect(lambda: self.Page_.para() )
        

        ## Page 3 : PROFIL PARAMETRE STRETEGY MOUVING AVERAGE
        self.Page = Page3(self.Stacked)
        self.Page3 = self.Page.setupUi()
        self.Stacked.addWidget(self.Page3)

## BUTTON CONNECTION 
        self.button.clicked.connect(lambda: self.recentIndix() )
        self.maBtn.clicked.connect(lambda: self.recentIndix())
        self.macdBtn.clicked.connect(lambda : self.recentIndix())

        self.button.clicked.connect(lambda : self.fileDialog() )
        self.maBtn.clicked.connect(lambda : self.Stacked.setCurrentWidget(self.Page2))
        self.macdBtn.clicked.connect(lambda : self.Stacked.setCurrentWidget(self.Page3))

        self.Stacked.setCurrentWidget(self.Page2)
        self.btn.click()

    def fileDialog(self) :
        #self.filename = QFileDialog.getOpenFileName(self.PageAcceuil, "Choisir un fichier", r"C:\Users\steph\LicenceASE2021_2023\6eme semestre\monMemoire\notebook\data", "CSV (*.csv)")
        #self.filename = self.filename[0]
        #if self.filename.endswith(".csv"): 
        self.Stacked.setCurrentWidget(self.Page1)

    def recentIndix(self) :
        RECENT = self.Stacked.currentWidget()