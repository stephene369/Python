# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import myressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget#widget{\n"
"	border : 4px solid rgb(45, 45, 45);\n"
"	border-radius:20px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 80))
        self.widget_3.setMaximumSize(QSize(16777215, 80))
        self.widget_3.setStyleSheet(u"QWidget#widget_2{\n"
"	background-color: rgb(195, 195, 195);\n"
"	border-top-left-radius:20px;\n"
"	border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"	background-color :rgba(0, 0, 0, 0);\n"
"	color: rgb(144, 144, 144);\n"
"	font:bold;\n"
"	font size:15px;\n"
"	font family : entypo;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:rgb(	142, 176, 27);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color:rgb(	91, 88, 53);\n"
"	padding-top : 5px;\n"
"	padding-left : 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(15, 15))
        self.label_6.setMaximumSize(QSize(15, 15))
        self.label_6.setStyleSheet(u"background-color:rgb(142, 176, 27);\n"
"border-radius:7px;")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(15, 15))
        self.label_5.setMaximumSize(QSize(15, 15))
        self.label_5.setStyleSheet(u"background-color:rgb(45, 45, 45);\n"
"border-radius:7px;")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(15, 15))
        self.label_4.setMaximumSize(QSize(15, 15))
        self.label_4.setStyleSheet(u"background-color:rgb(142, 176, 27);\n"
"border:4px solid rgb(45, 45, 45);\n"
"border-radius:7px;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.moveFrame = QFrame(self.widget_3)
        self.moveFrame.setObjectName(u"moveFrame")
        self.moveFrame.setFrameShape(QFrame.StyledPanel)
        self.moveFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.moveFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.moveFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16000, 16000))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"colour:rgb(144, 144, 144);\n"
"\n"
"background-color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 127);\n"
"background-color: rgb(89, 102, 52);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.moveFrame)

        self.minimizBtn = QPushButton(self.widget_3)
        self.minimizBtn.setObjectName(u"minimizBtn")
        self.minimizBtn.setMinimumSize(QSize(25, 25))
        self.minimizBtn.setMaximumSize(QSize(25, 25))
        self.minimizBtn.setStyleSheet(u":hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizBtn)

        self.maximizBtn = QPushButton(self.widget_3)
        self.maximizBtn.setObjectName(u"maximizBtn")
        self.maximizBtn.setMinimumSize(QSize(25, 25))
        self.maximizBtn.setMaximumSize(QSize(25, 25))
        self.maximizBtn.setStyleSheet(u":hover{\n"
"	background-color: rgb(203, 203, 203);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizBtn.setIcon(icon1)
        self.maximizBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.maximizBtn)

        self.closeBtn = QPushButton(self.widget_3)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(25, 25))
        self.closeBtn.setMaximumSize(QSize(25, 25))
        self.closeBtn.setStyleSheet(u":hover{\n"
"	background-color: rgba(255, 50, 35,0.8);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/window-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow-left-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(25, 25))
        self.pushButton_6.setMaximumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(25, 25))
        self.pushButton_5.setMaximumSize(QSize(25, 25))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        self.lineEdit.setStyleSheet(u"background-color:rgb(31,31,31);\n"
"border-radius:5px;\n"
"color : rgb(144, 144, 144);\n"
"padding-left:5px;")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.webEngine = QWidget(self.widget_2)
        self.webEngine.setObjectName(u"webEngine")
        self.webEngine.setStyleSheet(u"background-color:rgb(45, 45, 45);\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(144, 144,144);")

        self.verticalLayout_2.addWidget(self.webEngine)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"background-color:rgb(45, 45, 45);\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(144, 144,144);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VirginieBROWSER", None))
        self.minimizBtn.setText("")
        self.maximizBtn.setText("")
        self.closeBtn.setText("")
        self.pushButton_4.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Developed by Virginie", None))
    # retranslateUi

