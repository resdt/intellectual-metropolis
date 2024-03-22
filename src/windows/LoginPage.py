# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "main1.ui"
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os
import PIL
from PyQt5 import QtCore, QtGui, QtWidgets

import src.main.PATH as path


TMP_FOLD = path.TMP_FOLD

DATA_BACKGROUND_PATH = path.DATA_BACKGROUND_PATH
RESIZED_BACKGROUND_PATH = path.RESIZED_BACKGROUND_PATH


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 761)
        MainWindow.setMinimumSize(QtCore.QSize(1338, 761))
        MainWindow.setMaximumSize(QtCore.QSize(1338, 761))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 490, 71, 31))
        self.label_2.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 530, 131, 16))
        self.label_3.setStyleSheet("font: 10pt \"Yu Gothic UI Semilight\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 580, 161, 20))
        self.label_5.setStyleSheet("font: 10pt \"Yu Gothic UI Semilight\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 630, 181, 16))
        self.label_6.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 660, 91, 16))
        self.label_7.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 660, 81, 16))
        self.label_8.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 1161, 191))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 25pt \"OCR A Extended\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 1361, 741))
        image = PIL.Image.open(DATA_BACKGROUND_PATH)
        resized_image = image.resize((1338, 761))
        os.makedirs(TMP_FOLD, exist_ok=True)
        resized_image.save(RESIZED_BACKGROUND_PATH)
        self.label_9.setStyleSheet(f"background-image: url({RESIZED_BACKGROUND_PATH});\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-position: center;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(""))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 540, 141, 51))
        self.label_10.setStyleSheet("font: 10pt \"Yu Gothic UI Semilight\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-20, 40, 221, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(""))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(420, 250, 331, 351))
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(520, 270, 211, 41))
        self.label_12.setStyleSheet("font: 63 15pt\"Yu Gothic UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440, 370, 131, 31))
        self.label_13.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(530, 370, 211, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(211, 31))
        self.lineEdit.setMaximumSize(QtCore.QSize(211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 420, 161, 41))
        self.label_14.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 430, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 520, 251, 51))
        self.pushButton_5.setStyleSheet("font: 63 12pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(47, 142, 192);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 600, 161, 20))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Yu Gothic UI Semilight\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(460, 470, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(530, 400, 211, 21))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_10.raise_()
        self.label_4.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.lineEdit.raise_()
        self.label_14.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_5.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1338, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Версия 0.1"))
        self.label.setText(_translate("MainWindow",
                                      "Мониторинг комплекса энергосбережения"))
        self.label_12.setText(_translate("MainWindow", "Авторизация"))
        self.label_13.setText(_translate("MainWindow", "Логин:"))
        self.label_14.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton_5.setText(_translate("MainWindow", "Вход"))
        self.label_16.setText(_translate("MainWindow",
                                         "Введите учетные данные"))
