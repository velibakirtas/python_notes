# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.no_label = QtWidgets.QLabel(self.centralwidget)
        self.no_label.setGeometry(QtCore.QRect(130, 40, 61, 31))
        self.no_label.setObjectName("no_label")
        self.no_label2 = QtWidgets.QLabel(self.centralwidget)
        self.no_label2.setGeometry(QtCore.QRect(130, 80, 61, 31))
        self.no_label2.setToolTipDuration(-1)
        self.no_label2.setObjectName("no_label2")
        self.txt_line = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_line.setGeometry(QtCore.QRect(180, 39, 311, 31))
        self.txt_line.setText("")
        self.txt_line.setObjectName("txt_line")
        self.txt_line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_line2.setGeometry(QtCore.QRect(180, 79, 311, 31))
        self.txt_line2.setObjectName("txt_line2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(180, 120, 75, 31))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(260, 120, 75, 31))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(340, 120, 75, 31))
        self.btn_carpma.setObjectName("btn_carpma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(420, 120, 75, 31))
        self.btn_bolme.setObjectName("btn_bolme")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(180, 160, 311, 21))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
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
        self.no_label.setText(_translate("MainWindow", "Sayı 1: "))
        self.no_label2.setText(_translate("MainWindow", "Sayı 2: "))
        self.btn_toplama.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç: "))
