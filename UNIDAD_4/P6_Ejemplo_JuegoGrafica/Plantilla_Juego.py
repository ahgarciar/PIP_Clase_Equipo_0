# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plantilla_Juego.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 601, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_action = QtWidgets.QPushButton(self.centralwidget)
        self.btn_action.setGeometry(QtCore.QRect(650, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_action.setFont(font)
        self.btn_action.setObjectName("btn_action")
        self.btn_arriba = QtWidgets.QPushButton(self.centralwidget)
        self.btn_arriba.setGeometry(QtCore.QRect(820, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_arriba.setFont(font)
        self.btn_arriba.setObjectName("btn_arriba")
        self.btn_izquierda = QtWidgets.QPushButton(self.centralwidget)
        self.btn_izquierda.setGeometry(QtCore.QRect(680, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_izquierda.setFont(font)
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.btn_abajo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abajo.setGeometry(QtCore.QRect(820, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abajo.setFont(font)
        self.btn_abajo.setObjectName("btn_abajo")
        self.btn_derecha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_derecha.setGeometry(QtCore.QRect(960, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_derecha.setFont(font)
        self.btn_derecha.setObjectName("btn_derecha")
        self.btn_centro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_centro.setGeometry(QtCore.QRect(820, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_centro.setFont(font)
        self.btn_centro.setObjectName("btn_centro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)




        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)
        # para referir al mismo axes

        self.verticalLayout.addWidget(self.canvas)





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_action.setText(_translate("MainWindow", "INICIAR"))
        self.btn_arriba.setText(_translate("MainWindow", "ARRIBA"))
        self.btn_izquierda.setText(_translate("MainWindow", "IZQUIERDA"))
        self.btn_abajo.setText(_translate("MainWindow", "ABAJO"))
        self.btn_derecha.setText(_translate("MainWindow", "DERECHA"))
        self.btn_centro.setText(_translate("MainWindow", "CENTRO"))

