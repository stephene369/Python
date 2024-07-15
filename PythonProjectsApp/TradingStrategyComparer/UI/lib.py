import sys

from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal,QSize,QEasingCurve
from PyQt5.QtGui import QIcon, QDesktopServices,QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout , QVBoxLayout , 
                             QFileDialog , QStackedWidget , QWidget,
                             QGridLayout,QSpinBox,QSizePolicy,QScrollArea ,
                             QTextEdit,QTableWidgetItem)
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, BodyLabel, StrongBodyLabel, PushButton ,
                            BodyLabel, StateToolTip,SubtitleLabel,SmoothScrollArea,
                            OpacityAniStackedWidget,PopUpAniStackedWidget,TitleLabel,
                            ComboBox,DateEdit,CaptionLabel,SpinBox,PixmapLabel,TextEdit,
                            LineEditButton,LineEdit,TableWidget,)
from qfluentwidgets import FluentIcon as FIF 
from pathlib import Path
from time import sleep
from threading import *

from numpy import linspace
import numpy as np

import matplotlib.pyplot as plt
from pandas import read_csv , DataFrame , core
import pandas.core.series


from PIL import Image

CENTER = Qt.AlignmentFlag.AlignCenter
BOTTOM = Qt.AlignmentFlag.AlignBottom
LEFT = Qt.AlignmentFlag.AlignLeft
RIGHT = Qt.AlignmentFlag.AlignRight
TOP = Qt.AlignmentFlag.AlignTop
VCENTER = Qt.AlignmentFlag.AlignVCenter
HCENTER = Qt.AlignmentFlag.AlignHCenter


class BackgroundThread(QThread):
    signal = pyqtSignal(str)

    def run(self):
        sleep(5)  # Simulate a time-consuming operation
        self.signal.emit("Thread finished sleeping.")

def startThread(self):
    thread = BackgroundThread()
    thread.start()
