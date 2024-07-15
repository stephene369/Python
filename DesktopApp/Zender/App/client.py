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
import json
from pathlib import Path
import subprocess as sb
import os
from print_color import print
import subprocess
import platform

from PyQt5.QtCore import QObject, QThread , pyqtSignal , Qt 
from qfluentwidgets import InfoBarPosition , InfoBar 



class Client : 
    def __init__(self) -> None:
        self.destination = os.path.join(os.path.expanduser("~"), "Zender")
        os.makedirs(self.destination , exist_ok=True)


    def connection(self,host:str , parent) : 
        self.parent = parent
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.Worker_connection = WorkerTread_Connection(
            sock=self.sock , parent=self.parent , host=host )
        

        self.Worker_connection.message.connect(self.connectionConnect)
        self.Worker_connection.start()

    def connectionConnect(self,message) :
        if message == True : 
            self.createSuccessInfoBar()
            self.ReceiveFiles(
                sock=self.sock , 
                parent=self.parent )
            
        else : 
            self.createErrorInfoBar()
            print("Connection failed")

    def createErrorInfoBar(self):
        InfoBar.error(
            title='Error :',
            content="Can't etablish connection to server ...",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=-1,    # won't disappear automatically
            parent=self.parent
        )

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Success :',
            content="Connection etablished with the server ...",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.parent
        )



    def ReceiveFiles(self , sock , parent ) :
        self.Worker_ReceiveFiles = WorkerTread_Receive(
            sock=sock , parent=parent )
        
        #self.Worker_ReceiveFiles.message.connect(self.ReceiveFiles)
        self.Worker_ReceiveFiles.start()



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
            Path(r).mkdir(exist_ok=True)

        for filename in settings["filenames"] : 
            file = open( self.destination.join(filename) , "wb" )
            while True : 
                data = self.sock.recv(1024)
                if data == b"stephenew36@gmail.com":
                    break 
                file.write(data) 
            file.close()

    def close(self) : 
        self.sock.close()



class WorkerTread_Receive(QThread) : 
    message = pyqtSignal( dict )

    def __init__(self , sock:socket.socket , parent ) -> None:
        super().__init__()
        self.sock = sock
        self.parent_ = parent
        self.destination = os.path.join(os.path.expanduser("~"), "Zender")


    def run(self) :
        self.get_settings()
        self.receive()

    def connection(self,host:str) : 
        self.host = host
        self.port = 20030
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect( ( self.host , self.port ) )

    def get_settings(self) : 

        with open("settings/settings.json","wb") as js :
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
            Path(r).mkdir(exist_ok=True)

        for filename in settings["filenames"] : 
            filepath = Path(self.destination).joinpath(filename) 
            file = open( filepath , "wb" )
            while True : 
                data = self.sock.recv(1024)
                if data == b"stephenew36@gmail.com":
                    break 
                file.write(data) 
            file.close()

            self.createSuccessInfoBar(message=str(filepath))

    def createSuccessInfoBar(self, message):
        InfoBar.success(
            title='Received : ',
            content=message,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.parent_)
        


class WorkerTread_Connection(QThread) : 
    message = pyqtSignal( bool )

    def __init__(self , sock , parent, host) -> None:
        super().__init__() 
        self.sock = sock
        self.host = host
        self.port = 20030

    def run(self) :
        print("Running Connection Work")
        if self.connection() : self.message.emit(True)
        else : self.message.emit(False)


    def connection(self) : 
        try :    
            self.sock.connect( ( self.host , self.port ) )
            return True 
        except Exception as e :
            return False 