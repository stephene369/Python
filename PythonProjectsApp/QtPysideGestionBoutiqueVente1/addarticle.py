from PySide2.QtWidgets import QSpinBox , QLineEdit , QTableWidget  , QTableWidgetItem
from pandas import read_csv
from folder import Chemin


def insert_price(articl : QLineEdit , nombre : QSpinBox , 
        prix : QSpinBox) :
    try :
        article=articl.text()
        article=article.capitalize()
        nombre_=nombre.value()
        nombre_=int(nombre_)
        df=read_csv(Chemin('datab_aritcle'))
        prixUnitaire=df[(df['Designation']==article)]['PrixUnitaire']
        prixUnitaire=int(prixUnitaire)
        prixTotal=prixUnitaire*nombre_
        prix.setValue(prixTotal)
    except Exception as e : print(e.args)


def remove_row(row : int ) :
    try :
        df=read_csv(Chemin('datab_liste_article'))
        df=df.drop(row)
        df.to_csv(Chemin('datab_liste_article') , mode= 'w' , index=False)
    except Exception as e : print(e.args)

