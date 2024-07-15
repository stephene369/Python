# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceCQCMJzP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import interface.icons__rc as icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 537)
        MainWindow.setStyleSheet(u"*{\n"
"	border : none ;\n"
"	background-color: transparent;\n"
"	background : transparent;\n"
"	padding : 0 ;\n"
"	margin : 0 ;\n"
"	color : #fff;\n"
"	font: 11.5pt \"Yu Gothic UI Semilight\";\n"
"}\n"
"#centralwidget{\n"
"	border : 1px solid blue ;\n"
"	background-color : #262b34;\n"
"\n"
"}\n"
"#usersForm { \n"
"	border : 1px solid #050b74;\n"
"}#users {\n"
"	background-color: rgb(31, 31, 31);\n"
"	border : 1px solid #050b74;\n"
"}#formFrame {\n"
"	background-color: rgb(31, 31, 31);\n"
"	border : 1px solid #050b74;\n"
"}\n"
"#rootForm{\n"
"	border : 1px solid #050b74;	\n"
"}#root {\n"
"	background-color: rgb(31, 31, 31);\n"
"	border : 1px solid #050b74;\n"
"}\n"
"\n"
"#menuCont {	\n"
"	background-color: rgb(43, 49, 57);\n"
"}\n"
"#menuCont QPushButton{\n"
"	text-align : left ;\n"
"	padding : 2px;\n"
"}\n"
"#menuCont QPushButton:hover{	\n"
"	font: 11.5pt \"MS Sans Serif\";\n"
"	background-color: #767676 ;\n"
"	border : 0.4px solid red ;\n"
"}\n"
"QPushButton:on {\n"
"        background: qlineargradient(x1 : 0"
                        ", y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"QPushButton:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuConterner = QCustomSlideMenu(self.centralwidget)
        self.menuConterner.setObjectName(u"menuConterner")
        self.menuConterner.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.menuConterner)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menuCont = QCustomSlideMenu(self.menuConterner)
        self.menuCont.setObjectName(u"menuCont")
        self.menuCont.setMaximumSize(QSize(45, 16777215))
        self.menuCont.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.menuCont)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuHeader = QFrame(self.menuCont)
        self.menuHeader.setObjectName(u"menuHeader")
        self.menuHeader.setMaximumSize(QSize(50, 100))
        self.menuHeader.setFrameShape(QFrame.StyledPanel)
        self.menuHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menuHeader)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nano = QPushButton(self.menuHeader)
        self.nano.setObjectName(u"nano")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nano.sizePolicy().hasHeightForWidth())
        self.nano.setSizePolicy(sizePolicy)
        self.nano.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.212121 rgba(0, 3, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/nano.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nano.setIcon(icon)
        self.nano.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.nano)

        self.homeBtn = QPushButton(self.menuHeader)
        self.homeBtn.setObjectName(u"homeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/homeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.homeBtn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.menuHeader)

        self.menu = QFrame(self.menuCont)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formBtn = QPushButton(self.menu)
        self.formBtn.setObjectName(u"formBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/formIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.formBtn.setIcon(icon2)
        self.formBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.formBtn)

        self.tableBtn = QPushButton(self.menu)
        self.tableBtn.setObjectName(u"tableBtn")
        self.tableBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/tableDatabase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableBtn.setIcon(icon3)
        self.tableBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.tableBtn)

        self.articleBtn = QPushButton(self.menu)
        self.articleBtn.setObjectName(u"articleBtn")
        self.articleBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/listData.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.articleBtn.setIcon(icon4)
        self.articleBtn.setIconSize(QSize(32, 32))
        self.articleBtn.setCheckable(False)
        self.articleBtn.setChecked(False)
        self.articleBtn.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.articleBtn)

        self.changeBtn = QPushButton(self.menu)
        self.changeBtn.setObjectName(u"changeBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/7612772.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeBtn.setIcon(icon5)
        self.changeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.changeBtn)

        self.saveBtn = QPushButton(self.menu)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setStyleSheet(u"text-align : left ")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/Back_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon6)
        self.saveBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.saveBtn)


        self.verticalLayout.addWidget(self.menu)

        self.menuDown = QFrame(self.menuCont)
        self.menuDown.setObjectName(u"menuDown")
        self.menuDown.setFrameShape(QFrame.StyledPanel)
        self.menuDown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuDown)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 40)
        self.usersBtn = QPushButton(self.menuDown)
        self.usersBtn.setObjectName(u"usersBtn")
        self.usersBtn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/usersGroup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usersBtn.setIcon(icon7)
        self.usersBtn.setIconSize(QSize(31, 31))

        self.verticalLayout_4.addWidget(self.usersBtn)

        self.infosBtn = QPushButton(self.menuDown)
        self.infosBtn.setObjectName(u"infosBtn")
        self.infosBtn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/infosIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infosBtn.setIcon(icon8)
        self.infosBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.infosBtn)


        self.verticalLayout.addWidget(self.menuDown, 0, Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.menuCont)


        self.horizontalLayout.addWidget(self.menuConterner)

        self.centralFrame = QFrame(self.centralwidget)
        self.centralFrame.setObjectName(u"centralFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralFrame.sizePolicy().hasHeightForWidth())
        self.centralFrame.setSizePolicy(sizePolicy1)
        self.centralFrame.setFrameShape(QFrame.StyledPanel)
        self.centralFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.centralFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centralContener = QFrame(self.centralFrame)
        self.centralContener.setObjectName(u"centralContener")
        sizePolicy1.setHeightForWidth(self.centralContener.sizePolicy().hasHeightForWidth())
        self.centralContener.setSizePolicy(sizePolicy1)
        self.centralContener.setFrameShape(QFrame.StyledPanel)
        self.centralContener.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.centralContener)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.centralStacked = QStackedWidget(self.centralContener)
        self.centralStacked.setObjectName(u"centralStacked")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.loginPage.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.loginPage)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.loginSubPage = QStackedWidget(self.loginPage)
        self.loginSubPage.setObjectName(u"loginSubPage")
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.users.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.users)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.users)
        self.leftFrame.setObjectName(u"leftFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy2)
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.leftFrame)

        self.usersForm = QFrame(self.users)
        self.usersForm.setObjectName(u"usersForm")
        self.usersForm.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.usersForm.sizePolicy().hasHeightForWidth())
        self.usersForm.setSizePolicy(sizePolicy3)
        self.usersForm.setMinimumSize(QSize(0, 0))
        self.usersForm.setMaximumSize(QSize(700, 700))
        self.usersForm.setStyleSheet(u"*{lineedit-password-character : 1000}")
        self.usersForm.setFrameShape(QFrame.StyledPanel)
        self.usersForm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.usersForm)
        self.verticalLayout_10.setSpacing(35)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(50, 0, 50, 50)
        self.pushButton = QPushButton(self.usersForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(90, 90))

        self.verticalLayout_10.addWidget(self.pushButton)

        self.label = QLabel(self.usersForm)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"text-align : right ; ")

        self.verticalLayout_10.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setContentsMargins(-1, 10, -1, -1)
        self.userName = QLabel(self.usersForm)
        self.userName.setObjectName(u"userName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.userName)

        self.userPass = QLabel(self.usersForm)
        self.userPass.setObjectName(u"userPass")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.userPass)

        self.usersnameEd = QLineEdit(self.usersForm)
        self.usersnameEd.setObjectName(u"usersnameEd")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.usersnameEd)

        self.userspassEd = QLineEdit(self.usersForm)
        self.userspassEd.setObjectName(u"userspassEd")
        self.userspassEd.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.userspassEd)


        self.verticalLayout_10.addLayout(self.formLayout)

        self.usersMsg = QLabel(self.usersForm)
        self.usersMsg.setObjectName(u"usersMsg")

        self.verticalLayout_10.addWidget(self.usersMsg)

        self.usersConBtn = QPushButton(self.usersForm)
        self.usersConBtn.setObjectName(u"usersConBtn")

        self.verticalLayout_10.addWidget(self.usersConBtn)

        self.asRootBtn = QPushButton(self.usersForm)
        self.asRootBtn.setObjectName(u"asRootBtn")

        self.verticalLayout_10.addWidget(self.asRootBtn)


        self.horizontalLayout_6.addWidget(self.usersForm)

        self.rightFrame = QFrame(self.users)
        self.rightFrame.setObjectName(u"rightFrame")
        sizePolicy2.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy2)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.rightFrame)

        self.loginSubPage.addWidget(self.users)
        self.root = QWidget()
        self.root.setObjectName(u"root")
        sizePolicy3.setHeightForWidth(self.root.sizePolicy().hasHeightForWidth())
        self.root.setSizePolicy(sizePolicy3)
        self.root.setMaximumSize(QSize(16777215, 16777215))
        self.root.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.root)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.leftForm1 = QFrame(self.root)
        self.leftForm1.setObjectName(u"leftForm1")
        sizePolicy2.setHeightForWidth(self.leftForm1.sizePolicy().hasHeightForWidth())
        self.leftForm1.setSizePolicy(sizePolicy2)
        self.leftForm1.setMinimumSize(QSize(0, 0))
        self.leftForm1.setToolTipDuration(3)
        self.leftForm1.setStyleSheet(u"")
        self.leftForm1.setFrameShape(QFrame.StyledPanel)
        self.leftForm1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.leftForm1)

        self.rootForm = QFrame(self.root)
        self.rootForm.setObjectName(u"rootForm")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rootForm.sizePolicy().hasHeightForWidth())
        self.rootForm.setSizePolicy(sizePolicy4)
        self.rootForm.setMaximumSize(QSize(600, 800))
        self.rootForm.setStyleSheet(u"")
        self.rootForm.setFrameShape(QFrame.StyledPanel)
        self.rootForm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.rootForm)
        self.verticalLayout_11.setSpacing(35)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(50, 0, 50, 50)
        self.pushButton_2 = QPushButton(self.rootForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/rootusers.jfif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QSize(150, 120))

        self.verticalLayout_11.addWidget(self.pushButton_2)

        self.label_3 = QLabel(self.rootForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(30)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setContentsMargins(0, 10, 0, 0)
        self.label_4 = QLabel(self.rootForm)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.rootForm)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.rootnameEd = QLineEdit(self.rootForm)
        self.rootnameEd.setObjectName(u"rootnameEd")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.rootnameEd)

        self.rootpassEd = QLineEdit(self.rootForm)
        self.rootpassEd.setObjectName(u"rootpassEd")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.rootpassEd)


        self.verticalLayout_11.addLayout(self.formLayout_2)

        self.rootMsg = QLabel(self.rootForm)
        self.rootMsg.setObjectName(u"rootMsg")

        self.verticalLayout_11.addWidget(self.rootMsg)

        self.rootConBtn = QPushButton(self.rootForm)
        self.rootConBtn.setObjectName(u"rootConBtn")

        self.verticalLayout_11.addWidget(self.rootConBtn)

        self.asUsersBtn = QPushButton(self.rootForm)
        self.asUsersBtn.setObjectName(u"asUsersBtn")

        self.verticalLayout_11.addWidget(self.asUsersBtn)


        self.horizontalLayout_7.addWidget(self.rootForm)

        self.rightForm1 = QFrame(self.root)
        self.rightForm1.setObjectName(u"rightForm1")
        sizePolicy2.setHeightForWidth(self.rightForm1.sizePolicy().hasHeightForWidth())
        self.rightForm1.setSizePolicy(sizePolicy2)
        self.rightForm1.setMinimumSize(QSize(0, 0))
        self.rightForm1.setStyleSheet(u"")
        self.rightForm1.setFrameShape(QFrame.StyledPanel)
        self.rightForm1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.rightForm1)

        self.loginSubPage.addWidget(self.root)

        self.horizontalLayout_5.addWidget(self.loginSubPage)

        self.centralStacked.addWidget(self.loginPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.homePage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.scrollArea = QScrollArea(self.homePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 112, 72))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_12.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.centralStacked.addWidget(self.homePage)
        self.formPage = QWidget()
        self.formPage.setObjectName(u"formPage")
        self.verticalLayout_13 = QVBoxLayout(self.formPage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.formPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 687, 908))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_15 = QVBoxLayout(self.widget_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_15.addWidget(self.label_6, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_16 = QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Formulaire = QWidget()
        self.Formulaire.setObjectName(u"Formulaire")
        self.Formulaire.setStyleSheet(u"QWidget{\n"
"	background-color: ;\n"
"}\n"
"\n"
"QLabel{\n"
"	color : #fff;\n"
"	font-weight : 2000 ;\n"
"}\n"
"QLabel#heading{\n"
"	color: #4c4c4c ;\n"
"	font-size : 18 px ;\n"
"	margin-bottom : 10 px ;\n"
"}\n"
"QLabel#subheading{\n"
"	color: #0f1925 ;\n"
"	font-size : 12 px ;\n"
"	font-weight : normal ;\n"
"	margin-bottom : 10px ;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius : 7px ;\n"
"	border : 1px solid #e0e4e7 ;\n"
"}\n"
"QLineEdit:focus,\n"
"QSpinBox:focus\n"
"{\n"
"	border : 1px solid #1c3d70;\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color : #b3b3b3\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color : ;\n"
"	color : #fff ;\n"
"	border-radius : 7px ;\n"
"	border-left : 1px solid #1e4b87;\n"
"	border-right : 1px solid #1e4b87;\n"
"	border-bottom : 1px solid #1e4b87;\n"
"	border-top : 1px solid #1e4b87;\n"
"	padding : 1px 9px ;\n"
"	margin-top : 10 px ;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #a7a7a7;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left : 1px solid #1c3d70;\n"
"	border-right : "
                        "1px solid #1c3d70;\n"
"	border-bottom : 1px solid #1c3d70;\n"
"}\n"
"QPushButton:focus{\n"
"	border-left : 1px solid #1c3d70;\n"
"	border-right : 1px solid #1c3d70;\n"
"	border-top : 1px solid #1c3d70;\n"
"	border-bottom : 1px solid #1c3d70 ;\n"
"}\n"
"QSpinBox {\n"
"	background-color : ;\n"
"	color : #fff ;\n"
"	border-radius : 7px ;\n"
"	border-bottom : 1px solid #e0e4e7;\n"
"	padding : 1px 9px ;\n"
"	margin-top : 10 px ;\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.Formulaire)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.Formulaire)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(50)
        self.formLayout_4.setVerticalSpacing(60)
        self.formLayout_4.setContentsMargins(150, 20, 0, 30)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.nameEd = QLineEdit(self.frame_3)
        self.nameEd.setObjectName(u"nameEd")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.nameEd)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.maleRad = QRadioButton(self.frame_3)
        self.maleRad.setObjectName(u"maleRad")

        self.horizontalLayout_2.addWidget(self.maleRad)

        self.femaleRad = QRadioButton(self.frame_3)
        self.femaleRad.setObjectName(u"femaleRad")

        self.horizontalLayout_2.addWidget(self.femaleRad)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.articleCon = QLineEdit(self.frame_3)
        self.articleCon.setObjectName(u"articleCon")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.articleCon)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.nbArticle = QSpinBox(self.frame_3)
        self.nbArticle.setObjectName(u"nbArticle")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.nbArticle)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.prixTotal = QSpinBox(self.frame_3)
        self.prixTotal.setObjectName(u"prixTotal")

        self.verticalLayout_20.addWidget(self.prixTotal)

        self.addBtn = QPushButton(self.frame_3)
        self.addBtn.setObjectName(u"addBtn")

        self.verticalLayout_20.addWidget(self.addBtn)


        self.formLayout_4.setLayout(4, QFormLayout.FieldRole, self.verticalLayout_20)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.heureLab = QLabel(self.frame_3)
        self.heureLab.setObjectName(u"heureLab")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.heureLab)

        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.dateLab = QLabel(self.frame_3)
        self.dateLab.setObjectName(u"dateLab")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.dateLab)


        self.horizontalLayout_3.addLayout(self.formLayout_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tablelisteAchat = QTableWidget(self.frame_6)
        if (self.tablelisteAchat.columnCount() < 3):
            self.tablelisteAchat.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablelisteAchat.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablelisteAchat.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablelisteAchat.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablelisteAchat.setObjectName(u"tablelisteAchat")

        self.verticalLayout_19.addWidget(self.tablelisteAchat)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.deleteLineBtn = QPushButton(self.frame_7)
        self.deleteLineBtn.setObjectName(u"deleteLineBtn")
        self.deleteLineBtn.setStyleSheet(u":hover,:focus{border-radius : 7px ;\n"
"border-left : 1px solid #6a0707;\n"
"border-right : 1px solid #6a0707;\n"
"border-bottom : 1px solid #6a0707;\n"
"border-top : 1px solid #6a0707;}")

        self.horizontalLayout_8.addWidget(self.deleteLineBtn)

        self.lineNumber = QSpinBox(self.frame_7)
        self.lineNumber.setObjectName(u"lineNumber")

        self.horizontalLayout_8.addWidget(self.lineNumber)


        self.verticalLayout_19.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Formulaire)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(150, 0, 150, 10)
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_18.addWidget(self.lineEdit)

        self.saveMsg = QLabel(self.frame_4)
        self.saveMsg.setObjectName(u"saveMsg")

        self.verticalLayout_18.addWidget(self.saveMsg, 0, Qt.AlignBottom)

        self.saveFormBtn = QPushButton(self.frame_4)
        self.saveFormBtn.setObjectName(u"saveFormBtn")

        self.verticalLayout_18.addWidget(self.saveFormBtn)

        self.annulerFormBtn = QPushButton(self.frame_4)
        self.annulerFormBtn.setObjectName(u"annulerFormBtn")
        self.annulerFormBtn.setStyleSheet(u":hover,:focus{border-radius : 7px ;\n"
"border-left : 1px solid #6a0707;\n"
"border-right : 1px solid #6a0707;\n"
"border-bottom : 1px solid #6a0707;\n"
"border-top : 1px solid #6a0707;}")

        self.verticalLayout_18.addWidget(self.annulerFormBtn)

        self.otherBtn = QPushButton(self.frame_4)
        self.otherBtn.setObjectName(u"otherBtn")

        self.verticalLayout_18.addWidget(self.otherBtn)


        self.verticalLayout_17.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.Formulaire)
        self.Autre = QWidget()
        self.Autre.setObjectName(u"Autre")
        self.verticalLayout_21 = QVBoxLayout(self.Autre)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(30)
        self.formLayout_5.setVerticalSpacing(30)
        self.formLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.label_14 = QLabel(self.Autre)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.Autre)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.label_15)

        self.label_16 = QLabel(self.Autre)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.otherEd = QLineEdit(self.Autre)
        self.otherEd.setObjectName(u"otherEd")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.otherEd)

        self.label_17 = QLabel(self.Autre)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.otherPrice = QSpinBox(self.Autre)
        self.otherPrice.setObjectName(u"otherPrice")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.otherPrice)


        self.verticalLayout_21.addLayout(self.formLayout_5)

        self.saveOtherBtn = QPushButton(self.Autre)
        self.saveOtherBtn.setObjectName(u"saveOtherBtn")

        self.verticalLayout_21.addWidget(self.saveOtherBtn)

        self.backToFormBtn = QPushButton(self.Autre)
        self.backToFormBtn.setObjectName(u"backToFormBtn")

        self.verticalLayout_21.addWidget(self.backToFormBtn)

        self.stackedWidget.addWidget(self.Autre)

        self.verticalLayout_16.addWidget(self.stackedWidget)


        self.verticalLayout_14.addWidget(self.widget_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

        self.centralStacked.addWidget(self.formPage)
        self.articlePage = QWidget()
        self.articlePage.setObjectName(u"articlePage")
        self.verticalLayout_25 = QVBoxLayout(self.articlePage)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.articlePage)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 184, 229))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_26.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_26.addWidget(self.label_20)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.designationEd = QLineEdit(self.frame_5)
        self.designationEd.setObjectName(u"designationEd")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.designationEd)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.prixUnitaireEd = QSpinBox(self.frame_5)
        self.prixUnitaireEd.setObjectName(u"prixUnitaireEd")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.prixUnitaireEd)

        self.addArticleBtn = QPushButton(self.frame_5)
        self.addArticleBtn.setObjectName(u"addArticleBtn")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.addArticleBtn)

        self.cancelArticleBtn = QPushButton(self.frame_5)
        self.cancelArticleBtn.setObjectName(u"cancelArticleBtn")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.cancelArticleBtn)


        self.verticalLayout_27.addLayout(self.formLayout_6)


        self.verticalLayout_26.addWidget(self.frame_5)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_26.addWidget(self.tableWidget)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_25.addWidget(self.scrollArea_4)

        self.centralStacked.addWidget(self.articlePage)
        self.tablePage = QWidget()
        self.tablePage.setObjectName(u"tablePage")
        self.verticalLayout_22 = QVBoxLayout(self.tablePage)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.tablePage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy3.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 150, 145))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_23.addWidget(self.label_18)

        self.stackedWidget_2 = QStackedWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.dbPage = QWidget()
        self.dbPage.setObjectName(u"dbPage")
        self.verticalLayout_24 = QVBoxLayout(self.dbPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.moreInfos = QPushButton(self.dbPage)
        self.moreInfos.setObjectName(u"moreInfos")

        self.verticalLayout_24.addWidget(self.moreInfos)

        self.dataBase = QTableWidget(self.dbPage)
        self.dataBase.setObjectName(u"dataBase")

        self.verticalLayout_24.addWidget(self.dataBase)

        self.stackedWidget_2.addWidget(self.dbPage)
        self.dbPageInfo = QWidget()
        self.dbPageInfo.setObjectName(u"dbPageInfo")
        self.stackedWidget_2.addWidget(self.dbPageInfo)

        self.verticalLayout_23.addWidget(self.stackedWidget_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_22.addWidget(self.scrollArea_3)

        self.centralStacked.addWidget(self.tablePage)
        self.changePage = QWidget()
        self.changePage.setObjectName(u"changePage")
        self.verticalLayout_28 = QVBoxLayout(self.changePage)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.changePage)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 100, 30))
        self.label_23 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(60, 30, 47, 14))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_28.addWidget(self.scrollArea_5)

        self.centralStacked.addWidget(self.changePage)
        self.savePage = QWidget()
        self.savePage.setObjectName(u"savePage")
        self.centralStacked.addWidget(self.savePage)
        self.infosPage = QWidget()
        self.infosPage.setObjectName(u"infosPage")
        self.centralStacked.addWidget(self.infosPage)

        self.verticalLayout_9.addWidget(self.centralStacked)


        self.verticalLayout_6.addWidget(self.centralContener)

        self.sizeGrid = QFrame(self.centralFrame)
        self.sizeGrid.setObjectName(u"sizeGrid")
        self.sizeGrid.setStyleSheet(u"")
        self.sizeGrid.setFrameShape(QFrame.StyledPanel)
        self.sizeGrid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sizeGrid)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.msgLab = QLabel(self.sizeGrid)
        self.msgLab.setObjectName(u"msgLab")
        sizePolicy3.setHeightForWidth(self.msgLab.sizePolicy().hasHeightForWidth())
        self.msgLab.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.msgLab)

        self.sizegrid = QFrame(self.sizeGrid)
        self.sizegrid.setObjectName(u"sizegrid")
        self.sizegrid.setMinimumSize(QSize(30, 25))
        self.sizegrid.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.sizegrid.setFrameShape(QFrame.StyledPanel)
        self.sizegrid.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizegrid, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.sizeGrid, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.centralFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centralStacked.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nano.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
        self.formBtn.setText(QCoreApplication.translate("MainWindow", u"   Formulaire", None))
        self.tableBtn.setText(QCoreApplication.translate("MainWindow", u"   Table", None))
        self.articleBtn.setText(QCoreApplication.translate("MainWindow", u"   Article", None))
        self.changeBtn.setText(QCoreApplication.translate("MainWindow", u"Modification", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"   Sauvegarde", None))
        self.usersBtn.setText(QCoreApplication.translate("MainWindow", u"   Utilisateur", None))
        self.infosBtn.setText(QCoreApplication.translate("MainWindow", u"   Information ", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.userPass.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.usersMsg.setText("")
        self.usersConBtn.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.asRootBtn.setText(QCoreApplication.translate("MainWindow", u"As Root", None))
        self.pushButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"             Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.rootnameEd.setText("")
        self.rootMsg.setText("")
        self.rootConBtn.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.asUsersBtn.setText(QCoreApplication.translate("MainWindow", u"As Simple Users", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Forme Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nom : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sexe : ", None))
        self.maleRad.setText(QCoreApplication.translate("MainWindow", u"Homme", None))
        self.femaleRad.setText(QCoreApplication.translate("MainWindow", u"Femme", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Article :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Prix Total: ", None))
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Heure : ", None))
        self.heureLab.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Date : ", None))
        self.dateLab.setText("")
        ___qtablewidgetitem = self.tablelisteAchat.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Article", None));
        ___qtablewidgetitem1 = self.tablelisteAchat.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prix", None));
        ___qtablewidgetitem2 = self.tablelisteAchat.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PrixTotal", None));
        self.deleteLineBtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer la ligne", None))
        self.saveMsg.setText("")
        self.saveFormBtn.setText(QCoreApplication.translate("MainWindow", u"Enregister", None))
        self.annulerFormBtn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.otherBtn.setText(QCoreApplication.translate("MainWindow", u"Autre", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Depence Hors Vente", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Objet : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Prix total :", None))
        self.saveOtherBtn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.backToFormBtn.setText(QCoreApplication.translate("MainWindow", u"Annuler / Retour ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Liste des articles", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ajourter des articles", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Designation : ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Prix Unitaire : ", None))
        self.addArticleBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.cancelArticleBtn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Base de donnee", None))
        self.moreInfos.setText(QCoreApplication.translate("MainWindow", u"More Information", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Supprimer ou modifier une ligne dans la base de donnee", None))
        self.msgLab.setText("")
    # retranslateUi

