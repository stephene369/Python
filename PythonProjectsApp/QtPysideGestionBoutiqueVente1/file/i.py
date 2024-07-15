import time
from PySide2.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, QTimer

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.setText(current_time)

app = QApplication()
window = QWidget()
window.setWindowTitle("Horloge numérique")

label = QLabel()
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 40px; color: blue")

layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()

timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)

app.exec_()
