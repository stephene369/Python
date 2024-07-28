from .lib import *
from .home import HomeWidget

class Window(FluentWindow):
    def __init__(self): 
        super().__init__()

        self.navigationInterface.setHidden(True)
        self.homeInterface = HomeWidget("Home" , self)
        self.addSubInterface(self.homeInterface, FIF.HOME , "Home")
    
 

