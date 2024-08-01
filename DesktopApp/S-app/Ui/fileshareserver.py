from .lib import * 
from App import FileServer 


class ServerWidget(SmoothScrollArea):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        home_dir = Path.home()
        downloads_dir = home_dir / "Downloads"
        media_dir = downloads_dir / "media"

        self.Frame = QFrame(self)
        
        self.setObjectName(text.replace(' ', '-'))
        
                

        self.VBox = QVBoxLayout(self)

        ## FRAME 1 
        self.frame1 = QFrame(self)
        self.Box_frame1 = QVBoxLayout(self.frame1)
        self.VBox.addWidget(self.frame1 , 0 , Qt.AlignmentFlag.AlignTop)

        self.titleLabel = TitleLabel("File Server", self.frame1)
        self.subTitle = SubtitleLabel(self.frame1)

        self.Box_frame1.addWidget(self.titleLabel)
        self.Box_frame1.addWidget(self.subTitle)

        self.subTitle.setText(f"Every file on {media_dir} will be available publicly")
        self.subTitle.setObjectName("subTitle")

        ## FRAME 2
        self.frame2 = QFrame(self)
        self.VBox.addWidget(self.frame2 , 1 , Qt.AlignmentFlag.AlignCenter)
        self.Box_frame2 = QHBoxLayout(self.frame2)

        self.launchButton = TransparentPushButton(FIF.WIFI,"Launch Server", self.frame2)
        self.linkButton = HyperlinkButton(self.frame2)
        self.linkButton.click
        
        self.launchButton.clicked.connect(self.updateServer)

        self.Box_frame2.addWidget(self.launchButton)
        self.Box_frame2.addWidget(self.linkButton)

        with open("resources/fileshareserver.qss" , encoding='utf-8') as f : 
            style = f.read()
            self.setStyleSheet( style )
            self.subTitle.setStyleSheet(style)
            



    def updateServer(self) : 
        print("Update/Launch Server")
        self.worker = Worker(self.linkButton)
        self.worker.finished.connect(self.handleServerUpdate)
        self.worker.start()
        #self.linkButton.setUrl(f"http://{self.Server.local_ip}/{self.Server.port}")


    def handleServerUpdate(self, success):
        if success:
            return True
        else:
            self.linkButton.setUrl("")
            self.linkButton.setStyleSheet("color:red")


class Worker(QThread):
    finished = pyqtSignal(bool)

    def __init__(self , hyperlink :HyperlinkButton):
        super().__init__()
        self.server = FileServer()
        self.hyperlink  = hyperlink

    def run(self):
        try:
            self.server.launch(hyperlink=self.hyperlink)
            self.finished.emit(True)
        except Exception as e:
            self.finished.emit(False)