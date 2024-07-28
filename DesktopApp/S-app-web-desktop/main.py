""" 
coding:utf-8
# By Stephene WANTCHEKON

### GITHUB : 
https://github.com/stephene369


### INSTAGRAM : 
https://www.instagram.com/stephene.nk/


### FACEBOOK : 
https://www.facebook.com/stephene.wantchekon/


### LINKEDIN : 
https://www.linkedin.com/in/stephene-wantchekon-b13322252/


### coding:utf-8
# """

from Ui.lib import *  
from Ui.window import Window 


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()





