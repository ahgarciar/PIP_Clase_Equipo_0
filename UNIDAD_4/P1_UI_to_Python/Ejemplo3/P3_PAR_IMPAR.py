# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P3_PAR_IMPAR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_checar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_checar.setGeometry(QtCore.QRect(120, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_checar.setFont(font)
        self.btn_checar.setObjectName("btn_checar")

        self.txt_n = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_n.setGeometry(QtCore.QRect(120, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_n.setFont(font)
        self.txt_n.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_n.setObjectName("txt_n")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 15, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btn_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpiar.setGeometry(QtCore.QRect(450, 220, 131, 41))
        self.btn_limpiar.setObjectName("btn_limpiar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
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
        self.btn_checar.setText(_translate("MainWindow", "CHECAR SI ES PAR"))
        self.txt_n.setText(_translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "N:"))
        self.btn_limpiar.setText(_translate("MainWindow", "LIMPIAR"))

