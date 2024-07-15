import zipfile
import os

class Zipper :
    def __init__(self,source:str) -> None:
        try : 
            zippath = os.path.splitext(source)[0]+".zip"
            
            if os.path.isdir(source) :
                self.zip_directory(directory_path=source,
                            zip_path=zippath)
            
            elif os.path.isfile(source) :
                self.zip_file(file_path=source,
                            zip_path=zippath)
        except  Exception as e : print(e)
        self.zippath = zippath


    def zip_directory(self,directory_path, zip_path):

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

            for root, dirs, files in os.walk(directory_path):

                for file in files:

                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))

    def zip_file(self,file_path, zip_path):

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

            zipf.write(file_path, arcname=os.path.basename(file_path))
