from PySide2 import QtWidgets, QtCore

class AnimatedButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(AnimatedButton, self).__init__(parent)
        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)  # Durée de l'animation en millisecondes
        self.animation.setStartValue(QtCore.QRect(50, 50, 100, 30))  # Position et taille de départ du bouton
        self.animation.setEndValue(QtCore.QRect(200, 200, 100, 30))  # Position et taille finale du bouton

    def startAnimation(self):
        self.animation.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    button = AnimatedButton(window)
    button.setGeometry(50, 50, 100, 30)
    button.setText("Bouton animé")

    startButton = QtWidgets.QPushButton("Démarrer l'animation", window)
    startButton.clicked.connect(button.startAnimation)
    startButton.setGeometry(50, 100, 150, 30)

    window.show()

    app.exec_()




