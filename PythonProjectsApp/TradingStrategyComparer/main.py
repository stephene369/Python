from UI.navigation import *
from PyQt5.QtWidgets import QWidget
from win32api import GetSystemMetrics , GetUserName

WIDTH_ = GetSystemMetrics(0);HEIGHT_ = GetSystemMetrics(1)
USER = GetUserName()

X = int(WIDTH_*0.20)
Y = int(HEIGHT_*0.05)
W = WIDTH_  - int(1.5*X)
H = HEIGHT_ - int(3*Y) 

class WINDOW(Window):
    def __init__(self) :
        super().__init__()
        self.setGeometry(X,Y,W,H)
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width() , desktop.height()
        self.resize(int(desktop.width()*0.90) , desktop.height())
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    #setTheme(Theme.DARK)
    app = QApplication(sys.argv)
    w = WINDOW()
    w.show()
    app.exec_()