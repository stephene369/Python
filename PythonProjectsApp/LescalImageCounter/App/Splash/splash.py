from ..Lib import * 

class SplashInterface(SplashScreenImage) :
    def __init__(self ,icon, parent):
        super().__init__(icon=icon , parent=parent)
        
    def createSubInterface(self , val:int):
        loop = QEventLoop(self)
        QTimer.singleShot(val, loop.quit)
        loop.exec()
