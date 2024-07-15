from ..Lib  import * 
from ..Class import Widget

class SettingInterface(Widget) :
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

