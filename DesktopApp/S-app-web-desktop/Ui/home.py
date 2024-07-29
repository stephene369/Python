from .lib import *
import  socket
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
        self.port=self.find_free_port() 
        self.launchWorker = LauncherWorker(port=self.port)
        self.launchWorker.finished.connect(self.launchWorkerFinished)
        self.launchWorker.start()
        self.browser.load(QUrl(f"http://localhost:{self.port}" )) 


    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]


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

    def __init__(self , port ):
        super().__init__()
        self.server = Launcher()
        self.port = port
        print("Launcher Worker Initializ")


    def run(self):
        try : 
            self.link = self.server.lauch(port=self.port)
            self.finished.emit({
            "link":f"http://localhost:{self.port}"
            })

        except Exception as e : 
            self.finished.emit({
                "link":False
            })
