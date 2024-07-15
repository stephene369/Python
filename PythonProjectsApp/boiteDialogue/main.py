from sys import argv , exit
from Ui.ui import *


class MainWindow(QWidget) :
    def __init__(self) :
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()



if __name__ == "__name__" :
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())
else :
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())
    

