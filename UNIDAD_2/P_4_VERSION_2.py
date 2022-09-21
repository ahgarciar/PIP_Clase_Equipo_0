import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_4_Control_ImagenesInformacion.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(2)
        self.verticalSlider.setSingleStep(1)

        valor = 0
        self.verticalSlider.setValue(valor)
        self.txt_valor.setText(str(valor))

        self.verticalSlider.valueChanged.connect(self.cambia_valor)

        self.datosPersonaje = {
            0: ["SIN SELECCION", 0, 0, 0],  #CUANDO NO SE SELECCIONA UN PERSONAJE VALIDO
            1:["Broly", 22, 30, 28],
            2:["Vegeta", 27, 60, 40]
        }

    # Área de los Slots
    def cambia_valor(self):
        try:
            indice = self.verticalSlider.value() #devuelve un entero
            print("indice: ", indice)
            self.txt_valor.setText(str(indice))

            datosPersonales = self.datosPersonaje[indice] #todos los datos del personaje
            print("Datos Personales: ", datosPersonales)

            ##asignacion de datos personales a la interfaz
            self.txt_nombre.setText(datosPersonales[0])
            # como el dato es numero, hay que pasarlo a letra (cadenas de caracteres)
            self.txt_edad.setText(str(datosPersonales[1]))
            self.txt_peleas_realizadas.setText(str(datosPersonales[2]))
            self.txt_peleas_ganadas.setText(str(datosPersonales[3]))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

