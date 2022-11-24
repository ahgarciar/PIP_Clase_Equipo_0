import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

from P1_UI_to_Python.Ejemplo3 import P3_PAR_IMPAR as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_checar.clicked.connect(self.checar)
        self.btn_limpiar.clicked.connect(self.limpiar)

    def checar(self):
        #######################################
        self.txt_resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_resultado.setGeometry(QtCore.QRect(200, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_resultado.setFont(font)
        self.txt_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_resultado.setObjectName("txt_resultado")
        self.txt_resultado.show() #se ocupa cuando se añadir el elemento en un lugar
                                  #diferente al constructor de la clase
        #######################################
        val = int(self.txt_n.text())
        if val % 2 == 0:
            self.txt_resultado.setText("PAR")
            print("PAR")
        else:
            self.txt_resultado.setText("IMPAR")
            print("IMPAR")

    def limpiar(self):
        self.txt_n.setText("2")
        self.txt_resultado.deleteLater() #elimina el elemento

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())