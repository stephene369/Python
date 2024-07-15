import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget Example')
        self.setGeometry(100, 100, 600, 400)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Index', 'Value'])

        self.addRows()

    def addRows(self):
        data = [('a', 'Apple'), ('b', 'Banana'), ('c', 'Cherry'), ('d', 'Date')]

        for row, (index, value) in enumerate(data):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(index))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableExample()
    window.show()
    sys.exit(app.exec_())
