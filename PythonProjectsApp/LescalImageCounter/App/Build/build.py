from ..Lib import * 
from ..Class import *
from ..Home import *
from ..Splash import *
from ..Common import *
from ..Setting import *
from ..Counter import *
from ..History import *

class Main(Window) :
    def __init__(self):
        super().__init__()

        self.HomeInterface = HomeInterface("Home")
        self.SettingInterface = SettingInterface("Setting")
        self.counterInterface = CounterInterface("Conteur")
        self.HistoryInterface = HistoryInterface("Historique")

        self.SplashInterface = SplashInterface(
            icon=r"resource\icons\SplashIcon.png",
            parent=self)
        

        self.show()

        self.SplashInterface.createSubInterface(val=2500)        
        self.AddInterface()
        self.initButton()

        self.SplashInterface.finish()
        

    def AddInterface(self) :
        self.addSubInterface(interface=self.HomeInterface,
            icon=qta.icon("ei.home") , 
            text="Explorer")

        self.addSubInterface(interface=self.counterInterface, 
            icon=qta.icon("mdi.speedometer-slow","mdi.speedometer","mdi6.speedometer-medium"),
            text="Conteur d'element")

        self.addSubInterface(interface=self.HistoryInterface, 
            icon=qta.icon("ri.chat-history-fill"),
            text="Historique d'Image")

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget("LESCAL" , AVATAR_ICON ),
            position=NavigationItemPosition.BOTTOM,
            tooltip="Visiter notre Site",
            onClick=self.showMessage
        )

        self.addSubInterface(self.SettingInterface,
            qta.icon("ri.settings-5-line"),"Parametre",
            NavigationItemPosition.BOTTOM)
        

    def showMessage(self) :
        w = MessageBox(
            "LESCEL",
            "LAboratoire d'Etude Statistique et de Concetion d'Application et Logiciel",
            self
        )
        w.yesButton.setText("Visiter")
        w.cancelButton.setText("Sortir")

        if w.exec() :
            QDesktopServices.openUrl(QUrl("https://lescal-soc.com/index.php"))
    

    def initButton(self) :
        self.HomeInterface.homeWidget.counterCard.openButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.counterInterface) )
        self.HomeInterface.homeWidget.historyCard.openButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.HistoryInterface) )
        self.HomeInterface.homeWidget.appCard.installButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.counterInterface) )
        