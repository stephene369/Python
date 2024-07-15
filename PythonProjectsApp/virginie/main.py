from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from nav import Ui_Form
import sys

class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super (moWidget, self).__init__()
    def moussePressEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def moussePressEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition) 
            event.accept()                  

class navVirginieApp(moWidget, Ui_Form):
    def __init__(self):
        super(navVirginieApp, self).__init__()
        self.setupUi(self)
        self.pushutton.clicked.connect(self.showMinimized)
        self.pushutton_3.clicked.connect(self.showMaximized)
        self.pushutton_2.clicked.connect(sys.exit)
        self.lineEdit.returnPressed.connect(self.load)
        self.pushutton_4.clicked.connect(self.backward)
        self.pushutton_5.clicked.connect(self.forward)
        self.pushutton_6.clicked.connect(self.reload)
        
    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)
            
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)
        
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
        
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
        
        
    
    def winShowMaximized(self):
        if self.pushButton_3.isChecked():
            self.widget.setStyleSheet("QWidget#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))border : 0px solid rgb(45, 45, 45);border-radius:0px;}")
            self.showMaximized()
        else:
            self.widget.setStyleSheet("QWidget#widget{border : 4px solid rgb(45, 45, 45);border-radius:20px;}")
            self.showMaximized()
            self.showNormal()
        
app = QtWidgets.QApplication(sys.argv)
Form = navVirginieApp()
Form.show()
sys.exit(app.exec_())
       