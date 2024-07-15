""" coding:utf-8

# By Stephene WANTCHEKON 

### GITHUB : 
https://github.com/stephene369


### LINKEDIN : 
https://www.linkedin.com/in/stephene-wantchekon-b13322252/


### FACEBOOK : 
https://www.facebook.com/stephene.wantchekon/


### INSTAGRAM : 
https://www.instagram.com/stephene.nk/

### coding:utf-8"""

import socket
from tkinter import filedialog 
import tkinter as tk
from print_color.print_color import print 
from pathlib import Path
import os
from time import sleep
import json
import platform
import subprocess


from PyQt5.QtCore import QObject, QThread , pyqtSignal , Qt 
from qfluentwidgets import InfoBarPosition , InfoBar 


root = tk.Tk()
root.withdraw()


class Server : 

    def __init__(self) -> None:
        os.makedirs("settings" , exist_ok=True )
        self.host = self.get_local_ip_address()
        self.port = 20030

        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.bind((self.host, self.port))

        self.Clients = []
        

    def currentWifi(self) : 
        o_system = platform.system()
        if o_system == "Windows" :
            pass 
        elif o_system == "Linux":
            try :
                wifi_name = str(subprocess.check_output(['iwgetid'])).split(":")[1].replace("\\n","").replace('"',"").replace("\\","")
                return wifi_name
            
            except Exception as e :
                print(e)
                return None


    def get_local_ip_address(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1", 1))
            ip_address = s.getsockname()[0]
        except Exception as e:
            print("Erreur lors de la récupération de l'adresse IP:", e)
            ip_address = None
        finally:
            s.close()
        
        return ip_address 
    

    def accept_connection(self ,sock ,nbclients:int) :

        self.Worker_Accept = WorkerThread_Accept(
            sock=sock , 
            nbClient=nbclients, )

        self.Worker_Accept.message.connect(self.getClients)
        self.Worker_Accept.start()

    
    def getClients(self , message) :
        self.Clients = message["clients"] 


    def get_file_settings(self  , type_:str) : 
        """
        Get the settings of the files to send.

        Parameters
        ----------
        type_ : What do you want to send : 
        `files`
        
        """

        self.dialog = filedialog
        data = {"root":[] , "filesname":{} , "origin":[] }

        if type_ == "files" : 
            filespath = self.dialog.askopenfilenames()
            data["root"] = filespath
            data["filesname"] = { Path(file).name : os.path.getsize(file) for file in filespath }
            data["origin"] = list(filespath)


        elif type_ == "folder" : 
        
            Path_ = self.dialog.askdirectory()
            chemin = Path_
            name = Path(chemin).name

            data = { 'root':[] , 'filenames':{} ,"origin":[]}

            for root,_,files in os.walk(chemin) :
                relative = os.path.relpath(root,chemin)
                relative = str(Path(name).joinpath(relative))
                data['root'].append(relative )

                for file in files :
                    f=Path(file)
                    f=str(Path(relative).joinpath(f.name))
                    data['filenames'].update({ f:os.path.getsize(str(Path(root).joinpath(file))) }) 
                    data['origin'].append(str(Path(root).joinpath(file)))

        with open("settings/settings.json",'w') as js :
            js.write( json.dumps( data,indent=4 ) )


    def send_settings(self, ) :
        self.Worker_SendSettings = WorkerThread_SendSettings(
            sock=self.sock,
            clients=self.Clients )
        
        self.Worker_SendSettings.message.connect(self.send_files)
        self.Worker_SendSettings.start()
 

    def send_files(self) :
        self.Worker_SendFiles = WorkerTread_SendFiles(
            clients=self.Clients)
        
        self.Worker_SendSettings.start()


    def close(self) :
        self.sock.close()
        return None




class WorkerThread_Accept(QThread):
    message = pyqtSignal(dict)
    def __init__(self , sock:socket.socket,nbClient:int):
        super().__init__()
        self.sock = sock
        self.nbClient = nbClient

        self.sock.listen(self.nbClient)
        self.Clients = []

    def run(self): 
        for i in range(self.nbClient):
            conn = self.sock.accept()
            self.Clients.append(conn)
            self.createSuccessInfoBar(conn=conn )
                
        self.message.emit( {"clients":self.Clients  } )
        
    def createSuccessInfoBar(self  , conn):
            InfoBar.success(
                title='Connected to : ',
                content=f"{conn}",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000
        )


class WorkerThread_SendSettings(QThread):

    message = pyqtSignal(dict)
    def __init__(self , sock:socket.socket,clients:list):
        super().__init__()
        self.sock = sock 
        self.clients = clients

    def run(self) : 
        for client in self.clients : 
            with open("settings/settings.json",'rb') as js :
                print(f"Sending setting to {client}")
                
                while True :
                    setting = js.read(1024) 
                    if not setting :
                        sleep(2)
                        setting = b"stephenew36@gmail.com"
                        client[0].sendall(setting)
                        print("Setting sent !")
                        break
                    else :
                        client[0].sendall(setting)

        sleep(4)
        self.message.emit({ "finiched":True })

 

class WorkerTread_SendFiles(QThread) : 
    message = pyqtSignal( dict )

    def __init__(self , clients) -> None:
        super().__init__()
        self.Clients = clients

    def run(self) : 
        with open("settings/settings.json","r") as js :
            data = json.load(js)
            self.filesPath = data['origin']

        total = len(self.filesPath) ; i = 0
        for filename in self.filesPath :
            i+=1

            file = open(filename, "rb")
            for client in self.Clients :
                print(f"\nSending {filename} to {client[1]}")
                while True :
                    self.data = file.read(1024)
                    if not self.data:
                        sleep(3)
                        self.data=b"stephenew36@gmail.com"
                        client[0].sendall(self.data)
                        break
        
                    else:
                        client[0].sendall(self.data)
                
            file.close()
            print(f"{file} : sent",color='green')
            print(f"{i} / {total}")