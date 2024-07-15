import os
import py7zr

try:
    os.makedirs('File7z' , exist_ok=True)
    try:
        with py7zr.SevenZipFile('py7zipFile/passArchive.7z' , 'w') as archive:
            path='File7z'
            archive.writeall(path , 'Passord')
            archive.close()
    except AttributeError:
        print("")
        
    with py7zr.SevenZipFile('py7zipFile/passArchive.7z' , 'a') as archive:
        fileName=os.listdir('file')
        for Name in fileName :     
            path='file'
            path=os.path.join(path,Name)
            archive.write(path , f"{path}\\{Name}")
        archive.close()
except AttributeError :
    print("")

