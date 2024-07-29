from .lib import *

class HomeWidget(QWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))

        self.vBoxLayout = QVBoxLayout(self)   
        self.browser = QWebEngineView(self)
        
        self.server = Laucher()
        self.url = self.server.lauch()
        self.browser.load( QUrl(self.url) )

        self.setLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(3, 3, 3, 3)
        self.vBoxLayout.addWidget(self.browser)


        

