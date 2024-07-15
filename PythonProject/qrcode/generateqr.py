import pyqrcode

link='www.geekforgeeks.com'

url = pyqrcode.create(link)

url.svg('myqrcode.svg',scale=10) 

url.png('myqrcode.png',scale=10 , module_color=(2,43,22,0))