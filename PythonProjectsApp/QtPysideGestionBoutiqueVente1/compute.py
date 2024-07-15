from folder import Chemin
from pandas import read_csv
from PySide2.QtWidgets import QLineEdit

def Cumule(lineEdit : QLineEdit) :
    try : 
        df=read_csv(Chemin('datab_liste_article'))
        liste_prix=list(df['Prix Total'])
        cumule=sum(liste_prix)
        val="{:0,.0f}".format(cumule)+"f"
        lineEdit.setText(val)
    except Exception as e : print(e.args)


def dropNa(data : str) :
    df=read_csv(data)
    df=df.dropna()
    df.to_csv(data,index=False)

def lessValue(name : str ,value : int) :
    try : 
        df=read_csv(Chemin('datab_aritcle'))
        nbDispo=int(df[df['Designation']==name.capitalize()]['Disponible'])
        df.loc[df['Designation']==name,'Disponible']=(nbDispo-value)
        df.to_csv(Chemin('datab_aritcle'),index=False)
    except Exception as e : print(e.args)

