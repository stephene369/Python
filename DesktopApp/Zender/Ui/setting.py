from .lib import *

class SettingWidget(SmoothScrollArea):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.Frame = QFrame(self)
        self.setWidget(self.Frame)

        with open("resources/settings.qss" , encoding='utf-8') as f : 
            self.setStyleSheet( f.read() )
        
        self.setObjectName(text.replace(' ', '-'))

