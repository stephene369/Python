from PySide2.QtWidgets import *
from PySide2.QtGui import *

def removeGrid(self) :
    for (C , T) in zip (range(1,(self.nbCircuit*3),3) , self.nb_Circuit) :
        for i in range(0 , T*4,4) :
            w = self.ui.tableWidget.cellWidget(4+i , C)
            self.ui.tableWidget.removeCellWidget(4+i , C )
            i = self.ui.tableWidget.item(4+i , C)
            w.deleteLater()
            print(w.layout(),i)
            #self.ui.tableWidget.update()
    
def circuitItem(self , n ) :
    item = QTableWidgetItem(f"Circuit {n}")
    item.setFont(QFont('Arial',13,True))
    #item.setBackgroundColor(QColor(127,127,0,30))
    item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.8))
    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    return item

def tronconItem(self , n) :
    item = QTableWidgetItem(f"Troncon {n}")
    item.setFont(QFont('Arial',13,True))
    item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.6))
    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    return item

def item(self , text:str) :
    item = QTableWidgetItem(f"{text}")
    item.setFont(QFont('Arial',13,False))
    item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.4))
    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    return item