##uso de modulo pyserial
import serial as s
###################################

import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P1_EscrituraSerial.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None

        self.btn_conexion.clicked.connect(self.conexion)

        self.btn_accion.clicked.connect(self.accion)

        self.btn_accion.setEnabled(False)

    def accion(self):
        v = self.btn_accion.text()
        if v == "PRENDER":
            self.btn_accion.setText("APAGAR")
            self.arduino.write("1".encode())
        else:
            self.btn_accion.setText("PRENDER")
            self.arduino.write("0".encode())

    def conexion(self):
        v = self.btn_conexion.text()
        if v == "CONECTAR": #pasa de desconectado a conectado
            self.btn_conexion.setText("DESCONECTAR")

            if self.arduino == None: #SI NUNCA ME HABIA CONECTADO
                com = "COM" + self.txt_com.text()
                self.arduino = s.Serial(com, baudrate=9600, timeout=1000) ##realiza la conexion
                # y la iniciliza
                self.txt_estado.setText("INICIALIZADA")

                self.btn_accion.setEnabled(True)

            elif not self.arduino.isOpen():
                self.arduino.open()
                self.txt_estado.setText("REESTABLECIDA")

                self.btn_accion.setEnabled(True)

        else: #pasa de conectado a desconectado
            self.btn_conexion.setText("CONECTAR")

            self.arduino.close()
            self.txt_estado.setText("CERRADA")

            self.btn_accion.setEnabled(False)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())