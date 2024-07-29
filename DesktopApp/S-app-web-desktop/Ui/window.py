"""
Stephene WANTCHEKON
===================
"""
from .lib import *
from .home import HomeWidget

class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle('PyQt-Fluent-Widgets')
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))

        self.vbox = QVBoxLayout(self)
        self.home = HomeWidget(parent=self , text="Home")

        self.addSubInterface(self.home ,FIF.HOME , "Home")
        self.navigationInterface.setHidden(True)
        

        self.show()
        self.initWindow(0)


        self.createSubInterface()
        self.initWindow(1)


        # close splash screen
        self.splashScreen.finish()

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(8000, loop.quit)
        loop.exec()


    def initWindow(self , s):
        if s==0 : 
            self.resize(700, 600)
            self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.setWindowTitle('PyQt-Fluent-Widgets')

            desktop = QApplication.desktop().availableGeometry()
            w, h = desktop.width(), desktop.height()
            self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        elif s==1 :
            self.resize(int(900*1.2), int(700*1.2))
            self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.setWindowTitle('PyQt-Fluent-Widgets')

            desktop = QApplication.desktop().availableGeometry()
            w, h = desktop.width(), desktop.height()
            self.move(w//2 - self.width()//2, h//2 - self.height()//2)    

            self.setMinimumHeight( int(h/2.5) )
            self.setMinimumWidth( int(w/2.5) )
