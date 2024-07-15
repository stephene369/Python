# coding:utf-8
from UI.lib import *
from UI.home import homeFrame
from UI.MA import (SelectData , collectInformation , 
                   maResults, createImageThread,maDataBase)

class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(" ","-"))
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)

        
class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Widget('home', self)
        
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
        
        
        self.MA.addWidget(self.getMAdata )
        self.MA.addWidget(self.getMAinfos_Widget )
        self.MA.addWidget(self.MA_resultat_Widget)
        self.MA.addWidget(self.MA_DataBase_Widget)
        self.MA.setObjectName("stack")
        
        self.OSMA = Widget("macd" , self)
        self.about = Widget("about" , self)
        self.about.vBox.addWidget(homeFrame(self))
        self.settingInterface = Widget('Setting', self)
        
        self.initNavigation()
        self.initWindow()
        self.initButton()
        #self.MA.setCurrentWidget(self.MA_resultat )
        
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
        
        self.getMAdata.nextBtn.clicked.connect(lambda : self.infosNextBtnFonction())
    
    def infosNextBtnFonction(self) :
        self.MA_resultat.backBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.getMAinfos_Widget) )
        self.MA_resultat.nextBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.MA_DataBase_Widget) )
        self.MA_resultat.processus=createImageThread(df=self.getMAdata.filePath,col="Date",debut=0,fin=200,rapide=10,lente=20)
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
        self.vBox1.addWidget(self.getMAinfos.navigationFrame)
        self.MA_DataBase.backBtn.clicked.connect(lambda : self.MA.setCurrentWidget(self.MA_resultat_Widget))
        self.getMAinfos.backBtn.setEnabled(False)
        self.getMAinfos.backBtn.setToolTip("Vous ne poourver plus\nChoisir une autre base de donnees")
        
    def startProcess(self) :
        self.MA_resultat.startBtn.setEnabled(False)
        self.MA_resultat.processus.run()
        
        
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.MA, FIF.PENCIL_INK, 'Moving Average')
        self.addSubInterface(self.OSMA, FIF.PENCIL_INK, 'Stochastic Oscillator  & MACD')
        
        self.navigationInterface.addSeparator()
        
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('stephene36@gmail.com', 'resource/shoko.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(self.about , FIF.INFO , "About")
        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # add badge to navigation item

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('resource/shoko.png'))
        self.setWindowTitle('Python -PyQt5 -  PyQt-Fluent-Widgets')

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