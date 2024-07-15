from pandas import read_csv , DataFrame 
from folder import Chemin
from PySide2.QtWidgets import QTableWidget  , QTableWidgetItem ,QHeaderView 
from PySide2.QtCore import Qt


def display(data: str , table : QTableWidget) :
    try :
        df=read_csv(data)
        table.setColumnCount(len(df.columns))
        table.setRowCount(len(df))
        
        for i in range(len(df)) :
            item=QTableWidgetItem(str(i))
            table.setVerticalHeaderItem(i , item)
        
        for j in range(len(df.columns)) :
            columns=list(df.columns)
            item=QTableWidgetItem(str(columns[j]))
            table.setHorizontalHeaderItem(j,item)
        
        for k in range(len(df)) :
            for l in range (len(df.columns)) :
                item=QTableWidgetItem(str(df.iloc[k][l]))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(k , l , item)      

        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

   
    except Exception as e : print(e)


def displayListe() :
    df={"Designation" : [] , "Nombre" : [] , "Prix Total" : []}
    df=DataFrame(df)
    df.to_csv(Chemin('datab_liste_article'),mode='w',index=False)
