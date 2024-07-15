from pandas import read_csv ,DataFrame
from PySide2.QtWidgets import QComboBox , QLabel
from folder import Chemin

def usersNamedb():
    try : 
        df = read_csv(Chemin('rootdb'))
        df0=df['username']
        df=read_csv(Chemin('usersdb'))
        for i in list(df['username']) :
            df0.loc[len(df0)]=i  
        return df0
    except Exception as e : print(e)

def dateLabeldb():
    df=read_csv(Chemin('datab_c'))
    df=df['Date']
    return df 


def generate(usersCombo : QComboBox 
    , dateCombo : QComboBox , label : QLabel) :
    try :
        usersName=usersCombo.currentText()
        date=dateCombo.currentText()
        database = Chemin('datab_c')
        df=read_csv(database)
        df=df[(df['Utilisateur']==usersName)&(df['Date']==date)]
        df=df.drop(columns=['Nom' , 'Sexe' , 'Heure'])
        somme=sum(df['Prix_Total'])
        directory_=f"{Chemin('db_version_path')}"+f"//{usersName}-"+f"{date.replace('/','-')}"
        
        label.setText(f"Le {date} , {usersName} a vendu pour "+"{:0,.0f}".format(somme)+" f ")
        df.to_csv(directory_ , index=False)
        return directory_
    except Exception as e : print(e)

