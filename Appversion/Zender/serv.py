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



host = "198.168.0.142"
port = 2003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))


nbClient = 1
sock.listen(nbClient)

print(socket.gethostbyaddr(host),color='red')


Client = []
for i in range(nbClient) :
    print(f"En attente de connection :  ...")
    conn = sock.accept()
    Client.append(conn)
    print("Connected to : ",conn[1],color='green')


dialog = filedialog

def get_file_path( typ) :
    if typ=="files" :
        filesPath = dialog.askopenfilenames()
        setting = {
            'root':[],
            'filesnames':{ Path(file).name : os.path.getsize(file) for file in filesPath },
            "origin":list(filesPath)}
    
        with open("setting.json","w") as js :
            js.write( json.dumps(setting,indent=4) )

    else :

        Path_ = dialog.askdirectory()
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


        with open("setting.json",'w') as js :
            js.write( json.dumps( data,indent=4 ) )

        
get_file_path('files')



for client in Client : 
    with open("setting.json", "rb") as js : 
        print("Senfing setting to ... ", client)

        while True : 
            setting = js.read()
            if not setting :
                sleep(2)
                setting = b"stephenew36@gmail.com"
                client[0].sendall(setting)
                print("Setting sent !")
                break
            else :
                client[0].sendall(setting)