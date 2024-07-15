import sys 
from interface_ui import *
from PySide2.QtPrintSupport import *

class MainWindow(QMainWindow) :

    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # navigation button
        self.ui.closeBTn.clicked.connect(self.close)
        self.ui.maximizBtn.clicked.connect(self.showMaximized)
        self.ui.minimizBtn.clicked.connect(self.showMinimized)


        ## url par defaut sur la page web
        self.ui.webViewer.setUrl(QUrl("http://google.com"))

        ## action quand lurl change
        self.ui.webViewer.urlChanged.connect(self.update_url_bar)
        ## quand le chargement est fini
        self.ui.webViewer.loadFinished.connect(self.update_title)
        
        
        ## buttion retour,avant et recharge
        self.ui.backBtn.clicked.connect(lambda: self.ui.webViewer.back)
        self.ui.forwardBtn.clicked.connect(lambda: self.ui.webViewer.forward)
        self.ui.refreshBtn.clicked.connect(lambda : self.ui.webViewer.reload)

        ## qund la recherche est valider
        self.ui.urlbar.returnPressed.connect(self.navigation_sur_urls)

        self.show()

        
    
    def update_title(self):
        title = self.ui.webViewer.page().title()
        self.setWindowTitle("% s - Virginie Navigateur" % title)
    
    def navigate_home(self) :
        self.ui.webViewer.setUrl(QUrl("http://www.google.com"))
    
    def navigation_sur_urls(self):
        q = QUrl(self.ui.urlbar.text())
        if q.scheme() == "" : 
            q.setScheme("http")
        self.ui.webViewer.setUrl(q)
    
    def update_url_bar(self,q : QUrl  ) :
        self.ui.urlbar.setText(q.toString())
        self.ui.urlbar.setCursorPosition(0)

if __name__ == '__name__' :
    app =  QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

else :
    app =  QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



