import socket , os , subprocess
from mss import mss

def scrennshot():
    with mss() as sct:
        sct.shot(output='screen.png')

s = socket