from UI.navigation import *
from PyQt5.QtWidgets import QWidget


class WINDOW(Window):
    def __init__(self) :
        super().__init__()
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width() , desktop.height()
        self.resize(int(desktop.width()*0.90) , desktop.height())
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


if __name__ == '__main__':
    print("application")
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    #setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    print("application")
    w = WINDOW()
    print("application")

    w.show()
    app.exec_()
    print("application")
