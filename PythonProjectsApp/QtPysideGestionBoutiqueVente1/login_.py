from pandas import read_csv
from folder import Chemin
from PySide2.QtWidgets import QLineEdit , QLabel , QStackedWidget , QWidget
import os

def userslogin(C : list , nameEd : QLineEdit , passwEd : QLineEdit ,
     msg : QLabel , stack : QStackedWidget , page : QWidget) :
    name = nameEd.text()
    password=passwEd.text()
    nameEd.setText("")
    passwEd.setText("")
    try : 
        df = read_csv(Chemin('usersdb'))
        if not os.path.exists(Chemin('usersdb')) :
            msg.setText("Aucun utilisateur enregitrer")
            return 0
        else :
            user=df[(df['username']==name) & (df['password']==password)]
            if len(user) ==1:
            
                stack.setCurrentWidget(page)
                msg.setText(f"Connecte en tant que '' {name} '' ")
                return ['connected' , name]
            else :
                msg.setText("Mot de passe ou nom d utilisteur incorrect")
                return 2 
    except Exception as e : print(e ,'\nAucun Utilisateur Inscrit')
    
def rootlogin(C : list , nameEd : QLineEdit , passwEd : QLineEdit ,
     msg : QLabel , stack : QStackedWidget , page : QWidget) :
    try :
        df = read_csv(Chemin('rootdb'))
        name = nameEd.text()
        password=passwEd.text()
        nameEd.setText("")
        passwEd.setText("")
        if not os.path.exists(Chemin('rootdb')) :
            msg.setText("Aucun administrater enregitrer")
            return 0
        else :
            user=df[(df['username']==name) & (df['password']==password)]
            if len(user) ==1:
                stack.setCurrentWidget(page)
                msg.setText(f"Connecte en tant que '' {name} '' ")
                return ['connected' , name]
            else :
                msg.setText("Mot de passe ou nom d utilisateur incorrect")
                return 2
    except Exception as e : print(e)


