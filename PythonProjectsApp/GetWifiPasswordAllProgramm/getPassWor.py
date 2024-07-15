from ctypes import sizeof
from distutils import errors
from importlib.resources import path
from msilib.schema import Directory
from posixpath import split
from re import I
import subprocess
from unittest import expectedFailure, result
from pkg_resources import resource_listdir

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
        
print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))

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


try:
    subprocess.check_output(['netsh', 'wlan', 'export','profile','TECNO F2 2','key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
except subprocess.CalledProcessError:
    print(" ")
