
import os
import sys

import PySide2.QtGui
from PySide2.QtWebEngine import QtWebEngine
from nav2 import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.minimizBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximizBtn.clicked.connect(self.max_min)
        self.ui.closeBtn.clicked.connect(lambda : self.close())

        self.ui.webEngine = QtWebEngine()
        
        self.show() 

    

    def max_min(self) :
        if self.isMaximized() == False :
            self.showFullScreen()
        elif self.isMaximized == True  :
            self.showNormal()
    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
