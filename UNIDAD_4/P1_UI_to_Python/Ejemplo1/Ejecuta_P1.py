import sys

from PyQt5 import QtWidgets

from P1_UI_to_Python.Ejemplo1 import P1_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_saludar.clicked.connect(self.saludar)

    def saludar(self):
        self.mensaje("Hola Mundo")
        self.txt_saludar.setText("Hola Mundo")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())