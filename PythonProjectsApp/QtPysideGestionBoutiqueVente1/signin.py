import os
from compute import dropNa
from folder import Chemin
from pandas import read_csv , DataFrame 
from PySide2.QtWidgets import QLineEdit 

def root_signin(name : QLineEdit , password :QLineEdit , confirm : QLineEdit) :    
    try : 
        name=name.text()
        password=password.text()
        confirm = confirm.text()
        if password == confirm : 
            data=[[name , password]]
            coln=["username" , "password"]
            dataframe=DataFrame(data=data,columns=coln)
            direc=Chemin('rootdb')
            dataframe.to_csv(direc , mode='w' ,index=False)
        else :
            return ' '
        dropNa(Chemin('rootdb'))
    except Exception as e : print(e)
    
def defaulf_root(name : str , password : str):
    data=[[name , password]]
    coln=["username" , "password"]
    dataframe=DataFrame(data=data,columns=coln)
    direc=Chemin('rootdb')
    dataframe.to_csv(direc , mode='w' ,index=False)


def users_signin(name_ : QLineEdit , password_ :QLineEdit , confirm_ : QLineEdit) :
    try :
        name = name_.text()
        password=password_.text()
        confirm=confirm_.text()

        name_.setText('')
        password_.setText('')
        confirm_.setText('')

        if password==confirm :
            data=[[name , password]]
            coln=["username" , "password"]
            dataframe=DataFrame(data=data,columns=coln)
            direc=Chemin('usersdb')
            if not os.path.exists(direc) :
                dataframe.to_csv(direc , mode='w' , index=False)
                print('creation et insertion')
            else :
                df=read_csv(direc)
                user=df[df['username']==name]
                if len(user) == 0 :
                    print('addition')
                    dataframe.to_csv(direc , mode='a' , header=False , index=False)
                elif len(user) >=1 :
                    print('exist deja')
                    return 0
            
        else : 
            return " "
        dropNa(Chemin('usersdb'))
    except Exception as e : print(e) 