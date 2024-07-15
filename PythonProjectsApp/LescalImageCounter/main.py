import typing
from App import * 

class Lauch(QApplication) :
    QApplication.setAttribute(
        Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    
    QApplication.setAttribute(
        Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)

        self.window = Main()
        
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width() , desktop.height()
        self.window.resize(int(desktop.width()*0.80) , desktop.height())
        self.window.move(w//2 - self.window.width()//2, h//2 - self.window.height()//2)


        self.window.show()
        
        
        self.exec_()

Lauch(argv=sys.argv)
    
