# coding:utf-8
from UI.lib import *
from UI.about import homeFrame
from UI.MA import (SelectData , collectInformation , 
                   maResults, createImageThread,maDataBase)
from UI.home import *
from UI.traitement import TraitementInterface
from UI.OSCMA import Stoch


class Widget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(" ","-"))
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)

        
class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        print("Window called")
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width() , desktop.height()
        self.resize(int(desktop.width()*0.90) , desktop.height())
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
                
        # create sub interface
        self.homeInterface = Widget('home', self)
        self.homeInterface.vBox.addWidget(AppInfoCard(self.homeInterface) )
        
        self.MA = QStackedWidget(self)
        self.getMAdata = SelectData( self.MA)
        
        self.getMAinfos_Widget = QWidget(self.MA)
        self.getMAinfos = collectInformation(self.getMAinfos_Widget)
        self.vBox1 = QVBoxLayout(self.getMAinfos_Widget)
        self.getMAinfos_Widget.setLayout(self.vBox1)
        self.vBox1.addWidget(self.getMAinfos)
        ##self.vBox1.addWidget(self.getMAinfos.navigationFrame)
        
        self.MA_resultat_Widget = QWidget(self.MA)
        self.MA_resultat = maResults(self.MA_resultat_Widget)
        self.MA_resultat_Widget.vBox = QVBoxLayout()
        self.MA_resultat_Widget.setLayout(self.MA_resultat_Widget.vBox)
        self.MA_resultat_Widget.vBox.addWidget(self.MA_resultat.startBtn,0,LEFT|CENTER)
        self.MA_resultat_Widget.vBox.addWidget(self.MA_resultat,2)
        self.MA_resultat_Widget.vBox.addWidget(self.MA_resultat.navigationFrame,0)
        
        
        self.MA_DataBase_Widget = QWidget(self.MA)
        self.MA_DataBase = maDataBase(self.MA_DataBase_Widget)
        self.MA_DataBase.setContentsMargins(0,0,30,0)
        vBox = QVBoxLayout(self.MA_DataBase_Widget)
        self.MA_DataBase_Widget.setLayout(vBox)
        vBox.addWidget(self.MA_DataBase.frame)
        vBox.addWidget(self.MA_DataBase,1)
        vBox.addWidget(self.MA_DataBase.backBtn,0,LEFT|CENTER)
        
        ## Traitement
        self.traitementInterface = TraitementInterface(self.MA)
        
        self.MA.addWidget(self.getMAdata )
        self.MA.addWidget(self.getMAinfos_Widget )
        self.MA.addWidget(self.MA_resultat_Widget)
        self.MA.addWidget(self.MA_DataBase_Widget)
        self.MA.setObjectName("stack")
        
        self.OSMA = Stoch(self)
        self.OSMA.setObjectName("stochastique")

        self.about = Widget("about" , self)
        self.traitementInterface.setObjectName("traitement")
        self.about.vBox.addWidget(homeFrame(self))
        self.settingInterface = Widget('Setting', self)
        
        self.splashScreen = SplashScreenImage(r"image\SB.gif", self)

        # customize the title bar of splash screen
        # titleBar = StandardTitleBar(self.splashScreen)
        # titleBar.setIcon(self.windowIcon())
        # titleBar.setTitle(self.windowTitle())
        # self.splashScreen.setTitleBar(titleBar)

        self.show()
        self.createSubInterface(val=3500)        
        self.initNavigation()
        self.initWindow()
        self.initButton()
        self.splashScreen.finish()  
        
        
    def createSubInterface(self , val:int):
        loop = QEventLoop(self)
        QTimer.singleShot(val, loop.quit)
        loop.exec()



    def initButton(self) :
        self.getMAdata.btn.clicked.connect(lambda : self.getMAdata.fileDialog())
        self.getMAdata.nextBtn.clicked.connect(lambda : self.getMAdata.nextPage(parent=self.MA , next=self.getMAinfos_Widget))
        #self.getMAdata.nextBtn.clicked.connect(lambda : self.getMAinfos.initGrid(file=self.getMAdata.filePath))
        #self.getMAdata.filePath = r"C:\Users\steph\OneDrive\Documents\MesProjets\AppPython\TradingStrategyComparer\BRVM-Financials.csv"
        
        self.getMAdata.nextBtn.clicked.connect(lambda : self.getMAinfos.initGrid(file=self.getMAdata.filePath))
        self.getMAdata.nextBtn.clicked.connect(lambda : print(self.getMAdata.filePath))
        self.getMAdata.nextBtn.clicked.connect(lambda : self.getMAinfos.backBtn.clicked.connect(lambda : self.getMAinfos.previewPage(preview=self.getMAdata , parent=self.MA)))
        self.getMAdata.nextBtn.clicked.connect(lambda : self.getMAinfos.nextBtn.clicked.connect(lambda : self.getMAinfos.nextPage(next=self.MA_resultat_Widget , parent=self.MA)))
        
        #self.getMAinfos.initGrid(file=self.getMAdata.filePath)
        #self.getMAinfos.backBtn.clicked.connect(lambda : self.getMAinfos.previewPage(preview=self.getMAdata , parent=self.MA))
        #self.getMAinfos.nextBtn.clicked.connect(lambda : self.getMAinfos.nextPage(next=self.MA_resultat , parent=self.MA))
        
        self.getMAdata.nextBtn.clicked.connect(lambda : self.dataNextBtnFonction())
        self.getMAdata.nextBtn.clicked.connect(lambda: self.getMAinfos.nextBtn.clicked.connect(lambda : self.infosNextBtnFonction())  )
    
    def infosNextBtnFonction(self) :
        self.MA_resultat.processus=createImageThread(df=self.getMAdata.filePath,
        col=self.getMAinfos.combo1.currentText(),
        close=self.getMAinfos.combo2.currentText(),
        debut=self.getMAinfos.intervalle1.value(),
        fin=self.getMAinfos.intervalle2.value(),
        rapide=self.getMAinfos.fast.value(),lente=self.getMAinfos.slow.value(),labView=self.MA_resultat.labView , 
        labResisatance=self.MA_resultat.labViewResistance)
        self.MA_resultat.backBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.getMAinfos_Widget) )
        self.MA_resultat.nextBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.MA_DataBase_Widget) )
        
        self.MA_resultat.processus.update_signal.connect(self.MA_resultat.updateLabel )
        self.MA_resultat.startBtn.clicked.connect(lambda : self.MA_resultat.lab_.setHidden(False) )
        self.MA_resultat.startBtn.clicked.connect(lambda : self.MA_resultat.parametreProgress(
            {
                "name":self.getMAdata.filePath,
                "close":self.getMAinfos.combo2.currentText(),
                "indix":self.getMAinfos.combo1.currentText(),
                "debut":self.getMAinfos.intervalle1.value() ,
                "fin":self.getMAinfos.intervalle2.value(),
                "rapide":[self.getMAinfos.rapide1.value() , self.getMAinfos.rapide2.value()],
                "lente":[self.getMAinfos.lente1.value() , self.getMAinfos.lente2.value()],
                "min_benef":self.getMAinfos.minBenefice.value(),
                "min_diff":self.getMAinfos.diffSpin.value(), 
                "min_transaction":self.getMAinfos.minTransaction.value()}
        ))
        self.MA_resultat.startBtn.clicked.connect(self.startProcess)
        self.MA_DataBase.backBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.MA_resultat_Widget))
        
    def dataNextBtnFonction(self) :
        self.vBox1.addWidget(self.getMAinfos.navigationFrame)
        self.getMAinfos.backBtn.setEnabled(False)
        self.getMAinfos.backBtn.setToolTip("Vous ne poourver plus\nChoisir une autre base de donnees")
        
    def startProcess(self) :
        self.MA_resultat.startBtn.setEnabled(False)
        self.MA_resultat.processus.run()        
        
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        
        self.p = self.addSubInterface(self.MA, qta.icon("ri.stock-fill") , 'Moving Average')
        self.addSubInterface(self.OSMA,qta.icon("ri.stock-line") , 'Stochastic Oscillator  & MACD')
        
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.traitementInterface, qta.icon("ei.broom"), "Pré-Treitement")
    
        self.navigationInterface.addSeparator()
                
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('stephene36@gmail.com', 'resource/SB.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(self.about , FIF.INFO , "About")
        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # add badge to navigation item

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('resource/SB.png'))
        self.setWindowTitle('StrategyBacktest')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            'stephenew36@gmail.com',
            '''Cette application est concu dans le cadre de l application des strategies de trading sur les donnees anterieurs
            Voir le code source 👨‍💻''',
            self
        )
        w.yesButton.setText('OK')
        w.cancelButton.setText('Cancel')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))