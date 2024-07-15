from PySide6.QtWidgets import *
import sys

app= QApplication([])

window = QMainWindow()
window.setGeometry(500,100,500,500)


button = QPushButton(window)
window.setCentralWidget(button)
button.setText("ve ver erve evve eev erv ")
button.clicked.connect(lambda : print("jai ete cliquer"))


window.show()
app.exec()