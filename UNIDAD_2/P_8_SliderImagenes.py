import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_8_SliderImagenes.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial
        self.btn_accion.clicked.connect(self.controlSlider)

        self.hiloSecundario = QtCore.QTimer()
        self.hiloSecundario.timeout.connect(self.manejadorSegundoPlano)

        self.contador = 0

        self.imagenes = {
            #0: [":/Intro/UAT-Logotipo202.png"],
            0: ":/Principal/broly.jpg",
            1: ":/Principal/vegeta.jpg"
        }

    # Área de los Slots
    def controlSlider(self):
        etiqueta = self.btn_accion.text() #INICIAR   DETENER
        if etiqueta == "INICIAR":
            self.btn_accion.setText("DETENER")
            #se inicia el timer
            self.hiloSecundario.start(1000)
        else: #detener
            self.btn_accion.setText("INICIAR")
            #se detiene el timer
            self.hiloSecundario.stop()
            self.lb_imagen.setPixmap(QtGui.QPixmap(":/Intro/UAT-Logotipo202.png"))

        #self.val_n = int(self.txt_n.text())#obtencion de valor de n
        #self.hiloSecundario.start(500)

    def manejadorSegundoPlano(self):
        ruta = self.imagenes[self.contador]
        print(ruta)
        self.lb_imagen.setPixmap(QtGui.QPixmap(ruta))

        self.contador += 1 #decrementa uno cada tick

        if self.contador == 2:
            self.contador = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

