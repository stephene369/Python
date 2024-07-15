from PySide2.QtWidgets import QWidget , QStackedWidget , QLineEdit

def Conn(C, stack : QStackedWidget ,page : QWidget) :
    try : 
        if C [0]== "not connected" :
            return 0
        elif (C[0]=="connected") :
            stack.setCurrentWidget(page)
            return 0
    except Exception as e : print(e)

def logBtnConn(nameEd : QLineEdit , passEd : QLineEdit , stack : QStackedWidget , page : QWidget) :
    try : 
        nameEd.setText('')
        passEd.setText('')
        stack.setCurrentWidget(page)
    except Exception as e : print(e)
