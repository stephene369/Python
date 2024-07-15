import socket
import json
from pathlib import Path
import subprocess as sb
import os
from print_color import print
from colorama import init

init()

ze = os.getlogin()
zender = f"c:/Users/{ze}/.zender"
zender = f"J:/.zender"
os.makedirs(zender,exist_ok=True)

class Receive :
	def __init__(self) : 
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
		# Defining Socket
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host,self.port))

		# Establishing Connections

	def get_setting(self) : 
		with open("setting.json","wb") as js :
			print("Receiveing setting : ")
			while True : 
				self.setting = self.sock.recv(1000)
				if self.setting == b"stephenew36@gmail.com" :
					print("End to get setting ",color='red')
					break
				js.write(self.setting)
		print("Setting received")

	def receive(self,destination:Path) :
		# Receiving File Data
		self.destination = destination
  
		print("\n\nReceving file : ")
		with open("setting.json","r") as js :
			setting = json.load(js)
   
		try :
			for root in setting.get('root'):
				R = Path(destination).joinpath(root)
				
				if not Path(R).exists() : 
					Path(R).mkdir(exist_ok=True)
					print(f"Creating {R}")
				else :
					print("\nPath exists . !")
		except Exception as e : print(e) 
  
		input("Tape anykey to continue : ")

		filenames = setting['filename']
		total = len(filenames) ; i = 0 
		for filename in filenames :
			i+=1
			filename=destination.joinpath(filename)
			file = open(filename, "wb") 
			print(f"\nWritting {filename}")
			while True :
				data = self.sock.recv(1500)
				if data==b"stephenew36@gmail.com" :
					print(f"Fin d'ecriture de {filename}" , color = 'green')
					break
				file.write(data)
			print(f"Data recived : {i} / {total}",color='red')
			file.close()

Rec = Receive()

Ip = Rec.get_IpAdress(ty='client')
if Ip:
	octHote = input("Entrer le nombre qui s'affiche chez le server : ..  ")
	Ip = f'{Ip}.{octHote}'
	print(f"Connection a : ... {Ip}",color='blue')
	print(f"Connecter `a {socket.gethostbyaddr(Ip)} \n" , color='red')
	
	Rec.connection(host=Ip,port=2003)
	while True :
		inp = input("Press any key to receive Data or 'q' to quit : ")
		if inp!='q':
			Rec.get_setting()
			Rec.receive(destination=Path(zender))
		else  :
			break 

   
