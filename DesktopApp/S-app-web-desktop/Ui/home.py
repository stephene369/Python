from .lib import *
import  socket
class HomeWidget(QWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = QWebEngineView(self)

        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)

        ## Launch Main brower 
        
        #self.browser.load(QUrl("https://github.com/stephene369/"))
        self.port=self.find_free_port() 
        self.launchWorker = LauncherWorker(port=self.port , browser=self.browser)
        self.launchWorker.finished.connect(self.launchWorkerFinished)
        self.launchWorker.start()
        self.browser.load(QUrl(f"http://localhost:{self.port}" )) 

        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.on_downloadRequested)

    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]

    def launchWorkerFinished(self, success):
        print(success)
        if success["link"] == False: 
            print("Le lien ne marche pas")
        else: 
            self.link = success["link"]
            self.browser.load(QUrl(self.link))
            print("Server en cours")

    def on_downloadRequested(self, download):
        downloadPath = QFileDialog.getSaveFileName(self, "Save File", download.path())[0]
        if downloadPath:
            download.setPath(downloadPath)
            download.accept()


class LauncherWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self , port , browser):
        super().__init__()
        self.server = Launcher(browser=browser)
        self.port = port
        print("Launcher Worker Initializ")


    def run(self):
        try : 
            self.link = self.server.launch(port=self.port)
            self.finished.emit({
            "link":f"http://localhost:{self.port}"
            })

        except Exception as e : 
            self.finished.emit({
                "link":False
            })
