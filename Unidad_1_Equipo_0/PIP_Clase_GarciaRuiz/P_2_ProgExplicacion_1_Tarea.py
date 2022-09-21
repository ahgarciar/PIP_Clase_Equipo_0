import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Interfaz_1.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_next.clicked.connect(self.check_edad)

    # Área de los Slots
    def check_edad(self):
        try:
            print("hola")
            edad = self.txt_edad.text()  #cadena de caracteres
            edad = str(edad)
            print(edad)
            edad = int(edad)

            if edad >= 18:
                #puede votar
                self.mensaje("Puede VOTAR")
            else:
                #no se puede votar
                self.mensaje("NO Puede VOTAR")
        except Exception as ex:
            print(ex)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(str(msj))
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

