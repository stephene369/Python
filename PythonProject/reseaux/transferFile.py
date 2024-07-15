import socket 
import os 

sep='<SEPARATOR>'
buff=4096


host="192.168.8.117"

port = 50201

filname='data.csv'


filsize=os.path.getsize(filname)

s=socket.socket()

print(f'[+] connecting to {host}:port')
s.connect((host, port))

