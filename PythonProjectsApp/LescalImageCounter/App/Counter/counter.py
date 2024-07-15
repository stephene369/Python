from ..Lib  import * 
from ..Class import Widget
from ..Process import ShowImageProcessus,EasyCountProcess

class CounterInterface(Widget) :
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

        self.CounterScrollArea = SingleDirectionScrollArea(self)
        self.CounterWidget = CounterWidget(self.CounterScrollArea)

        self.vBox = QVBoxLayout(self)
        self.vBox.addSpacing(30)
        self.vBox.addWidget(self.CounterScrollArea)
        self.CounterScrollArea.setWidget(self.CounterWidget)
        self.CounterScrollArea.setWidgetResizable(True)

        self.vBox.setContentsMargins(0,30,0,0)

class CounterWidget(QWidget) :
    def __init__(self,parent=None) :
        super().__init__(parent=parent)

        self.newBtn = PushButton("",self)
        self.newBtn.setIcon(qta.icon("mdi.autorenew"))
        self.newBtn.setIconSize(QSize(50,50))

        self.VBOX = QVBoxLayout(self)
        self.VBOX.addWidget(self.newBtn,0,LEFT|TOP)
        

        self.newBtn.clicked.connect(self.newInterface)
        #self.initObject()
    
    def newInterface(self) :
        try : 
            self.Frame0.deleteLater()
            self.Frame1.deleteLater()
            self.vBox.deleteLater()
        except Exception as e : print(e)

        self.update()
        self.initObject()
        self.newBtn.setHidden(True)

    def initObject(self) :
        self.vBox = QVBoxLayout()
        
    ## Frame 0 
        self.Frame0 = QFrame(self)
        self.vBox0 = QVBoxLayout(self.Frame0)
        
        self.addImageBtn = PushButton("",self)
        icon = qta.icon("ri.image-add-line", 
                        color='blue')

        self.addImageBtn.setSizePolicy(
            QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.addImageBtn.setIcon(icon)
        self.addImageBtn.setIconSize(QSize(150,150))
        self.addImageBtn.clicked.connect(self.fileDialog)

        self.progressRing = IndeterminateProgressRing(self)
        self.progressRing.setSizePolicy(
            QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.progressRing.setStrokeWidth(6)

        self.progressRing.setFixedSize(QSize(250,250))
        self.progressRing.setHidden(True)

        self.imageLab = ImageLabel(self)

    ## FRame1
        self.Frame1 = QFrame(self)
        self.vBox1 = QVBoxLayout(self.Frame1)
        self.Frame1.setLayout(self.vBox1)
        self.imageResultLabel = ImageLabel(self.Frame1)
        self.resultLabel = TitleLabel(self.Frame1)

    ## VBox0 
        self.vBox0.addWidget(self.addImageBtn)
        self.vBox0.addWidget(self.progressRing,0,CENTER)
        self.vBox0.addWidget(self.imageLab,0,CENTER)

    ## VBox 1
        self.vBox1.addWidget(self.imageResultLabel,0,CENTER)
        self.vBox1.addWidget(self.resultLabel,0,CENTER)

    ##VBox
        self.vBox.addWidget(self.Frame0)
        self.vBox.addWidget(self.Frame1)

    ## VBOX
        self.VBOX.addLayout(self.vBox)

    def ImageProcessing(self ) :
        self.vBox1.addWidget(self.progressRing,0,CENTER)
        self.progressRing.setHidden(False)
        self.Frame1.setHidden(False)
        
        self.imageProcess = EasyCountProcess(filePath=self.chemin,imagelab=self.imageResultLabel)
        self.imageProcess.signal.connect(self.updateResultImageLabel)
        self.imageProcess.start()

    def updateImageLabel(self,message) :
        self.progressRing.setHidden(True)
        self.imageLab.setHidden(False)
        self.chemin = message[0]

        self.ImageProcessing()


    def updateResultImageLabel(self,message) :
        self.resultLabel.setText("L'image contient : "+str(message[0])+ " elements" )
        self.progressRing.setStrokeWidth(message[1])
        
        if self.imageProcess.isFinished() :
            self.progressRing.setHidden(True)
            self.newBtn.setHidden(False)


    def fileDialog(self) :
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open images Fles", "", "Images *.png *.jpeg *.jpg *.bmp *.jfif;; Autres (*)")
        extention = [".png" , ".jpg" , ".jfif", "jpeg",".bmp" ]

        if Path(self.filePath).suffix in extention :
            self.createSuccessInfoBar(self.filePath)
            self.addImageBtn.setHidden(True)
            self.progressRing.setHidden(False)
            
            self.showImageProcess = ShowImageProcessus(
                filepath=self.filePath,imageLab=self.imageLab)
            self.showImageProcess.signal.connect(self.updateImageLabel)
            self.showImageProcess.start()
        
        elif self.filePath and (Path(self.filePath).suffix not in extention) :
            self.cresteError2InfosBar()
        else :
            self.createErrorInfoBar()

    def createSuccessInfoBar(self , filepath):
        # convenient class mothod
        InfoBar.success(
            title='sucess',
            content=f"{filepath}\ncharger avec succes",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self)

    def createErrorInfoBar(self):
        InfoBar.error(
            title='erreur',
            content=f"Veillez charger un fichier ",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,    # won't disappear automatically
            parent=self)

    def cresteError2InfosBar(self):
        InfoBar.error(
            title='erreur',
            content=f"Le fichier {self.filePath} \n n'est pas prise en charge ",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=2000,    # won't disappear automatically
            parent=self)