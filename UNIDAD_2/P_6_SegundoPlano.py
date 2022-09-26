import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_6_SegundoPlano.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial

        self.btn_hiloPrincipal.clicked.connect(self.hiloPrincipal)
        self.btn_segundoPlano.clicked.connect(self.segundoPlano)

        self.hiloSecundario = QtCore.QTimer()
        self.hiloSecundario.timeout.connect(self.manejadorSegundoPlano)

        self.contadorcito = 0

    # Área de los Slots
    def hiloPrincipal(self):
        n = int(self.txt_n.text())
        import time as t
        for i in range(n, -1, -1): #de 10 a 0 de 1 en 1
            print(i)
            self.txt_contador.setText(str(i))
            t.sleep(0.5)

    def segundoPlano(self):
        self.hiloSecundario.start(500)

    def manejadorSegundoPlano(self):
        self.contadorcito += 1
        print("Ocurrio el Tick #", self.contadorcito)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

