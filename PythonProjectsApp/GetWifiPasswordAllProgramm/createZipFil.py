
from zipfile import ZipFile
import os


with ZipFile('zipFile/PasswordWifi.zip', 'w') as zObj: # 'w' or 'a'
    zObj.setpassword('23')
    path='C:\\Users\steph\\OneDrive\MesProjets\\Python\\Python_Files\\GetWifiPasswordAllProgramm\\file'
    listFile= os.listdir(path)
    
    for fName in listFile :
        filePath=f"{path}\\{fName}"
        zObj.write(filePath,fName)
        os.remove(filePath)
    zObj.close()      
os.removedirs(path)

