from ..Lib import *
from ..Class import *

class HomeInterface(Widget) :
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

        self.vBox = QVBoxLayout(self)
        self.homeWidget = HomeWidget(self)
        self.homeWidget.setFixedHeight(620)

        self.HomeSrollArea = SingleDirectionScrollArea(self)

        self.vBox.addSpacing(30)
        self.vBox.addWidget(self.HomeSrollArea)
        self.HomeSrollArea.setWidget(self.homeWidget)
        self.HomeSrollArea.setWidgetResizable(True)

        self.setContentsMargins(0,0,0,0)
    	

class HomeWidget(QWidget): 
    def __init__(self,parent):
        super().__init__(parent=parent)

        self.vBox = QVBoxLayout(self)
        self.appCard = AppInfoCard(self ,
        imageLabel="resource\icons\AppIcon.png",
        title="EasyCount",
        install="Commencer",
        url="https://lescal-soc.com/index.php",
        urlName="lescal-soc.com")
        
        self.counterCard = AppCard(icon=r"resource\icons\counter.png",
                title="Compteur",
                content="Choisisez une image et obtener le nombre d'element sur celle-ci",
                parent=self)
                
        self.counterCard.setFixedHeight(120)

        self.historyCard = AppCard(icon=r"resource\icons\history.png",
                title="Historique",
                content="Visualiser l'historique de toute les images passee",
                parent=self)
        self.historyCard.setFixedHeight(120)

        print(self.historyCard.styleSheet())

        self.vBox.addWidget(self.appCard)
        self.vBox.addWidget(self.counterCard)
        self.vBox.addWidget(self.historyCard)

        FluentStyleSheet.FLUENT_WINDOW.apply(self)


class AppInfoCard(SimpleCardWidget):
    def __init__(self, parent,
                imageLabel:str,
                title:str,
                install:str,
                url:str,
                urlName:str,
                ):
        super().__init__(parent)
        self.iconLabel = ImageLabel(imageLabel)
        self.iconLabel.setBorderRadius(10,10,10,10)
        self.iconLabel.scaledToWidth(200)

        self.nameLabel = TitleLabel(title , self)
        self.installButton = PrimaryPushButton(install,self)
        self.companyLabel = HyperlinkLabel(
            QUrl(url),urlName,self
        )
        self.installButton.setFixedWidth(150)

        self.scoreWidget3 = StatisticsWidget("Rapide","⏩" , self)
        self.scoreWidget0 = StatisticsWidget("Score du \nprecision","99%🥇" , self)
        self.scoreWidget2 = StatisticsWidget("Historique\n d'image","🔄" , self)
        self.scoreWidget1 = StatisticsWidget("Facile à \nutilisé",str("✍"),self)
        self.separator0 = VerticalSeparator(self)
        self.separator1 = VerticalSeparator(self)
        self.separator2 = VerticalSeparator(self)
        self.separator3 = VerticalSeparator(self)

        self.descriptionLab = BodyLabel(
            "Une application de comptage d'éléments sur image ultra-pratique. Comptez tout en un instant avec précision grâce à la puissance de la vision par ordinateur. Idéale pour une variété de besoins, de la gestion de stocks à la surveillance de la foule. Simplifiez le comptage avec notre application intuitive."
        )
        self.descriptionLab.setWordWrap(True)

        self.tagButton = PillPushButton("Contacter" , self)
        self.tagButton.setCheckable(False)
        setFont(self.tagButton, 12)
        self.tagButton.setFixedSize(80,32)

        self.hBox = QHBoxLayout(self)
        self.vBox = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.statisticsLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.initLayout()

        self.color_timer = QTimer(self)
        self.color_timer.timeout.connect(self.changeColor)
        self.color_timer.start(800)
        #self.installButton.animateClick(5000)
        
    def changeColor(self) :
        color = QColor(randint(0,250) , randint(0,250) , randint(150,250))
        self.companyLabel.setStyleSheet(f"""
background-color: transparent;
color: {color.name()}  ;
font: 16px 'Segoe UI', 'Microsoft YaHei';
""")


    def initLayout(self) :
        self.hBox.setSpacing(30)
        self.hBox.setContentsMargins(34, 24, 24, 24)
        self.hBox.addWidget(self.iconLabel,0,LEFT|TOP)
        self.hBox.addLayout(self.vBox,1)

        self.vBox.setContentsMargins(0, 0, 0, 0)
        self.vBox.setSpacing(0)

        ## 
        self.vBox.addLayout(self.topLayout)
        self.topLayout.setContentsMargins(0,0,0,0)
        self.topLayout.addWidget(self.nameLabel)
        self.topLayout.addWidget(self.installButton,0, Qt.AlignRight)

        ## 
        self.vBox.addSpacing(3)
        self.vBox.addWidget(self.companyLabel,0,LEFT|CENTER)

        ## Stati
        self.vBox.addSpacing(20)
        self.vBox.addSpacing(20)
        self.vBox.addLayout(self.statisticsLayout)
        self.statisticsLayout.setContentsMargins(0, 0, 0, 0)
        self.statisticsLayout.setSpacing(10)
        self.statisticsLayout.addWidget(self.scoreWidget0)
        self.statisticsLayout.addWidget(self.separator0)
        self.statisticsLayout.addWidget(self.scoreWidget1)
        self.statisticsLayout.addWidget(self.separator1)       
        self.statisticsLayout.addWidget(self.scoreWidget2)
        self.statisticsLayout.addWidget(self.separator2)   
        self.statisticsLayout.addWidget(self.scoreWidget3)
        self.statisticsLayout.addWidget(self.separator3)   

        self.statisticsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #self.statisticsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ##
        self.vBox.addSpacing(20)
        self.vBox.addWidget(self.descriptionLab)

        ## Button 
        self.vBox.addSpacing(12)
        self.buttonLayout.setContentsMargins(0,0,0,0)
        self.vBox.addLayout(self.buttonLayout)
        self.buttonLayout.addWidget(self.tagButton, 0, Qt.AlignLeft)
    

class StatisticsWidget(QWidget):
    """ Statistics widget """

    def __init__(self, title: str, value: str, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = CaptionLabel(title, self)
        self.valueLabel = BodyLabel(value, self)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.setContentsMargins(16, 0, 16, 0)
        self.vBoxLayout.addWidget(self.valueLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignBottom)

        setFont(self.valueLabel, 18, QFont.DemiBold)
        self.titleLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))


class AppCard(CardWidget):
    """ App card """

    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)

        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton('Cliquer', self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(65, 65)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)
        self.moreButton.clicked.connect(self.onMoreButtonClicked)

    def onMoreButtonClicked(self):
        menu = RoundMenu(parent=self)
        menu.addAction(Action(FluentIcon.SHARE, 'share', self))
        menu.addAction(Action(FluentIcon.PIN, 'pin', self))

        x = (self.moreButton.width() - menu.width()) // 2 + 10
        pos = self.moreButton.mapToGlobal(QPoint(x, self.moreButton.height()))
        menu.exec(pos)
