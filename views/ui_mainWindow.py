# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 624)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionFont_Size = QAction(MainWindow)
        self.actionFont_Size.setObjectName(u"actionFont_Size")
        self.actionFull_Screen_Mode = QAction(MainWindow)
        self.actionFull_Screen_Mode.setObjectName(u"actionFull_Screen_Mode")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionView_Reapport = QAction(MainWindow)
        self.actionView_Reapport.setObjectName(u"actionView_Reapport")
        self.actionExport_Report = QAction(MainWindow)
        self.actionExport_Report.setObjectName(u"actionExport_Report")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.dataTableView = QTableView(self.frame_2)
        self.dataTableView.setObjectName(u"dataTableView")

        self.verticalLayout.addWidget(self.dataTableView)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 2, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1, Qt.AlignTop)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.video_label = QLabel(self.frame)
        self.video_label.setObjectName(u"video_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_label.sizePolicy().hasHeightForWidth())
        self.video_label.setSizePolicy(sizePolicy1)
        self.video_label.setMinimumSize(QSize(640, 480))
        self.video_label.setMaximumSize(QSize(640, 480))
        self.video_label.setTextFormat(Qt.PlainText)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.video_label)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.date = QLabel(self.centralwidget)
        self.date.setObjectName(u"date")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        self.date.setFont(font2)

        self.horizontalLayout_3.addWidget(self.date)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1059, 21))
        self.menufiler = QMenu(self.menubar)
        self.menufiler.setObjectName(u"menufiler")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuStudents = QMenu(self.menubar)
        self.menuStudents.setObjectName(u"menuStudents")
        self.menuAttendance = QMenu(self.menubar)
        self.menuAttendance.setObjectName(u"menuAttendance")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufiler.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuStudents.menuAction())
        self.menubar.addAction(self.menuAttendance.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menufiler.addAction(self.actionopen)
        self.menufiler.addAction(self.actionsave)
        self.menufiler.addAction(self.actionQuit)
        self.menufiler.addSeparator()
        self.menuView.addAction(self.actionFont_Size)
        self.menuView.addAction(self.actionFull_Screen_Mode)
        self.menuStudents.addAction(self.actionAdd)
        self.menuStudents.addAction(self.actionDelete)
        self.menuStudents.addAction(self.actionEdit)
        self.menuAttendance.addAction(self.actionView_Reapport)
        self.menuAttendance.addAction(self.actionExport_Report)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionFont_Size.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.actionFull_Screen_Mode.setText(QCoreApplication.translate("MainWindow", u"Full-Screen Mode", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionView_Reapport.setText(QCoreApplication.translate("MainWindow", u"View Reapport", None))
        self.actionExport_Report.setText(QCoreApplication.translate("MainWindow", u"Export Report", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ATTENDANCES</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.video_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DATE : ", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.menufiler.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuStudents.setTitle(QCoreApplication.translate("MainWindow", u"Students", None))
        self.menuAttendance.setTitle(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

