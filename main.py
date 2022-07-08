"""
此代码由PyQt5的PyUic5进行转换，所以代码结构比较乱，没有注释，请大家谅解。
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 635)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/手表.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 341, 151))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 80, 121, 61))
        self.label_2.setStyleSheet("image: url(:/img/img/手表.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 121, 101))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/应用管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 280, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 170, 121, 101))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/视频.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 280, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 170, 121, 101))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/截图.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 280, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 350, 121, 101))
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/工具箱.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 460, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 350, 121, 101))
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/文件夹.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 460, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 170, 121, 101))
        self.pushButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(850, 280, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 350, 121, 101))
        self.pushButton_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/连接.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 460, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(810, 350, 121, 101))
        self.pushButton_8.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/退出程序.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(830, 460, 72, 15))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        import threading
        t1 = threading.Thread(target=self.toast, args=())
        t1.setDaemon(True)
        t1.start()

        self.retranslateUi(MainWindow)
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_7.clicked.connect(self.startconnect)
        self.pushButton.clicked.connect(self.startinstall)
        self.pushButton_2.clicked.connect(self.startscreenrecord)
        self.pushButton_3.clicked.connect(self.startscreenshot)
        self.pushButton_6.clicked.connect(self.startsettings)
        self.pushButton_4.clicked.connect(self.starttoolbox)
        self.pushButton_5.clicked.connect(self.tishi)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startconnect(self):
        self.child_window = Ui_Form()
        self.child_window.show()

    def startinstall(self):
        self.child_window = Ui_Form1()
        self.child_window.show()
    def tishi(self):
        QMessageBox.information(None, "信息", "敬请期待", QMessageBox.Yes)
    def startscreenrecord(self):
        self.child_window = Ui_Form2()
        self.child_window.show()

    def startscreenshot(self):
        self.child_window = Ui_Form3()
        self.child_window.show()
        
    def startsettings(self):
        self.child_window = Ui_Form4()
        self.child_window.show()
    def starttoolbox(self):
        self.child_window = Ui_Form5()
        self.child_window.show()
    def toast(self):
        from win10toast import ToastNotifier
        TN = ToastNotifier()
        TN.show_toast("XTCToolBox", "XTCToolBox启动", "./ajfj2-yrv0f-002.ico", 10)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XTCToolBox"))
        self.label.setText(_translate("MainWindow", "XTCToolBox"))
        self.label_3.setText(_translate("MainWindow", "安装应用"))
        self.label_4.setText(_translate("MainWindow", "录屏"))
        self.label_5.setText(_translate("MainWindow", "截屏"))
        self.label_6.setText(_translate("MainWindow", "工具箱"))
        self.label_7.setText(_translate("MainWindow", "文件管理"))
        self.label_8.setText(_translate("MainWindow", "设置"))
        self.label_9.setText(_translate("MainWindow", "连接设备"))
        self.label_10.setText(_translate("MainWindow", "退出程序"))

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(self.width(), self.height())
        self.setObjectName("Form")
        self.setFixedSize(684, 432)
        self.resize(684, 432)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/连接.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 641, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 100, 601, 51))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("font: 9pt \"MiSans\";\n"
"image: url(:/img/img/检测.png);")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(450, 300, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 160, 431, 211))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 351, 41))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 30, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 310, 181, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget_2.setGeometry(QtCore.QRect(10, 140, 431, 211))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.commandLinkButton.clicked.connect(self.connectDevices)
        self.pushButton.clicked.connect(self.restartAdbService)
        self.pushButton_3.clicked.connect(self.restartAdbService)
        self.pushButton_2.clicked.connect(self.wificonnect)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def connectDevices(self):
        QMessageBox.information(self, "信息", "开始检测设备连接，请连接设备。", QMessageBox.Yes)
        os.system("adb wait-for-device")
        Devices = os.popen("adb devices").read()
        次数 = Devices.count("device")
        if(次数 == 1):
            QMessageBox.warning(self, "信息", "连接失败，请重新连接", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "信息", "连接成功", QMessageBox.Yes)


    def restartAdbService(self):
        QMessageBox.information(self, "信息", "正在杀死adb进程......", QMessageBox.Yes)
        os.popen("taskkill /f /im adb.exe")
        os.popen("adb kill-server")
        QMessageBox.information(self, "信息", "正在启动adb进程......", QMessageBox.Yes)
        os.popen("adb start-server")
        QMessageBox.information(self, "信息", "成功重启adb服务", QMessageBox.Yes)
    def wificonnect(self):
        QMessageBox.information(self, "信息", "正在尝试连接......", QMessageBox.Yes)
        os.system("adb connect "+self.lineEdit.text())
        Devices = os.popen("adb devices").read()
        次数 = Devices.count("device")
        if (次数 == 1):
            QMessageBox.warning(self, "信息", "连接失败，请重新连接", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "信息", "连接成功", QMessageBox.Yes)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "连接设备"))
        self.label.setText(_translate("Form", "请在插入设备之后进行检测"))
        self.commandLinkButton.setText(_translate("Form", "检测"))
        self.pushButton.setText(_translate("Form", "重启ADB服务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "有线连接"))
        self.lineEdit.setPlaceholderText(_translate("Form", "在这里输入你要连接设备的IP地址"))
        self.pushButton_2.setText(_translate("Form", "启动连接"))
        self.pushButton_3.setText(_translate("Form", "重启ADB服务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "无线连接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "无线转有线"))

class Ui_Form1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(564,148)
        self.setObjectName("Form")
        self.resize(564, 148)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/应用管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(380, 30, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 80, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self)
        self.pushButton_2.clicked.connect(self.setFiles)
        self.pushButton.clicked.connect(self.installApps)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "安装软件"))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入apk文件路径"))
        self.pushButton.setText(_translate("Form", "启动安装"))
        self.pushButton_2.setText(_translate("Form", "选择文件"))

    def setFiles(self):
        import os
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "APK安装包(*.apk);;所有文件(*);")
        if(fileType == '所有文件(*);'):
            QMessageBox.warning(self, "信息", "文件格式非APK", QMessageBox.Yes)
        else:
            self.lineEdit.setText(str(fileName))

    def installApps(self):
        apkName = self.lineEdit.text()
        import os
        result = os.popen("adb install "+apkName).read()
        print(result)
        if("no devices/emulators found" in result):
            QMessageBox.warning(self, "信息", "您未连接设备", QMessageBox.Yes)
        if("User-Version 'adb install' is not allowed directly,Pls ask 'XTC-Company'." in result):
            QMessageBox.warning(self, "信息", "您的手表为小天才手表，且为刷入sboot包，仅可通过pm安装或无法安装，正在启动命令行......", QMessageBox.Yes)
            os.system("adb shell")
class Ui_Form2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(549,254)
        self.setObjectName("Form")
        self.resize(549, 254)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/视频.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(420, 40, 121, 41))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 341, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(190, 90, 61, 31))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 90, 131, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 351, 71))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.screenRecord)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def screenRecord(self):
        dirName = self.lineEdit.text()
        recordTime = self.spinBox.value()
        print(self.checkBox.isChecked())
        print(dirName)
        print(recordTime)
        if(self.checkBox.isChecked() == True):
            os.system("adb shell screenrecord  --time-limit" + " " + str(recordTime) + " " + "--verbose" + " " + dirName)
            os.popen("adb pull " + dirName + " " + os.getcwd())
            QMessageBox.information(self, "信息", "录屏完成", QMessageBox.Yes)
            os.system("explorer "+os.getcwd())
        elif(self.checkBox.isChecked() == False):
            os.system("adb shell screenrecord  --time-limit" + " " + str(recordTime) + " "  + " " + dirName)
            os.popen("adb pull " + dirName + " " + os.getcwd())
            QMessageBox.information(self, "信息", "录屏完成", QMessageBox.Yes)
            os.system("explorer "+os.getcwd())
        else:
            pass


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "录屏"))
        self.checkBox.setText(_translate("Form", "是否打开log"))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入录制位置"))
        self.label.setText(_translate("Form", "输入录制时间"))
        self.pushButton.setText(_translate("Form", "开始录屏"))


class Ui_Form3(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(400, 107)
        self.setFixedSize(400,107)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/截图.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 301, 61))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.screenShot)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def screenShot(self):
        os.system("adb shell screencap -p /sdcard/1.jpg")
        os.popen("adb pull /sdcard/1.jpg"+" "+os.getcwd())
        QMessageBox.information(self, "信息", "截屏保存完成", QMessageBox.Yes)
        os.system("1.jpg")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "截屏"))
        self.pushButton.setText(_translate("Form", "截屏"))
"""
A rudimentary URL downloader (like wget or curl) to demonstrate Rich progress bars.
"""

import os.path
import sys
from concurrent.futures import as_completed, ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)


done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def copy_url(task_id: TaskID, url: str, path: str) -> None:
    """Copy data from a url to a local file."""
    progress.console.log(f"Requesting {url}")
    response = urlopen(url)
    # This will break if the response doesn't contain content length
    progress.update(task_id, total=int(response.info()["Content-length"]))
    with open(path, "wb") as dest_file:
        progress.start_task(task_id)
        for data in iter(partial(response.read, 32768), b""):
            dest_file.write(data)
            progress.update(task_id, advance=len(data))
            if done_event.is_set():
                return
    progress.console.log(f"Downloaded {path}")


def download(urls: Iterable[str], dest_dir: str):
    """Download multuple files to the given directory."""

    with progress:
        with ThreadPoolExecutor(max_workers=4) as pool:
            for url in urls:
                filename = url.split("/")[-1]
                dest_path = os.path.join(dest_dir, filename)
                task_id = progress.add_task("download", filename=filename, start=False)
                pool.submit(copy_url, task_id, url, dest_path)



class Ui_Form4(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.setFixedSize(400, 300)
        self.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 371, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 30, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 110, 251, 91))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 40, 151, 131))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("image: url(:/img/img/更新.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(140, 190, 72, 15))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton.clicked.connect(self.restartAdbService)
        self.pushButton_3.clicked.connect(self.updateProgram)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def restartAdbService(self):
        QMessageBox.information(self, "信息", "正在杀死adb进程......", QMessageBox.Yes)
        os.popen("taskkill /f /im adb.exe")
        os.popen("adb kill-server")
        QMessageBox.information(self, "信息", "正在启动adb进程......", QMessageBox.Yes)
        os.popen("adb start-server")
        QMessageBox.information(self, "信息", "成功重启adb服务", QMessageBox.Yes)
    
    def updateProgram(self):
        QMessageBox.information(self, "信息", "正在检查更新......", QMessageBox.Yes)
        import requests
        page = requests.get('https://gitee.com/vmtask/XTCToolBox2.0/raw/master/version.txt')
        if(float(page.text) == 3.0):
            QMessageBox.information(self, "信息", "已经是最新版本", QMessageBox.Yes)
        else:
            question = QMessageBox.information(self, "信息", "有最新版本，是否更新？", QMessageBox.Yes | QMessageBox.No)
            if(question == 16384):
                import requests
                page1 = requests.get('https://gitee.com/vmtask/XTCToolBox2.0/raw/master/downloads.txt')
                download([page1.text], "./")
                question = QMessageBox.information(self, "信息", "下载完毕，开始安装", QMessageBox.Yes | QMessageBox.No)
                os.system("Setup.exe")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置"))
        self.pushButton.setText(_translate("Form", "重启ADB服务"))
        self.pushButton_2.setText(_translate("Form", "启动最后一版CLI版"))
        self.label.setText(_translate("Form", "程序版本:2.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "基本"))
        self.label_2.setText(_translate("Form", "检查更新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "更新"))
class Ui_Form5(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(267, 229)
        self.setFixedSize(267, 229)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/工具箱.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(11, 99, 99, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(137, 99, 114, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(11, 37, 93, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(137, 37, 114, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 161, 93, 29))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 160, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "工具箱"))
        self.pushButton.setText(_translate("Form", "打开应用活动"))
        self.pushButton_2.setText(_translate("Form", "打开输入法选择"))
        self.pushButton_3.setText(_translate("Form", "打开自检"))
        self.pushButton_4.setText(_translate("Form", "打开开发者选项"))
        self.pushButton_5.setText(_translate("Form", "调整DPI"))
        self.pushButton_6.setText(_translate("Form", "命令行"))
import main_rc
if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()#MainWindow由启动类型确定，可自行更改，接下来都是这样
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())