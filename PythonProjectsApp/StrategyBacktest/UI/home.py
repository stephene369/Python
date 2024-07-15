import typing
from UI.lib import *


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

class AppInfoCard(SimpleCardWidget):
    """ App information card """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.imageLabel = ImageLabel(self)
        self.imageLabel.setImage(r"image\SB.gif")
        self.imageLabel.setFixedHeight(100)
        self.imageLabel.setFixedWidth(100)
        
        self.nameLabel = TitleLabel('StrategyBacktest', self)
        self.installButton = PrimaryPushButton('Apercu', self)
        #self.installButton.setTex()
        self.installButton.clicked.connect(self.MA_ViewFlyout)
        self.companyLabel = HyperlinkLabel(QUrl('https://github.com/'),
            'stephenew36@gmail.com.', self)
        self.installButton.setFixedWidth(160)

        self.scoreWidget = StatisticsWidget('Visualisation\nDes donnees', '', self)
        self.separator = VerticalSeparator(self)
        self.commentWidget = StatisticsWidget('Simulation\nde trading', '', self)
        self.separator1 = VerticalSeparator(self)
        self.commentWidget1 = StatisticsWidget('Filtrage de \nParametre', '', self)
        
        self.descriptionLabel = BodyLabel(
            "Dans cette application est il possble de tester la strategies des Moyenne Mobile pu la strategie Combinee de l'Oscillateur Stochastique a la Moyenne Mobile Convergence Divergence, de visualiser les donnees de faire les somulations en fonctino de votre profile d'investisseur", self)
        self.descriptionLabel.setWordWrap(True)

        self.tagButton = PillPushButton('ApercuMA', self)
        self.tagButton.setCheckable(True)
        setFont(self.tagButton, 12)
        self.tagButton.setFixedSize(80, 32)
        self.tagButton.setHidden(True)

        self.shareButton = TransparentToolButton(FluentIcon.SHARE, self)
        self.shareButton.setFixedSize(32, 32)
        self.shareButton.setIconSize(QSize(14, 14))

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.statisticsLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.initLayout()
        
        self.color_timer = QTimer(self)
        self.color_timer.timeout.connect(self.changeColor)
        self.color_timer.start(800)
        #self.installButton.animateClick(5000)
        
    def changeColor(self) :
        color = QColor(randint(160,170) , randint(160,200) , randint(180,200))
        self.installButton.setStyleSheet(f"""
background-color: {color.name()};
color: black;
border: 1px solid rgba(0, 0, 0, 0.073);
border-bottom: 1px solid rgba(0, 0, 0, 0.183);
border-radius: 5px;
font: 16px 'Segoe UI', 'Microsoft YaHei';
padding: 5px 12px 6px 12px;
outline: none;                                         
                                         """)
        self.companyLabel.setStyleSheet(f"""
color: {color.name()};
border: none;
border-radius: 6px;
background-color: transparent;
                                        """)
        
    def initLayout(self):
        self.hBoxLayout.setSpacing(30)
        self.hBoxLayout.setContentsMargins(34, 24, 24, 24)
        #self.hBoxLayout.addWidget(self.iconLabel)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)

        # name label and install button
        self.vBoxLayout.addLayout(self.topLayout)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.addWidget(self.imageLabel)
        self.topLayout.addWidget(self.nameLabel)
        self.topLayout.addWidget(self.installButton, 0, Qt.AlignRight)

        # company label
        self.vBoxLayout.addSpacing(3)
        self.vBoxLayout.addWidget(self.companyLabel,0,LEFT|TOP)

        # statistics widgets
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addLayout(self.statisticsLayout)
        self.statisticsLayout.setContentsMargins(0, 0, 0, 0)
        self.statisticsLayout.setSpacing(10)
        self.statisticsLayout.addWidget(self.scoreWidget,0,HCENTER|TOP)
        self.statisticsLayout.addWidget(self.separator)
        self.statisticsLayout.addWidget(self.commentWidget,0,HCENTER|CENTER)
        self.statisticsLayout.addWidget(self.separator1)
        self.statisticsLayout.addWidget(self.commentWidget1,0,HCENTER|TOP)
        
        self.statisticsLayout.setAlignment(Qt.AlignLeft)

        # description label
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(self.descriptionLabel)

        # button
        self.vBoxLayout.addSpacing(12)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.buttonLayout.addWidget(self.tagButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.shareButton, 0, Qt.AlignRight)

    def MA_ViewFlyout(self) :
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='Strategie des Moyennes Mobile',
            content="""
La stratégie des moyennes mobiles utilise les moyenne mobile arithmétiques sur deux differentes périodes :
la moyenne mobile lente (moyenne longue) et la moyenne mobile rapide (courte).Lorsque la moyenne mobile 
rapide croise et dépasse la moyenne mobile lente alors le marché est en tendance haussière ce qui est un 
signal d'achat. Le cas contraire traduit un signal de vente
    """,
            target=self.tagButton,
            parent=self,
            isClosable=True,
            image=r"image\MAanimation.gif")
    




class hommeWidget(QWidget) :
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        
        self.MA_Btn = PushButton("Moving Average" , self)
        self.MA_Btn.clicked.connect(self.MA_ViewFlyout)
    
    def MA_ViewFlyout(self) :
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='Strategie des Moyennes Mobile',
            content="""
La stratégie des moyennes mobiles utilise les moyenne mobile arithmétiques sur deux differentes périodes :
la moyenne mobile lente (moyenne longue) et la moyenne mobile rapide (courte).Lorsque la moyenne mobile 
rapide croise et dépasse la moyenne mobile lente alors le marché est en tendance haussière ce qui est un 
signal d'achat. Le cas contraire traduit un signal de vente
    """,
            target=self.MA_Btn,
            parent=self,
            isClosable=True,
            image=r"image\MAanimation1.gif")

