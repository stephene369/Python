from Ui.library import *

class Page1 :
    def __init__(self , parent:QWidget) :
        self.parent = parent 

    
    def setupUi(self) :
        self.page = QWidget(self.parent)

        
        self.Hbox = QHBoxLayout(self.page)
        self.maBtn = QPushButton(self.page , objectName='maBtn')
        self.macdBtn = QPushButton(self.page , objectName='macdBtn')

        icon = QIcon("icons/ma.jpg")
        self.maBtn.setIcon(icon)
        self.maBtn.setIconSize(QSize(100,100))
        self.maBtn.setText("Moving \n Average")

        icon = QIcon("icons/macd.png")
        self.macdBtn.setIcon(icon)
        self.macdBtn.setIconSize(QSize(100,100))
        self.macdBtn.setText("Stochastic \n MACD ")

        self.Hbox.addWidget(self.maBtn)
        self.Hbox.addWidget(self.macdBtn)
        
        self.maBtn.clicked.connect(self.ma)
        self.macdBtn.clicked.connect(self.macd)

        self.page.setContentsMargins(50,50,50,50)


        return (self.page , self.maBtn , self.macdBtn)
    
    def ma (self) :
        pass 

    def macd(self) :
        pass