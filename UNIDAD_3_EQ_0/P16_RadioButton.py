import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_16_RadioButton.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_Mujer.clicked.connect(self.Mujer)
        self.rb_Hombre.clicked.connect(self.Hombre)
        self.rb_Otro.clicked.connect(self.Otro)

        self.rb_Mujer_2.clicked.connect(self.Mujer_2)
        self.rb_Hombre_2.clicked.connect(self.Hombre_2)
        self.rb_Otro_2.clicked.connect(self.Otro_2)

        self.rb_Soltero.toggled.connect(self.Soltero)
        self.rb_Casado.toggled.connect(self.Casado)
        self.rb_UnionLibre.toggled.connect(self.UnionLibre)

        self.rb_Mujer.setChecked(True)
        self.rb_Mujer_2.setChecked(True)
        self.rb_Soltero.setChecked(True)

    def Mujer(self):
        v =  self.rb_Mujer.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Mujer")
    def Hombre(self):
        v = self.rb_Hombre.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Hombre")
    def Otro(self):
        v = self.rb_Otro.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Otro")

    def Mujer_2(self):
        v =  self.rb_Mujer_2.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Mujer_2")
    def Hombre_2(self):
        v = self.rb_Hombre_2.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Hombre_2")
    def Otro_2(self):
        v = self.rb_Otro_2.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Otro_2")

    def Soltero(self):
        v = self.rb_Soltero.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Soltero")
    def Casado(self):
        v = self.rb_Casado.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Casado")
    def UnionLibre(self):
        v = self.rb_UnionLibre.isChecked()
        print("Estado: " + str(v) + " Opc: " + "Union Libre")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())