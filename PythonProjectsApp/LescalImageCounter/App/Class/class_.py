from ..Lib import *


class Window(SplitFluentWindow) :
    def __init__(self) :
        super().__init__()


class Widget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))


class ScrollArea(SmoothScrollArea) :
    def __init__(self, parent=None):
        super().__init__(parent)