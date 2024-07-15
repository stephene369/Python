#import modules
from cgi import test
from tkinter import *
import os

# function define
def shutdown():
    return os.system("shutdown /s /t 90")

def restart():
    return os.system("shutdown /r /t 90")

def logout():
    return os.system("shutdown -l")

def hibernation():
    return os.system("shutdown /h")

def toCancel():
    return os.system("shutdown /a")

def closeApp():
    return os.system("shutdown /f")

# tkinter objets
master = Tk()

master.configure(bg='red')

# button 
Button(master , text = "Eteindre" , command=shutdown).grid(row = 1)
Button(master , text = "Redemarer" , command=restart).grid(row = 4)
Button(master , text="Deconnexion" , command=logout).grid(row=8)
Button(master , text="Cancel", command=toCancel).grid(row=12)
mainloop() 