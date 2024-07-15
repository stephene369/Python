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


####################
####################
####################
####################

# CLIENT CODE

####################
####################
####################
####################


class Client : 
    def __init__(self) -> None:
        self.destination = os.path.join(os.path.expanduser("~"), "Zender")
        os.makedirs(self.destination , exist_ok=True)
        
    def connection(self,host:str) : 
        self.host = host
        self.port = 20030
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect( ( self.host , self.port ) )


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











####################
####################
####################
####################

# SERVER CODE

####################
####################
####################
####################



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

root = tk.Tk()
root.withdraw()


class Server : 
    def __init__(self) -> None:
        os.makedirs("settings" , exist_ok=True )
        self.host = self.get_local_ip_address()
        self.port = 20030

        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.bind((self.host, self.port))
        

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
            data["root"] = []
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



server = Server()
server.get_file_settings('folder')
server.close()


















## Server
import socket 

if __name__ == '__main__': 
	# Defining Socket 
	host = '127.0.0.1'
	port = 8080
	totalclient = int(input('Enter number of clients: ')) 

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	sock.bind((host, port)) 
	sock.listen(totalclient) 
	# Establishing Connections 
	connections = [] 
	print('Initiating clients') 
	for i in range(totalclient): 
		conn = sock.accept() 
		connections.append(conn) 
		print('Connected with client', i+1) 

	fileno = 0
	idx = 0
	for conn in connections: 
		# Receiving File Data 
		idx += 1
		data = conn[0].recv(1024).decode() 

		if not data: 
			continue
	# Creating a new file at server end and writing the data 
		filename = 'output'+str(fileno)+'.txt'
		fileno = fileno+1
		fo = open(filename, "w") 
		while data: 
			if not data: 
				break
			else: 
				fo.write(data) 
				data = conn[0].recv(1024).decode() 

		print() 
		print('Receiving file from client', idx) 
		print() 
		print('Received successfully! New filename is:', filename) 
		fo.close() 
	# Closing all Connections 
	for conn in connections: 
		conn[0].close() 






























## CLients
import socket 
# Creating Client Socket 
if __name__ == '__main__': 
	host = '127.0.0.1'
	port = 8080

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connecting with Server 
	sock.connect((host, port)) 

	while True: 

		filename = input('Input filename you want to send: ') 
		try: 
		# Reading file and sending data to server 
			fi = open(filename, "r") 
			data = fi.read() 
			if not data: 
				break
			while data: 
				sock.send(str(data).encode()) 
				data = fi.read() 
			# File is closed after data is sent 
			fi.close() 

		except IOError: 
			print('You entered an ')









