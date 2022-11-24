import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "Prog_17_CheckBox.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cb_leer.clicked.connect(self.leer)
        self.cb_jugar.clicked.connect(self.jugar)
        self.cb_peliculas.clicked.connect(self.peliculas)

        self.cb_escuela.toggled.connect(self.escuela)
        self.cb_trabajar.toggled.connect(self.trabajar)
        self.cb_ejercicio.toggled.connect(self.ejercicio)

    def leer(self):
        v = self.cb_leer.isChecked()
        print("Estado: " + str(v) + " Opc.: LEER")
    def jugar(self):
        v = self.cb_jugar.isChecked()
        print("Estado: " + str(v) + " Opc.: JUGAR")
    def peliculas(self):
        v = self.cb_peliculas.isChecked()
        print("Estado: " + str(v) + " Opc.: PELICULAS")

    def escuela(self):
        v = self.cb_escuela.isChecked()
        print("Estado: " + str(v) + " Opc.: ESCUELA")
    def trabajar(self):
        v = self.cb_trabajar.isChecked()
        print("Estado: " + str(v) + " Opc.: TRABAJAR")
    def ejercicio(self):
        v = self.cb_ejercicio.isChecked()
        print("Estado: " + str(v) + " Opc.: EJERCICIO")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())