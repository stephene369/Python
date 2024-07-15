import socket
from tkinter import filedialog 
import tkinter as tk
from print_color.print_color import print 
from pathlib import Path
import os
import subprocess as sb
from time import sleep
import json
init()

root = tk.Tk()
root.withdraw()

class Send :
    def __init__(self,wait:int=2) -> None:
        self.dialog = filedialog
        self.wait = wait
        pass

    def get_IpAdress(self,ty : str ) :
        result = sb.check_output('ipconfig | findstr "IPv4 Adress."',shell=True,text=True)
        result=result.split("\n")
        
        if len(result)==3 :
            ip = result[1].split(": ")[1]
            
        elif len(result)==2 :
            ip = result[0].split(": ")[1]

        else :
            return False
        
        if ty == 'client' :
            ip = ip.split('.')[:-1]
            return ".".join(ip)
        
        if ty == 'server' :
            return ip


    def connection(self,host,port) :
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host,self.port))

        self.nbClient = 1
        self.sock.listen(self.nbClient)

        print(socket.gethostbyaddr(self.host),color='red')

        self.Client = []
        for i in range(self.nbClient) :
            print(f"En attente de connection :  ...")
            self.conn = self.sock.accept()
            self.Client.append(self.conn)
            print("Connected to : ",self.conn[1],color='green')
        


    def get_file(self) :
        self.filesPath = self.dialog.askopenfilenames()
        self.filenames = [ Path(file).name for file in self.filesPath ]
 
    def get_dir(self) :
        self.Path_ = self.dialog.askdirectory()
   
    def send_setting(self) :
        self.setting = {
            'filename':self.filenames,
            'type':"",
            "size":3}

        with open("setting.json","w") as js :
            js.write( json.dumps(self.setting,indent=4) )

        for client in self.Client: 
            with open("setting.json",'rb') as js :
                print(f"Sending setting to {client[1]}")
                
                while True :
                    setting = js.read(1000) 
                    if not setting :
                        sleep(2)
                        setting = b"stephenew36@gmail.com"
                        client[0].sendall(setting)
                        print("Setting sent !")
                        break
                    else :
                        client[0].sendall(setting)

    def send_dirs_setting(self) :
        print("ENc",color='red')
        chemin = self.Path_
        name = Path(chemin).name

        data = { 'root':[] , 'filename':[] ,"completePath":[] , "size":[]}

        for root,dirs,files in os.walk(chemin) :
            relative = os.path.relpath(root,chemin)
            relative = str(Path(name).joinpath(relative))
            data['root'].append(relative )

            for file in files :
                f=Path(file)
                f=str(Path(relative).joinpath(f.name))
                data['filename'].append(f) 
                data['size'].append( os.path.getsize(str(Path(root).joinpath(file))) )
                data['completePath'].append(str(Path(root).joinpath(file)))


        with open("setting.json",'w') as js :
            js.write( json.dumps( data,indent=4 ) )

        for client in self.Client: 
            with open("setting.json",'rb') as js :
                print(f"Sending setting to {client[1]}")
                
                while True :
                    setting = js.read(1000) 
                    if not setting :
                        sleep(2)
                        setting = b"stephenew36@gmail.com"
                        client[0].sendall(setting)
                        print("Setting sent !")
                        break
                    else :
                        client[0].sendall(setting)
        
        with open('setting.json','r') as js :
            re = json.load(js)
            self.filesPath = re['completePath']

    def send_files(self) :
        #Reading file and sending data to server
        total = len(self.filesPath) ; i = 0
        for filename in self.filesPath :
            i+=1
            file = open(filename, "rb")
            for client in self.Client :
                print(f"\nSending {filename} to {client[1]}")
                while True :
                    self.data = file.read(1500)
                    if not self.data:
                        sleep(self.wait)
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


temps = int(input("Duree d'attente en seconde : ")) 
while temps <=1 :
    temps = int(input("Duree d'attente en seconde : ")) 
step = Send(temps)
step

IP = step.get_IpAdress(ty='server')


if IP :
    print(f"\nNumero a donner au client : {IP.split('.')[-1:]}",tag=f"{IP.split('.')[-1:]}",color='blue',tag_color='purple')
    step.connection(host=IP,port=2003)

    while True :
        inp = input("Press 1 for send file or else for send Dir or 'q' to quit : .. ")
        if inp =='1':
            step.get_file()
            step.send_setting()
            input("Press Any key to continu ")
            sleep(2)
            step.send_files()
            step.close()
        
        elif inp=='q' :
            step.close()
            break

        else :
            step.get_dir()
            step.send_dirs_setting()
            input("Press Any key to continu : ")
            sleep(2)
            step.send_files()
else : 
    print("Vous etes pas connecter a un reseau local ")







