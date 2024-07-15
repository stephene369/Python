import socket
import json
from pathlib import Path
import subprocess as sb
import os
from print_color import print


class Client : 
    def __init__(self) -> None:
        self.destination = os.path.join(os.path.expanduser("~"), "Zender")
        os.makedirs(self.destination , exist_ok=True)
        
    def connection(self,host:str) : 
        self.host = host
        self.port = 20030
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect( ( self.host , self.port ) )
        
    def get_settings(self) : 

        with open("setting.json","wb") as js :
            print("Receiveing setting : ")
            
            while True : 
                self.setting = self.sock.recv(1024)
                if self.setting == b"stephenew36@gmail.com" :
                    print("End to get setting ",color='green')
                    break

                js.write(self.setting)
        print("Setting received")


    def receive(self) : 

        with open("settings/settings.json","r") as js : 
            settings = json.load(js)

        ## creating dictionary if receiving directory 
        for root in settings['root'] : 
            r = Path(self.destination).joinpath(root)

            if Path(r).exists() == True :
                Path(r).mkdir(exist_ok=True)

            else :
                pass 

            
