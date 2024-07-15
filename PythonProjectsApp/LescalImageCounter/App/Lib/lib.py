import sys
from random import randint

from PyQt5.QtWidgets import (QWidget,QVBoxLayout,QHBoxLayout,
    QApplication,QGraphicsDropShadowEffect,QFrame,QSizePolicy,
    QFileDialog)

from PyQt5.QtCore import (Qt,QSize,QEvent,QEventLoop,QTimer,QUrl,QPoint,
                    pyqtProperty,pyqtSignal,QThread)
from PyQt5.QtGui import (QIcon,QColor,QPainter,QDesktopServices,
                QFont,QRegion,QPainterPath)

from qfluentwidgets import (SplashScreen,SplitFluentWindow,
    SmoothScrollArea,FluentIconBase,ImageLabel,TitleLabel,
    FluentStyleSheet,isDarkTheme,MessageBox,NavigationAvatarWidget,
    NavigationItemPosition,SingleDirectionScrollArea,SimpleCardWidget,
    PrimaryPushButton,HyperlinkLabel,CaptionLabel,
    BodyLabel,setFont,VerticalSeparator,PillPushButton,RoundMenu,Action,FluentIcon,
    PushButton,IconWidget,TransparentToolButton,CardWidget,InfoBarPosition,
    InfoBar,IndeterminateProgressRing)

from pathlib import Path

import json

from qfluentwidgets.common.icon import toQIcon
from qframelesswindow import TitleBar

import qtawesome  as qta
from typing import Union

from PIL import Image,ImageOps,ImageFile,ImageEnhance

from datetime import datetime

CENTER = Qt.AlignmentFlag.AlignCenter
BOTTOM = Qt.AlignmentFlag.AlignBottom
LEFT = Qt.AlignmentFlag.AlignLeft
RIGHT = Qt.AlignmentFlag.AlignRight
TOP = Qt.AlignmentFlag.AlignTop
VCENTER = Qt.AlignmentFlag.AlignVCenter
HCENTER = Qt.AlignmentFlag.AlignHCenter


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
        self.shadowEffect.setBlurRadius(60)
        self.shadowEffect.setOffset(20, 20)
        
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
