from PySide2.QtWidgets import QLineEdit , QCompleter 
from folder import Chemin
from pandas import read_csv

def Completeur(lineEdit : QLineEdit ) :
    try : 
        df=read_csv(Chemin('datab_aritcle'))
        name=list(df['Designation'])
        liste=[]
        for l in name :
            liste.append(str(l).casefold())
        completer=QCompleter(liste)
        lineEdit.setCompleter(completer)
    except Exception as e : print(e)
    
def PriceCompleter(lineEdit : QLineEdit) :
    try : 
        df=read_csv(Chemin('datab_aritcle'))
        name=(list(df['Designation']))
        price = (list(df['PrixUnitaire']))
        liste=[]
        for l in zip (name , price) :
            liste.append(f'{str(l[0]).casefold()} : {str(l[1])}')
        completer=QCompleter(liste)
        lineEdit.setCompleter(completer)
    except Exception as e : print(e)

