# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(60, 40, 241, 71))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(340, 50, 251, 41))
        self.lbl_result.setObjectName("lbl_result")
        self.btn_getItem = QtWidgets.QPushButton(self.centralwidget)
        self.btn_getItem.setGeometry(QtCore.QRect(60, 140, 231, 41))
        self.btn_getItem.setObjectName("btn_getItem")
        self.btn_loadItem = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadItem.setGeometry(QtCore.QRect(330, 140, 251, 41))
        self.btn_loadItem.setObjectName("btn_loadItem")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(60, 190, 231, 41))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 21))
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
        self.lbl_result.setText(_translate("MainWindow", "TextLabel"))
        self.btn_getItem.setText(_translate("MainWindow", "Get Item"))
        self.btn_loadItem.setText(_translate("MainWindow", "Load Items"))
        self.btn_clear.setText(_translate("MainWindow", "Clear Item"))
