from PyQt5.QtWidgets import * 


class  Widow(QWidget) :
    def __init__(self) :
        super().__init__()


        self.show()


import sys
app = QApplication(sys.argv)
w = Widow()
app.exec_()
