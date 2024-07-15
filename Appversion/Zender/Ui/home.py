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
    
