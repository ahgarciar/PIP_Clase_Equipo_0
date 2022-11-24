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

    def agregar(self):
        nombre = self.txt_alumno.text()
        self.listWidget.addItem(str(nombre)) #unicamente puede guardar cadenas de caracteres


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())