from genericpath import exists
from importlib.resources import path
import os

# directory
directory=os.getlogin()

# parent Directory path
parentDir="G:\\ledossier"
isExist=os.path.exists(parentDir)

if (isExist==True):
    path=os.path.join(parentDir , directory )
    os.makedirs(path ,exist_ok=False)

