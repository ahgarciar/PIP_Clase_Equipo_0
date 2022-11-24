import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P9_ListWidget.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_agregar.clicked.connect(self.agregar)

        self.listaNombres = []

    def agregar(self):
        nombre = self.txt_alumno.text()

        if nombre not in self.listaNombres:
            self.listWidget.addItem(str(nombre)) #unicamente puede guardar cadenas de caracteres
            self.listaNombres.append(nombre)
        else:
            self.mensaje("El nombre ya existe en la lista")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())