import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Formula_General.ui"  # Nombre del archivo aquí.

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
        A = int(self.txt_valorA.text())
        B = int(self.txt_valorB.text())
        C = int(self.txt_valorC.text())

        print("A: ", A, " B: ", B, " C:", C)

        #formula  (-b+- raiz(b**2 -4ac) ) / 2a

        p1 = B ** 2
        p2 = -4  * A * C
        p3 = p1 - p2 #discrminante

        import math as m
        raiz_discriminante = m.sqrt(p3)

        dosA = 2 * A

        X1 = (-B + raiz_discriminante) / dosA
        X2 = (-B - raiz_discriminante) / dosA



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

