import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_2_Control_Dial.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals - Configuracion Inicial
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(1)

        valor = 0
        self.dial.setValue(valor)
        self.txt_valor.setText(str(valor))

        self.dial.valueChanged.connect(self.cambia_valor)

    # Área de los Slots
    def cambia_valor(self):
        try:
            v = self.dial.value() #devuelve un entero
            print(v)
            self.txt_valor.setText(str(v))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

