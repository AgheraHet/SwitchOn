# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeriFArek.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600,600)
        MainWindow.showMaximized()
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.All = QWidget()
        self.All.setObjectName(u"All")
        self.gridLayout = QGridLayout(self.All)
        self.gridLayout.setObjectName(u"gridLayout")
        self.All_2 = QScrollArea(self.All)
        self.All_2.setObjectName(u"All_2")
        self.All_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 756, 533))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
#         self.All_Card = QFrame(self.scrollAreaWidgetContents_3)
#         self.All_Card.setObjectName(u"All_Card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)

        self.All_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.All_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.All, "")
        self.Bad = QWidget()
        self.Bad.setObjectName(u"Bad")
        self.gridLayout_2 = QGridLayout(self.Bad)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Bad_2 = QScrollArea(self.Bad)
        self.Bad_2.setObjectName(u"Bad_2")
        self.Bad_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 756, 533))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")


        self.Bad_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.Bad_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Bad, "")
        self.Good = QWidget()
        self.Good.setObjectName(u"Good")
        self.Good.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.Good)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Good_2 = QScrollArea(self.Good)
        self.Good_2.setObjectName(u"Good_2")
        self.Good_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 756, 533))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")


        self.Good_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.Good_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Good, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SwitchOn", None))
#if QT_CONFIG(tooltip)
        self.centralwidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.All), QCoreApplication.translate("MainWindow", u"All", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bad), QCoreApplication.translate("MainWindow", u"Bad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Good), QCoreApplication.translate("MainWindow", u"Good", None))
    # retranslateUi

