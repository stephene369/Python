import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

# Classe pour la nouvelle interface
class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nouvelle Interface")
        self.setGeometry(100, 100, 200, 100)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ceci est la nouvelle interface"))
        self.setLayout(layout)

# Classe pour l'interface principale
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Principale")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        self.button = QPushButton("Ouvrir Nouvelle Interface")
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        # Connexion du clic du bouton à la méthode pour ouvrir la nouvelle interface
        self.button.clicked.connect(self.open_new_window)
    
    def open_new_window(self):
        new_window = NewWindow()
        new_window.show()

# Initialisation de l'application PyQt5
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
