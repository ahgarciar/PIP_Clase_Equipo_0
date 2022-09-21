import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Interfaz_2.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        A_X = float(self.txt_puntoA_X.text())
        A_Y = float(self.txt_puntoA_Y.text())
        B_X = float(self.txt_puntoB_X.text())
        B_Y = float(self.txt_puntoB_Y.text())

        parte1 = (A_X - B_X) ** 2
        parte2 = (A_Y - B_Y) ** 2

        parte3 = parte1 + parte2

        import math as m
        distancia = m.sqrt(parte3)

        self.mensaje(distancia)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(str(msj))
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

