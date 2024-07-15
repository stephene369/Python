import socket
import json
from pathlib import Path
import subprocess as sb
import os
from print_color import print


host = "198.168.0.142"
port = 2003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))


def get_setting() : 
    with open("setting.json","wb") as js :
        print("Receiveing setting : ")
        while True : 
            setting = sock.recv(1000)
            if setting == b"stephenew36@gmail.com" :
                print("End to get setting ",color='red')
                break
            js.write(setting)
    print("Setting received")
get_setting()