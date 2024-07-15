# coding:utf-8
import sys
from PyQt5.QtCore import QEasingCurve, Qt , QThread , pyqtSignal
from PyQt5.QtGui import QPixmap , QFont , QIcon
from PyQt5.QtWidgets import QFrame , QVBoxLayout , QHBoxLayout
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import (SmoothScrollArea, PixmapLabel, widgets , 
TitleLabel , SubtitleLabel, ComboBox , 
TransparentPushButton,BodyLabel, CaptionLabel,
StateToolTip, InfoBarPosition 
, InfoBar , FluentWindow , 
NavigationAvatarWidget ,NavigationItemPosition ,
InfoBadgePosition,FluentBackgroundTheme,InfoBadge)

from qfluentwidgets import FluentIcon as FIF