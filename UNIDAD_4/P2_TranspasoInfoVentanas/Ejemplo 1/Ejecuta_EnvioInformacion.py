import sys
from PyQt5 import uic, QtWidgets, QtCore

##########################################################################

qtCreatorFile1 = "Main_EnvioInfo.ui"  # Nombre del archivo aquí.
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())

        r = a + b

        self.dialogo = MyDialog()
        #self.dialogo.setModal(True)

        self.dialogo.txt_resultado.setText(str(r))

        self.dialogo.show()

##########################################################################

qtCreatorFile3 = "Second_EnvioInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion

    # Área de los Slots


##########################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
