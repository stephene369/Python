from PySide2.QtWidgets import QLineEdit , QSpinBox ,QComboBox 
from generatedb import usersNamedb , dateLabeldb

def  holder(lineEd : QLineEdit , texte : str) :
    lineEd.setPlaceholderText(texte)

def max(spin : QSpinBox) :
    spin.setMaximum(10000000)

def hidetexte(lineEdit: QLineEdit) :
    lineEdit.setEchoMode(QLineEdit.Password)

def usersComboItem(Combo : QComboBox):
    try : 
        df=usersNamedb()
        item=df
        item=list(item)
        Combo.addItems(item)

    except Exception as e :print(e)
    return 0

def dateComboItem(Combo : QComboBox) :
    try : 
        df=dateLabeldb()
        item=df.value_counts().index
        item=list(item)
        Combo.addItems(item)
    except Exception as e :print(e)
    return 0
