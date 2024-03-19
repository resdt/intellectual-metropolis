# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "UserWindow.ui"
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import os
import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dat

import src.main.PATH as path


OUT_FOLD = path.OUT_FOLD

TMP_PATH = path.TMP_PATH
STATION_PATH = path.STATION_PATH
TABLE_PATH = path.TABLE_PATH
PICT1_PATH = path.PICT1_PATH
PICT2_PATH = path.PICT2_PATH

table2 = []


class Ui_UserWindow(object):

    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(1003, 666)
        self.pushButton = QtWidgets.QPushButton(UserWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(UserWindow)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 171, 71))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(UserWindow)
        self.label.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(UserWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 410, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(UserWindow)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 171, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UserWindow)
        self.label_3.setGeometry(QtCore.QRect(620, 10, 141, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(UserWindow)
        self.label_4.setGeometry(QtCore.QRect(260, 370, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(UserWindow)
        self.label_5.setGeometry(QtCore.QRect(260, 400, 151, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit.setGeometry(QtCore.QRect(440, 370, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 400, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(UserWindow)
        self.label_6.setGeometry(QtCore.QRect(260, 70, 171, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(UserWindow)
        self.label_7.setGeometry(QtCore.QRect(260, 90, 171, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(UserWindow)
        self.label_8.setGeometry(QtCore.QRect(260, 110, 171, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(UserWindow)
        self.label_9.setGeometry(QtCore.QRect(260, 130, 161, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(UserWindow)
        self.label_10.setGeometry(QtCore.QRect(260, 150, 161, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(UserWindow)
        self.label_11.setGeometry(QtCore.QRect(260, 170, 161, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(UserWindow)
        self.label_12.setGeometry(QtCore.QRect(260, 190, 141, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(UserWindow)
        self.label_13.setGeometry(QtCore.QRect(260, 210, 141, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(UserWindow)
        self.label_14.setGeometry(QtCore.QRect(260, 230, 141, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(UserWindow)
        self.label_15.setGeometry(QtCore.QRect(260, 250, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(UserWindow)
        self.label_16.setGeometry(QtCore.QRect(260, 270, 141, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(UserWindow)
        self.label_17.setGeometry(QtCore.QRect(260, 290, 141, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 70, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 90, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 110, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_6.setGeometry(QtCore.QRect(440, 130, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 150, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_8.setGeometry(QtCore.QRect(440, 170, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 190, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_10.setGeometry(QtCore.QRect(440, 210, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_11.setGeometry(QtCore.QRect(440, 230, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_12.setGeometry(QtCore.QRect(440, 250, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_13.setGeometry(QtCore.QRect(440, 270, 113, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_14.setGeometry(QtCore.QRect(440, 290, 113, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_15.setGeometry(QtCore.QRect(620, 70, 113, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_16.setGeometry(QtCore.QRect(620, 90, 113, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_17.setGeometry(QtCore.QRect(620, 110, 113, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_18.setGeometry(QtCore.QRect(620, 130, 113, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_19.setGeometry(QtCore.QRect(620, 150, 113, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_20.setGeometry(QtCore.QRect(620, 170, 113, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_21.setGeometry(QtCore.QRect(620, 190, 113, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_22.setGeometry(QtCore.QRect(620, 210, 113, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_23.setGeometry(QtCore.QRect(620, 230, 113, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_24.setGeometry(QtCore.QRect(620, 250, 113, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_25.setGeometry(QtCore.QRect(620, 270, 113, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_26.setGeometry(QtCore.QRect(620, 290, 113, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_18 = QtWidgets.QLabel(UserWindow)
        self.label_18.setGeometry(QtCore.QRect(560, 70, 47, 14))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(UserWindow)
        self.label_19.setGeometry(QtCore.QRect(560, 90, 47, 14))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(UserWindow)
        self.label_20.setGeometry(QtCore.QRect(560, 110, 47, 14))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(UserWindow)
        self.label_21.setGeometry(QtCore.QRect(560, 130, 47, 14))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(UserWindow)
        self.label_22.setGeometry(QtCore.QRect(560, 150, 47, 14))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(UserWindow)
        self.label_23.setGeometry(QtCore.QRect(560, 170, 47, 14))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(UserWindow)
        self.label_24.setGeometry(QtCore.QRect(560, 190, 47, 14))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(UserWindow)
        self.label_25.setGeometry(QtCore.QRect(560, 210, 47, 14))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(UserWindow)
        self.label_26.setGeometry(QtCore.QRect(560, 230, 47, 14))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(UserWindow)
        self.label_27.setGeometry(QtCore.QRect(740, 230, 47, 14))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(UserWindow)
        self.label_28.setGeometry(QtCore.QRect(740, 150, 47, 14))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(UserWindow)
        self.label_29.setGeometry(QtCore.QRect(740, 130, 47, 14))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(UserWindow)
        self.label_30.setGeometry(QtCore.QRect(740, 170, 47, 14))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(UserWindow)
        self.label_31.setGeometry(QtCore.QRect(740, 190, 47, 14))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(UserWindow)
        self.label_32.setGeometry(QtCore.QRect(740, 90, 47, 14))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(UserWindow)
        self.label_33.setGeometry(QtCore.QRect(740, 210, 47, 14))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(UserWindow)
        self.label_34.setGeometry(QtCore.QRect(740, 70, 47, 14))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(UserWindow)
        self.label_35.setGeometry(QtCore.QRect(740, 110, 47, 14))
        self.label_35.setObjectName("label_35")
        self.pushButton_3 = QtWidgets.QPushButton(UserWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 570, 171, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(UserWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 570, 171, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(UserWindow)
        self.dateTimeEdit.setGeometry(QtCore.QRect(260, 490, 171, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 2, 19), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(UserWindow)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(260, 520, 171, 22))
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 2, 19), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_36 = QtWidgets.QLabel(UserWindow)
        self.label_36.setGeometry(QtCore.QRect(260, 440, 181, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(UserWindow)
        self.label_37.setGeometry(QtCore.QRect(30, 490, 161, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(UserWindow)
        self.label_38.setGeometry(QtCore.QRect(30, 520, 161, 16))
        self.label_38.setObjectName("label_38")
        self.listWidget_2 = QtWidgets.QListWidget(UserWindow)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 230, 91, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(UserWindow)
        self.listWidget_3.setGeometry(QtCore.QRect(130, 230, 71, 161))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_39 = QtWidgets.QLabel(UserWindow)
        self.label_39.setGeometry(QtCore.QRect(30, 210, 141, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(UserWindow)
        self.label_40.setGeometry(QtCore.QRect(130, 210, 141, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(UserWindow)
        self.label_41.setGeometry(QtCore.QRect(800, 50, 161, 91))
        self.label_41.setObjectName("label_41")
        self.lineEdit_27 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_27.setGeometry(QtCore.QRect(830, 120, 113, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_28.setGeometry(QtCore.QRect(830, 150, 113, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_29.setGeometry(QtCore.QRect(830, 180, 113, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_42 = QtWidgets.QLabel(UserWindow)
        self.label_42.setGeometry(QtCore.QRect(810, 140, 161, 91))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(UserWindow)
        self.label_43.setGeometry(QtCore.QRect(800, 80, 161, 91))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(UserWindow)
        self.label_44.setGeometry(QtCore.QRect(800, 130, 31, 51))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(UserWindow)
        self.label_45.setGeometry(QtCore.QRect(260, 310, 201, 16))
        self.label_45.setObjectName("label_45")
        self.lineEdit_30 = QtWidgets.QLineEdit(UserWindow)
        self.lineEdit_30.setGeometry(QtCore.QRect(440, 310, 113, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_46 = QtWidgets.QLabel(UserWindow)
        self.label_46.setGeometry(QtCore.QRect(710, 500, 231, 16))
        self.label_46.setObjectName("label_46")

        with open(TMP_PATH) as temp_file:
            temp_content = temp_file.readline().split()
            station_list = temp_content[-1].split(",")

        self.listWidget.addItems(station_list)

        self.pushButton.clicked.connect(self.showyourdevise)
        self.pushButton_2.clicked.connect(self.seetelemetry)
        self.listWidget_3.itemClicked.connect(self.view)
        self.pushButton_4.clicked.connect(self.maketable)
        self.pushButton_3.clicked.connect(self.seeGraph)
        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "Form2"))
        self.pushButton.setText(_translate("UserWindow", "Загрузить данные"))
        self.label.setText(_translate("UserWindow", "Выбирете доступный вам комплекс:"))
        self.pushButton_2.setText(_translate("UserWindow", "Выгрузить данные телеметрии"))
        self.label_2.setText(_translate("UserWindow", "При включенной системе"))
        self.label_3.setText(_translate("UserWindow", "При выключенной системе"))
        self.label_4.setText(_translate("UserWindow", "Время начала измерений:"))
        self.label_5.setText(_translate("UserWindow", "Время окончания измерений:"))
        self.label_6.setText(_translate("UserWindow", "Реактивная мощность по фазе A:"))
        self.label_7.setText(_translate("UserWindow", "Реактивная мощность по фазе B:"))
        self.label_8.setText(_translate("UserWindow", "Реактивная мощность по фазе C:"))
        self.label_9.setText(_translate("UserWindow", "Активная мощность по фазе A:"))
        self.label_10.setText(_translate("UserWindow", "Активная мощность по фазе B:"))
        self.label_11.setText(_translate("UserWindow", "Активная мощность по фазе C:"))
        self.label_12.setText(_translate("UserWindow", "Напряжение по фазе A:"))
        self.label_13.setText(_translate("UserWindow", "Напряжение по фазе B:"))
        self.label_14.setText(_translate("UserWindow", "Напряжение по фазе C:"))
        self.label_15.setText(_translate("UserWindow", "Косинус по фазе A:"))
        self.label_16.setText(_translate("UserWindow", "Косинус по фазе B:"))
        self.label_17.setText(_translate("UserWindow", "Косинус по фазе C:"))
        self.label_18.setText(_translate("UserWindow", "ВАр"))
        self.label_19.setText(_translate("UserWindow", "ВАр"))
        self.label_20.setText(_translate("UserWindow", "ВАр"))
        self.label_21.setText(_translate("UserWindow", "Вт"))
        self.label_22.setText(_translate("UserWindow", "Вт"))
        self.label_23.setText(_translate("UserWindow", "Вт"))
        self.label_24.setText(_translate("UserWindow", "Вольт"))
        self.label_25.setText(_translate("UserWindow", "Вольт"))
        self.label_26.setText(_translate("UserWindow", "Вольт"))
        self.label_27.setText(_translate("UserWindow", "Вольт"))
        self.label_28.setText(_translate("UserWindow", "Вт"))
        self.label_29.setText(_translate("UserWindow", "Вт"))
        self.label_30.setText(_translate("UserWindow", "Вт"))
        self.label_31.setText(_translate("UserWindow", "Вольт"))
        self.label_32.setText(_translate("UserWindow", "ВАр"))
        self.label_33.setText(_translate("UserWindow", "Вольт"))
        self.label_34.setText(_translate("UserWindow", "ВАр"))
        self.label_35.setText(_translate("UserWindow", "ВАр"))
        self.pushButton_3.setText(_translate("UserWindow", "Построить график"))
        self.pushButton_4.setText(_translate("UserWindow", "Выгрузить таблицу"))
        self.dateTimeEdit.setDisplayFormat(_translate("UserWindow", "dd.MM.yyyy H:mm:ss"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("UserWindow", "dd.MM.yyyy H:mm:ss"))
        self.label_36.setText(_translate("UserWindow", "Просмотр данных за диапазон:"))
        self.label_37.setText(_translate("UserWindow", "Начало диапазона просмотра:"))
        self.label_38.setText(_translate("UserWindow", "Конец диапазона просмотра:"))
        self.label_39.setText(_translate("UserWindow", "Имя файла"))
        self.label_40.setText(_translate("UserWindow", "Номер записи"))
        self.label_41.setText(_translate("UserWindow", "n=  (P_off-P_on)/P_off ∙100% "))
        self.label_42.setText(_translate("UserWindow", "n"))
        self.label_43.setText(_translate("UserWindow", "P_on"))
        self.label_44.setText(_translate("UserWindow", "P_off"))
        self.label_45.setText(_translate("UserWindow", "Количество включенных блоков:"))
        self.label_46.setText(_translate("UserWindow", "Позже график будет тут"))

    def showyourdevise(self):
        print("GO!")

        self.listWidget_2.clear()

        current = self.listWidget.currentItem().text()
        print(current)

        data_filenames = os.listdir(path=STATION_PATH)
        print(data_filenames)

        for filename in data_filenames:
            station = filename.split(".")[0]

            if current in station:
                print(station)
                self.listWidget_2.addItem(station)

        self.listWidget_2.sortItems()

    def seetelemetry(self):
        filename = self.listWidget_2.currentItem().text() + ".csv"

        self.listWidget_3.clear()

        with open(f"{STATION_PATH}/{filename}") as station_content:
            length = len(station_content.readlines())

        self.listWidget_3.addItems(map(str, list(range(1, length + 1))))

    def view(self):
        filename = self.listWidget_2.currentItem().text() + ".csv"
        row_number = int(self.listWidget_3.currentItem().text()) - 1
        print(row_number)

        station_content = open(f"{STATION_PATH}/{filename}").readlines()
        content_list = station_content[row_number].split(";")
        print(content_list)

        self.lineEdit.setText(content_list[0])
        self.lineEdit_2.setText(content_list[1])

        for i in range(3, 27):
            exec("self.lineEdit_%s.setText(content_list[i-1])" % i)

        self.lineEdit_30.setText(content_list[-1])

        fon = sum(list(map(float, content_list[5:8])))
        print(fon)

        foff = 0

        if content_list[17] != "":
            foff = sum(list(map(float, content_list[17:20])))
            print(foff)

        self.lineEdit_27.setText(str(fon))

        if foff != 0:
            self.lineEdit_28.setText(str(foff))
            self.lineEdit_29.setText(str((foff-fon) / foff * 100))

    def maketable(self):
        global table2

        date_start = dat.datetime.strptime(self.dateTimeEdit.text(),
                                           "%d.%m.%Y %H:%M:%S")
        date_end = dat.datetime.strptime(self.dateTimeEdit_2.text(),
                                         "%d.%m.%Y %H:%M:%S")
        print(date_start)
        print(date_end)

        current = self.listWidget.currentItem().text()
        # print(current)

        data_filenames = os.listdir(path=STATION_PATH)
        # print(data_filenames)

        for filename in data_filenames:
            station = filename.split(".")[0]

            if current in station:
                station_content = open(f"{STATION_PATH}/{filename}").readlines()

                for line in station_content:
                    content_list = line.split(";")
                    # print(content_list)

                    date_start_file = dat.datetime.strptime(content_list[0],
                                                            "%d.%m.%Y %H:%M:%S")
                    date_end_file = dat.datetime.strptime(content_list[1],
                                                          "%d.%m.%Y %H:%M:%S")
                    # print("===================")
                    # print(date_start)
                    # print(date_end)
                    # print(date_start_file)
                    # print(date_end_file)

                    if date_start <= date_start_file and date_end >= date_end_file:
                        table2.append(content_list)

                        print("YES!")

        print(table2)

        os.makedirs(OUT_FOLD, exist_ok=True)

        with open(TABLE_PATH, "w+") as table_output:
            writer = csv.writer(table_output)
            writer.writerows(table2)

        print("Writing done")

    def seeGraph(self):
        global table2
        print(table2)

        y1 = []
        y2 = []
        y3 = []
        y4 = []
        y5 = []
        y6 = []

        table2.sort(key=lambda x: dat.datetime.strptime(x[0],
                                                   "%d.%m.%Y %H:%M:%S"))
        print(table2)

        for row in table2:
            y1.append(float(row[5]))
            y2.append(float(row[6]))
            y3.append(float(row[7]))
            y4.append(float(row[2]))
            y5.append(float(row[3]))
            y6.append(float(row[4]))

        x = np.linspace(0, 101, len(y1))
        print(x, "     ", y1, y2, y3)

        fig, ax = plt.subplots()
        fig2, ax2 = plt.subplots()

        ax.plot(x, y1, color="blue", label="по фазе А")
        ax.plot(x, y2, color="red", label="по фазе B")
        ax.plot(x, y3, color="green", label="по фазе С")
        ax.set_xlabel("время")
        ax.set_ylabel("Активная мощность по фазе при включенной системе")
        ax.legend()

        ax2.plot(x, y4, color="blue", label="по фазе А")
        ax2.plot(x, y5, color="red", label="по фазе B")
        ax2.plot(x, y6, color="green", label="по фазе C")
        ax2.set_xlabel("время")
        ax2.set_ylabel("Реактивная мощность при включенной системе")
        ax2.legend()

        plt.show()

        os.makedirs(OUT_FOLD, exist_ok=True)
        fig.savefig(PICT1_PATH)
        fig2.savefig(PICT2_PATH)