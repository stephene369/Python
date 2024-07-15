from PySide6.QtWidgets import QApplication
from Ui.Ui import * 
from sys import argv , exit
from json import dumps

class MainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi()

        with open("style/style.scss",'r') as sc :
            self.setStyleSheet(sc.read())

        self.show()


app = QApplication(argv)
Window = MainWindow()
exit(app.exec())


