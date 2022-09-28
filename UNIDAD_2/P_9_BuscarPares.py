import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_9_BuscarPares.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial
        self.btn_validar.clicked.connect(self.validar)

        self.imagenesBuscar = [
            ":/Intro/UAT-Logotipo202.png",
            ":/Principal/broly.jpg",
            ":/Principal/vegeta.jpg"
        ]

        self.imagenesUsuario = [
            ":/Intro/UAT-Logotipo202.png",
            ":/Principal/broly.jpg",
            ":/Principal/vegeta.jpg"
        ]

    #############################################################################
        self.generarImagenAleatorioNueva()
    #############################################################################

        self.sel_imagen_usuario.valueChanged.connect(self.cambiaImagen)

        self.sel_imagen_usuario.setMaximum(len(self.imagenesUsuario)-1)
        self.sel_imagen_usuario.setMinimum(0)
        self.sel_imagen_usuario.setSingleStep(1)

        # indice del usuario
        self.sel_imagen_usuario.setValue(0)
        self.indice_del_usuario = 0

    # Área de los Slots
    def generarImagenAleatorioNueva(self):
        # obtiene un indice aleatorio para seleccionar a la imagen
        import random as rnd
        ## genera un numero aleatorio entre 0 y n
        self.indice_a_buscar = rnd.randint(0, len(self.imagenesBuscar) - 1)

        # establece la imagen aleatoria en el apartado correspondiente
        self.lb_imagenBuscar.setPixmap(
            QtGui.QPixmap(
                self.imagenesBuscar[self.indice_a_buscar]
            )
        )

    def validar(self):
        if self.indice_del_usuario == self.indice_a_buscar:
            self.mensaje("CORRECTO")

            print(len(self.imagenesBuscar))
            del self.imagenesBuscar[self.indice_a_buscar]
            print(len(self.imagenesBuscar))

            if len(self.imagenesBuscar) != 0:
                self.generarImagenAleatorioNueva()
            else:
                self.mensaje("Fin del Juego")

        else:
            self.mensaje("INCORRECTO")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

    def cambiaImagen(self):
        #actualiza el indice del usuario con base en el valor del slider
        self.indice_del_usuario = self.sel_imagen_usuario.value()

        self.lb_imageUsuario.setPixmap(
            QtGui.QPixmap(
                self.imagenesUsuario[self.indice_del_usuario]
            )
        )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

