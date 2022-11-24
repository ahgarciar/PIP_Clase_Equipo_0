import sys

from PyQt5 import QtWidgets, QtCore

from P1_UI_to_Python.Ejemplo2 import P2_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_saludar.clicked.connect(self.saludar)

        self.btn_nuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nuevo.setGeometry(QtCore.QRect(290, 80, 191, 61))
        self.btn_nuevo.setObjectName("btn_nuevo")

        self.btn_nuevo.setText("NUEVO SALUDO")

        self.btn_nuevo.clicked.connect(self.saludar)


    def saludar(self):
        try:
            #self.mensaje("Hola Mundo")
            self.lineEdit.setText("Hola Mundo")

            self.btn_nuevo.hide() ## opuesto a show

        except Exception as e:
            print(e)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())