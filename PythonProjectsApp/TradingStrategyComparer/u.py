import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel

class ScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        scroll_area = QScrollArea(self)
        content_widget = QWidget()
        content_layout = QVBoxLayout()

        for i in range(20):
            label = QLabel(f"Label {i}")
            content_layout.addWidget(label)

        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)

        layout.addWidget(scroll_area)
        self.setLayout(layout)

        self.setWindowTitle('Scroll Area Example')
        self.setGeometry(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScrollAreaExample()
    ex.show()
    sys.exit(app.exec_())
