import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_12_Examen_Sumas_V3.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial
        self.btn_validar.clicked.connect(self.validar)

        self.resultado_suma_actual = 0

        self.contSuma = 1

        self.generaSuma()

        self.tiempo_transcurrido = 0
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control_tiempo)
        self.segundoPlano.start(100) #porque es cada segundo

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        ####
        self.txt_resultado.setMinimum(0)
        self.txt_resultado.setMaximum(1000)
        self.txt_resultado.setValue(0)
        self.txt_resultado.setSingleStep(1)

    # Área de los Slots
    def control_tiempo(self):

        minutos = str(self.tiempo_transcurrido//60)
        segundos = str(self.tiempo_transcurrido%60)

        minutos = "0" + minutos if len(minutos)==1 else minutos
        segundos = "0" + segundos if len(segundos) == 1 else segundos

        compuesta = str(minutos) + ":" + str(segundos)

        print(self.tiempo_transcurrido)
        self.txt_tiempo_transcurrid.display(compuesta)
        self.tiempo_transcurrido+=1

    def generaSuma(self):
        self.txt_suma_actual.setText(str(self.contSuma))
        self.contSuma+=1

        import random as rnd
        val1 = rnd.randint(0,10)
        val2 = rnd.randint(0, 10)
        self.txt_val1.setText(str(val1))
        self.txt_val2.setText(str(val2))

        self.resultado_suma_actual = val1 + val2


    def validar(self):
        val_ingresado_usuario = str(self.txt_resultado.value())

        if val_ingresado_usuario != "":
            val_ingresado_usuario = int(val_ingresado_usuario)
            if val_ingresado_usuario == self.resultado_suma_actual:
                #es correcto
                self.mensaje("Es correcto el resultado")

                self.progressBar.setValue(self.progressBar.value()+10)

                totSumas_a_realizar = 10
                if self.contSuma != totSumas_a_realizar + 1:
                    self.generaSuma()
                else:
                    self.segundoPlano.stop()
            else:
                #es incorrecto
                self.mensaje("Es inccorrecto el resultado")

            self.txt_resultado.setValue(0) #limpiamos el valor ingresado por el usuario

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

