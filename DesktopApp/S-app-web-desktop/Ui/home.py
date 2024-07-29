from .lib import *

class HomeWidget(QWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = FramelessWebEngineView(self)

        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)

        ## Launch Main brower 
        
        #self.browser.load(QUrl("https://github.com/stephene369/"))
        self.launchWorker = LauncherWorker()
        self.launchWorker.finished.connect(self.launchWorkerFinished)
        self.launchWorker.start()


    def launchWorkerFinished(self , success):
        print(success)
        if success["link"] == False: 
            print("Le lien ne marche")
        else : 
            self.link = success["link"]
            self.browser.load(QUrl( self.link ))
            print("Server en cours")



class LauncherWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self ):
        super().__init__()
        self.server = Launcher()
        print("Launcher Worker Initializ")


    def run(self):

        self.link = self.server.lauch()

        print("Launcher run" , self.link)

        self.finished.emit({
        "link":"https://github.com/stephene369/"
        })
