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
            1:["Broly", 22, 30, 28],
            2:["Vegeta", 27, 60, 40]
        }

    # Área de los Slots
    def cambia_valor(self):
        try:
            indice = self.verticalSlider.value() #devuelve un entero
            print("indice: ", indice)
            self.txt_valor.setText(str(indice))

            #datos por defecto ##########################
            nombre = "SIN SELECCION"
            edad = 0
            peleas_realizadas = 0
            peleas_ganadas = 0
            #############################################
            if indice != 0: #si selecciono un indice valido (1 o 2)
                datosPersonales = self.datosPersonaje[indice] #todos los datos del personaje
                print("Datos Personales: ", datosPersonales)
                nombre = datosPersonales[0]
                edad = datosPersonales[1]
                peleas_realizadas = datosPersonales[2]
                peleas_ganadas = datosPersonales[3]

            ##asignacion de datos personales a la interfaz
            self.txt_nombre.setText(nombre)
            # como el dato es numero, hay que pasarlo a letra (cadenas de caracteres)
            self.txt_edad.setText(str(edad))
            self.txt_peleas_realizadas.setText(str(peleas_realizadas))
            self.txt_peleas_ganadas.setText(str(peleas_ganadas))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

