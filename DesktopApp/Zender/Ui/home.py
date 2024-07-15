from .lib import * 


class HomeWidget(SmoothScrollArea):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.Frame = QFrame(self)
        self.HBOX = QHBoxLayout(self)
        self.HBOX.addWidget(self.Frame)

        with open("resources/home.qss" , encoding='utf-8') as f : 
            self.setStyleSheet( f.read() )
        
        self.setObjectName(text.replace(' ', '-'))

        self.initInterface()
    
    def initInterface(self) : 
        self.sendButton = PushButton(FIF.SEND_FILL,"Send files")
        self.receiveButton = PushButton(FIF.DOWNLOAD,"Receive files")

        self.Frame_hbox = QHBoxLayout(self.Frame)
        self.Frame_hbox.addWidget(self.sendButton)
        self.Frame_hbox.addWidget(self.receiveButton)
