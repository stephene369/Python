# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_hydro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 613)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slidWidget = QWidget(self.centralwidget)
        self.slidWidget.setObjectName(u"slidWidget")
        self.verticalLayout = QVBoxLayout(self.slidWidget)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 60, 0, 60)
        self.menuBtn = QPushButton(self.slidWidget)
        self.menuBtn.setObjectName(u"menuBtn")

        self.verticalLayout.addWidget(self.menuBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.homeBtn = QPushButton(self.slidWidget)
        self.homeBtn.setObjectName(u"homeBtn")

        self.verticalLayout.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.slidWidget)
        self.dataBtn.setObjectName(u"dataBtn")

        self.verticalLayout.addWidget(self.dataBtn)

        self.infosBtn = QPushButton(self.slidWidget)
        self.infosBtn.setObjectName(u"infosBtn")

        self.verticalLayout.addWidget(self.infosBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.slidWidget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Page0 = QWidget()
        self.Page0.setObjectName(u"Page0")
        self.verticalLayout_2 = QVBoxLayout(self.Page0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget.addWidget(self.Page0)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_2 = QHBoxLayout(self.homePage)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paraBtn = QPushButton(self.homePage)
        self.paraBtn.setObjectName(u"paraBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paraBtn.sizePolicy().hasHeightForWidth())
        self.paraBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.paraBtn)

        self.surpBtn = QPushButton(self.homePage)
        self.surpBtn.setObjectName(u"surpBtn")
        sizePolicy.setHeightForWidth(self.surpBtn.sizePolicy().hasHeightForWidth())
        self.surpBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.surpBtn)

        self.stackedWidget.addWidget(self.homePage)
        self.paraPage = QWidget()
        self.paraPage.setObjectName(u"paraPage")
        self.paraPage.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.paraPage)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, 40, 40, 40)
        self.scrollArea = QScrollArea(self.paraPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 433, 1164))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 12)
        self.paraLab = QLabel(self.scrollAreaWidgetContents)
        self.paraLab.setObjectName(u"paraLab")
        self.paraLab.setStyleSheet(u"background:transparent ;")
        self.paraLab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.paraLab)

        self.label1Para = QLabel(self.scrollAreaWidgetContents)
        self.label1Para.setObjectName(u"label1Para")
        self.label1Para.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label1Para)

        self.grig1 = QGridLayout()
        self.grig1.setObjectName(u"grig1")
        self.hTSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.hTSpin.setObjectName(u"hTSpin")

        self.grig1.addWidget(self.hTSpin, 2, 1, 1, 1)

        self.hTLab = QLabel(self.scrollAreaWidgetContents)
        self.hTLab.setObjectName(u"hTLab")

        self.grig1.addWidget(self.hTLab, 2, 0, 1, 1)

        self.usageCombo = QComboBox(self.scrollAreaWidgetContents)
        self.usageCombo.setObjectName(u"usageCombo")

        self.grig1.addWidget(self.usageCombo, 0, 1, 1, 1)

        self.hSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.hSpin.setObjectName(u"hSpin")

        self.grig1.addWidget(self.hSpin, 1, 1, 1, 1)

        self.hLab = QLabel(self.scrollAreaWidgetContents)
        self.hLab.setObjectName(u"hLab")

        self.grig1.addWidget(self.hLab, 1, 0, 1, 1)

        self.usageLab = QLabel(self.scrollAreaWidgetContents)
        self.usageLab.setObjectName(u"usageLab")

        self.grig1.addWidget(self.usageLab, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.grig1)

        self.label2Para = QLabel(self.scrollAreaWidgetContents)
        self.label2Para.setObjectName(u"label2Para")
        self.label2Para.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label2Para)

        self.grid2 = QGridLayout()
        self.grid2.setObjectName(u"grid2")
        self.longTtSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.longTtSpin.setObjectName(u"longTtSpin")

        self.grid2.addWidget(self.longTtSpin, 5, 1, 1, 1)

        self.longCanLab = QLabel(self.scrollAreaWidgetContents)
        self.longCanLab.setObjectName(u"longCanLab")

        self.grid2.addWidget(self.longCanLab, 4, 0, 1, 1)

        self.longAspLab = QLabel(self.scrollAreaWidgetContents)
        self.longAspLab.setObjectName(u"longAspLab")

        self.grid2.addWidget(self.longAspLab, 3, 0, 1, 1)

        self.lonDefSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.lonDefSpin.setObjectName(u"lonDefSpin")

        self.grid2.addWidget(self.lonDefSpin, 2, 1, 1, 1)

        self.longTtLab = QLabel(self.scrollAreaWidgetContents)
        self.longTtLab.setObjectName(u"longTtLab")

        self.grid2.addWidget(self.longTtLab, 5, 0, 1, 1)

        self.longAspSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.longAspSpin.setObjectName(u"longAspSpin")

        self.grid2.addWidget(self.longAspSpin, 3, 1, 1, 1)

        self.lonDefLab = QLabel(self.scrollAreaWidgetContents)
        self.lonDefLab.setObjectName(u"lonDefLab")

        self.grid2.addWidget(self.lonDefLab, 2, 0, 1, 1)

        self.categorieLab = QLabel(self.scrollAreaWidgetContents)
        self.categorieLab.setObjectName(u"categorieLab")

        self.grid2.addWidget(self.categorieLab, 1, 0, 1, 1)

        self.categorieCombo = QComboBox(self.scrollAreaWidgetContents)
        self.categorieCombo.setObjectName(u"categorieCombo")

        self.grid2.addWidget(self.categorieCombo, 1, 1, 1, 1)

        self.longCanSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.longCanSpin.setObjectName(u"longCanSpin")

        self.grid2.addWidget(self.longCanSpin, 4, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.grid2)

        self.label3Para = QLabel(self.scrollAreaWidgetContents)
        self.label3Para.setObjectName(u"label3Para")

        self.verticalLayout_4.addWidget(self.label3Para)

        self.grid3 = QGridLayout()
        self.grid3.setObjectName(u"grid3")
        self.pressRelSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.pressRelSpin.setObjectName(u"pressRelSpin")

        self.grid3.addWidget(self.pressRelSpin, 1, 1, 1, 1)

        self.vMinSpin = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.vMinSpin.setObjectName(u"vMinSpin")

        self.grid3.addWidget(self.vMinSpin, 0, 1, 1, 1)

        self.pressRelLab = QLabel(self.scrollAreaWidgetContents)
        self.pressRelLab.setObjectName(u"pressRelLab")

        self.grid3.addWidget(self.pressRelLab, 1, 0, 1, 1)

        self.vMinLab = QLabel(self.scrollAreaWidgetContents)
        self.vMinLab.setObjectName(u"vMinLab")

        self.grid3.addWidget(self.vMinLab, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.grid3)

        self.label4Para = QLabel(self.scrollAreaWidgetContents)
        self.label4Para.setObjectName(u"label4Para")

        self.verticalLayout_4.addWidget(self.label4Para)

        self.grid4 = QGridLayout()
        self.grid4.setObjectName(u"grid4")
        self.nbCSpin = QSpinBox(self.scrollAreaWidgetContents)
        self.nbCSpin.setObjectName(u"nbCSpin")

        self.grid4.addWidget(self.nbCSpin, 1, 1, 1, 1)

        self.nbCLab = QLabel(self.scrollAreaWidgetContents)
        self.nbCLab.setObjectName(u"nbCLab")

        self.grid4.addWidget(self.nbCLab, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.grid4)

        self.getDataBtn = QPushButton(self.scrollAreaWidgetContents)
        self.getDataBtn.setObjectName(u"getDataBtn")

        self.verticalLayout_4.addWidget(self.getDataBtn)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(0, 600))

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.paraPage)
        self.surPage = QWidget()
        self.surPage.setObjectName(u"surPage")
        self.stackedWidget.addWidget(self.surPage)
        self.cumputePage = QWidget()
        self.cumputePage.setObjectName(u"cumputePage")
        self.verticalLayout_5 = QVBoxLayout(self.cumputePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.cumputePage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 508, 593))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.backToPara = QPushButton(self.scrollAreaWidgetContents_2)
        self.backToPara.setObjectName(u"backToPara")

        self.verticalLayout_6.addWidget(self.backToPara)

        self.recapTable = QTableWidget(self.scrollAreaWidgetContents_2)
        self.recapTable.setObjectName(u"recapTable")

        self.verticalLayout_6.addWidget(self.recapTable)

        self.calculBtn = QPushButton(self.scrollAreaWidgetContents_2)
        self.calculBtn.setObjectName(u"calculBtn")

        self.verticalLayout_6.addWidget(self.calculBtn)

        self.resultTable = QTableWidget(self.scrollAreaWidgetContents_2)
        self.resultTable.setObjectName(u"resultTable")

        self.verticalLayout_6.addWidget(self.resultTable)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.cumputePage)
        self.infosPage = QWidget()
        self.infosPage.setObjectName(u"infosPage")
        self.stackedWidget.addWidget(self.infosPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.homeBtn.setText("")
        self.dataBtn.setText("")
        self.infosBtn.setText("")
        self.paraBtn.setText("")
        self.surpBtn.setText("")
        self.paraLab.setText(QCoreApplication.translate("MainWindow", u"Systeme de distribution en Parapluie", None))
        self.label1Para.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.hTLab.setText("")
        self.hLab.setText("")
        self.usageLab.setText("")
        self.label2Para.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.longCanLab.setText("")
        self.longAspLab.setText("")
        self.longTtLab.setText("")
        self.lonDefLab.setText("")
        self.categorieLab.setText("")
        self.label3Para.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pressRelLab.setText("")
        self.vMinLab.setText("")
        self.label4Para.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.nbCLab.setText("")
        self.getDataBtn.setText("")
        self.backToPara.setText("")
        self.calculBtn.setText("")
    # retranslateUi

