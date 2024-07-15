import socket
from tkinter import filedialog 
import tkinter as tk
from print_color.print_color import print 
from pathlib import Path
import os
from time import sleep
import json
root = tk.Tk()
root.withdraw()


class Server : 

    def __init__(self) -> None:
        self.host = self.get_local_ip_address()
        self.port = 20030

        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.bind((self.host, self.port))
        

    def get_local_ip_address():
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
    

    def accept_connection(self , nbclients:int) : 
        
        self.sock.listen(nbclients) 
        self.Clients  = []
        
        for i in range(nbclients) : 
            conn = self.sock.accept()
            self.Clients.append(conn)
            print("Connected to : ",conn[1],color='green')

    def get_file_settings(self  , type_:str) : 
        """
        type_ : WHAT DO YOU WANT TO SEND 
        [FILES or FOLDER]
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

            data = { 'root':[] , 'filename':{} ,"origin":[]}

            for root,_,files in os.walk(chemin) :
                relative = os.path.relpath(root,chemin)
                relative = str(Path(name).joinpath(relative))
                data['root'].append(relative )

                for file in files :
                    f=Path(file)
                    f=str(Path(relative).joinpath(f.name))
                    data['filename'].update({ f:os.path.getsize(str(Path(root).joinpath(file))) }) 
                    data['origin'].append(str(Path(root).joinpath(file)))

        with open("settings/setting.json",'w') as js :
            js.write( json.dumps( data,indent=4 ) )


    def send_settings(self) :
        for client in self.Clients : 
            with open("settings/setting.json",'rb') as js :
                print(f"Sending setting to {client[1]}")
                
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
    
    def send_files(self) :
        #Reading file and sending data to server
        with open("settings/settings.json","r") as js :
            data = json.load(js)
            self.filesPath = data['origin']

        total = len(self.filesPath) ; i = 0
        for filename in self.filesPath :
            i+=1

            file = open(filename, "rb")
            for client in self.Client :
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

    def close(self) :
        self.sock.close()
        return None