from datetime import datetime
from json import load , dumps
from os import listdir , makedirs 


class recent :
    def __init__(self) :
        self.file_path = "data/recent.json"
        self.file_name = "recent.json"


    def read_(self) :
        makedirs("data",exist_ok=True)
        if self.file_name not in listdir(path="data") :
            file = open(self.file_path,"w")
            data = {"path":"." , "time":str(datetime.now())}
            file.write(dumps(data,indent=4))
            file.close()

        else :
            file = open(self.file_path,"r")
            data = load(file)
            file.close
            return data['path']

    def write_(self,dir:str) :
        data = {"path":dir , "time":str(datetime.now())}
        with open(self.file_path,"w") as file :
            file.write(dumps(data , indent=4))
            


