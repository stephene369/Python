from PyQt5.QtGui import QIcon , QColor
from PyQt5.QtCore import Qt, QEventLoop, QTimer, QSize , QThread,pyqtSignal
from PyQt5.QtCore import QSize , QEasingCurve, Qt , QThread , pyqtSignal , QUrl 
from PyQt5.QtWidgets import (
    QApplication,QWidget , QHBoxLayout,QVBoxLayout , QFrame, 
    QLabel,QFileDialog

)

from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEngineProfile
from PyQt5.QtCore import QUrl 
from qframelesswindow.webengine import FramelessWebEngineView 

from qfluentwidgets import (
    FluentWindow , SplashScreen
)
import sys


from qfluentwidgets import FluentIcon as FIF

class HomeWidget(QWidget):
    def __init__(self, text: str, parent=None , url:str=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = QWebEngineView(self)

        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)

        self.browser.load( QUrl("http://localhost:47971/"))

        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.on_downloadRequested)


    def on_downloadRequested(self, download):
        downloadPath = QFileDialog.getSaveFileName(self, "Save File", download.path())[0]
        if downloadPath:
            download.setPath(downloadPath)
            download.accept()


class NewWindow(QWidget):
    def __init__(self , data:dict):
        super().__init__()

        title = "data['model']"
        url = "data['url']"
        url = "https://www.facebook.com"

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = QWebEngineView(self)

        self.browser.load( QUrl( url ) )

        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)


        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.on_downloadRequested)



        self.setWindowIcon(QIcon("App/icons/bxs-edit-alt.svg"))
        self.setWindowTitle(title)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize(int(w*0.9) , int(h*0.9) )
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)    

        self.setMinimumHeight( int(h/2.5) )
        self.setMinimumWidth( int(w/2.5) )


    def on_downloadRequested(self, download):
        downloadPath = QFileDialog.getSaveFileName(self, "Save File", download.path())[0]
        if downloadPath:
            download.setPath(downloadPath)
            download.accept()