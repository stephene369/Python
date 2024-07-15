import sys

from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal,QSize,QEasingCurve,QRectF,QTimer,QEventLoop
from PyQt5.QtGui import QIcon, QDesktopServices,QPixmap,QPainter,QPainterPath,QColor,QBrush,QFont
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout , QVBoxLayout , 
                             QFileDialog , QStackedWidget , QWidget,
                             QGridLayout,QSpinBox,QSizePolicy,QScrollArea ,
                             QTextEdit,QTableWidgetItem,QLabel)
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, isDarkTheme,Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, BodyLabel, StrongBodyLabel, PushButton ,
                            BodyLabel, StateToolTip,SubtitleLabel,SmoothScrollArea,
                            OpacityAniStackedWidget,PopUpAniStackedWidget,TitleLabel,
                            ComboBox,DateEdit,CaptionLabel,SpinBox,PixmapLabel,TextEdit,
                            LineEditButton,LineEdit,TableWidget,Flyout,InfoBarIcon,SimpleCardWidget,
                            SimpleCardWidget,HyperlinkLabel,PrimaryPushButton,
                            VerticalSeparator,PillPushButton,TransparentToolButton,
                            FluentIcon,ImageLabel,SplashScreen,FluentStyleSheet)


from qfluentwidgets import FluentIcon as FIF 
from pathlib import Path
from time import sleep
from threading import *

from numpy import linspace
import numpy as np

import matplotlib.pyplot as plt
from pandas import read_csv , DataFrame , read_sql
import pandas.core.series

from PIL import Image

import sqlite3 as sql

from random import randint

CENTER = Qt.AlignmentFlag.AlignCenter
BOTTOM = Qt.AlignmentFlag.AlignBottom
LEFT = Qt.AlignmentFlag.AlignLeft
RIGHT = Qt.AlignmentFlag.AlignRight
TOP = Qt.AlignmentFlag.AlignTop
VCENTER = Qt.AlignmentFlag.AlignVCenter
HCENTER = Qt.AlignmentFlag.AlignHCenter




### 
# coding:utf-8
from typing import Union
from PyQt5 import QtGui

from PyQt5.QtCore import Qt, QSize, QRectF, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsDropShadowEffect

from qfluentwidgets.common.icon import FluentIconBase, drawIcon, toQIcon
from qfluentwidgets import IconWidget
from qframelesswindow import TitleBar

import qtawesome as qta

class SplashScreenImage(QWidget):
    """ Splash screen """

    def __init__(self, icon: Union[str, QIcon, FluentIconBase], parent=None, enableShadow=True):
        super().__init__(parent=parent)

        self._icon = icon
        self._iconSize = QSize(300, 300)

        self.titleBar = TitleBar(self)
        self.iconWidget = ImageLabel(icon, self)
        self.shadowEffect = QGraphicsDropShadowEffect(self)

        self.iconWidget.setFixedSize(self._iconSize)
        self.shadowEffect.setColor(QColor(0, 0, 0, 0))
        self.shadowEffect.setBlurRadius(15)
        self.shadowEffect.setOffset(0, 0)
        
        self.vbox = QVBoxLayout(self)
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.iconWidget, 0,CENTER|CENTER)

        FluentStyleSheet.FLUENT_WINDOW.apply(self.titleBar)

        if enableShadow:
            self.iconWidget.setGraphicsEffect(self.shadowEffect)

        if parent:
            parent.installEventFilter(self)

    def setIcon(self, icon: Union[str, QIcon, FluentIconBase]):
        self._icon = icon
        self.update()

    def icon(self):
        return toQIcon(self._icon)

    def setIconSize(self, size: QSize):
        self._iconSize = size
        self.iconWidget.setFixedSize(size)
        self.update()

    def iconSize(self):
        return self._iconSize

    def setTitleBar(self, titleBar: QWidget):
        """ set title bar """
        self.titleBar.deleteLater()
        self.titleBar = titleBar
        titleBar.setParent(self)
        titleBar.raise_()
        self.titleBar.resize(self.width(), self.titleBar.height())

    def eventFilter(self, obj, e: QEvent):
        if obj is self.parent():
            if e.type() == QEvent.Resize:
                self.resize(e.size())
            elif e.type() == QEvent.ChildAdded:
                self.raise_()

        return super().eventFilter(obj, e)

    def resizeEvent(self, e):
        iw, ih = self.iconSize().width(), self.iconSize().height()
        self.iconWidget.move(self.width()//2 - iw//2, self.height()//2 - ih//2)
        self.titleBar.resize(self.width(), self.titleBar.height())

    def finish(self):
        """ close splash screen """
        self.close()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        # draw background
        c = 32 if isDarkTheme() else 255
        painter.setBrush(QColor(c, c, c))
        painter.drawRect(self.rect())
