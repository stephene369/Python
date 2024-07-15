import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem 
from qfluentwidgets import TableWidget , theme 
from PyQt5.QtCore import Qt
import pandas as pd

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.df = pd.read_csv("BRVM-Financials.csv")

        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)
        
        self.tableWidget.setColumnCount(len(self.df.columns))
        self.tableWidget.setHorizontalHeaderLabels(list(self.df.columns))

        self.addRows()

    def addRows(self):
        data = [('a', 'Apple'), ('b', 'Banana'), ('c', 'Cherry'), ('d', 'Date')]
        print(type(self.df.iloc[2]))
        
        for i in range(len(self.df)):
            self.tableWidget.insertRow(i)
            for j in range(len(self.df.iloc[i])) :
                self.tableWidget.setItem( i , j , QTableWidgetItem(str(self.df.iloc[i][j] )) )
        
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.selectRow(0)
        

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    window = TableExample()
    window.show()
    sys.exit(app.exec_())

"""from UI.maStrategy import maStrategy 
from UI.Suport import Support
import pandas as pd 

df = pd.read_csv("BRVM-Financials.csv" , index_col="Date") 
df = df[0:200][["Close"]]

resistance = Support(df=df,col="Close")

resistance.support_resistance()

"""