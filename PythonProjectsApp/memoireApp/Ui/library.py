from PySide6.QtWidgets import (QWidget,QVBoxLayout,QHBoxLayout,
    QFrame,QPushButton,QLabel,QFileDialog , QScrollArea, 
    QGridLayout , QComboBox , QCheckBox , QGroupBox , QRadioButton , 
    QSizePolicy,QLineEdit,QSpinBox)
from PySide6.QtCore import Qt 
from PySide6.QtGui import QIcon  ,QPixmap, QPainter,QImage,QPicture
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import  (QMainWindow , QStackedWidget ,QGraphicsView,
       QGraphicsPixmapItem , QGraphicsScene,  )

from PIL import Image

from threading import Thread

from time import sleep

from concurrent.futures import ThreadPoolExecutor

from pandas import read_csv , DataFrame

import matplotlib.pyplot as plt
from numpy import linspace


HCENTER = Qt.AlignmentFlag.AlignHCenter
VCENTER = Qt.AlignmentFlag.AlignVCenter
CENTER = Qt.AlignmentFlag.AlignCenter
TOP= Qt.AlignmentFlag.AlignTop
LEFT = Qt.AlignmentFlag.AlignLeft
RIGHT = Qt.AlignmentFlag.AlignRight
BUTTOM = Qt.AlignmentFlag.AlignBottom

RECENT:QWidget


INDIX = 0
OBJECT = {}

keys = ["objetif" , 
        "tolerance" , 
        "horizon" , 
        " "
        ]
