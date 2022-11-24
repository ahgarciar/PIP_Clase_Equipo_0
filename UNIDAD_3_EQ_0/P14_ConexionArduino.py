import sys

import serial as Serial

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P14_ConexionArduino.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

    def accion(self):
        texto = self.btn_accion.text()
        if texto == "CONECTAR":
            self.btn_accion.setText("DESCONECTAR")
            if self.arduino == None:
                self.arduino = Serial.Serial("/dev/cu.usbserial-10", baudrate=9600, timeout=1)
        elif texto == "DESCONECTAR":
            self.btn_accion.setText("RECONECTAR")
            if self.arduino != None and self.arduino.isOpen():
                self.arduino.close()
        else: #texto == "RECONECTAR"
            self.btn_accion.setText("DESCONECTAR")
            if self.arduino != None and not self.arduino.isOpen():
                self.arduino.open()

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())