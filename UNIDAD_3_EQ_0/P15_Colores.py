import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "Prog_15_Colores.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #R
        self.hs_R.setMinimum(0)
        self.hs_R.setMaximum(255)
        self.hs_R.setSingleStep(1)
        self.hs_R.setValue(0)

        #G
        self.hs_G.setMinimum(0)
        self.hs_G.setMaximum(255)
        self.hs_G.setSingleStep(1)
        self.hs_G.setValue(0)

        #B
        self.hs_B.setMinimum(0)
        self.hs_B.setMaximum(255)
        self.hs_B.setSingleStep(1)
        self.hs_B.setValue(0)

        self.txt_R.setText("0")
        self.txt_G.setText("0")
        self.txt_B.setText("0")

        self.hs_R.valueChanged.connect(self.cambioR)
        self.hs_G.valueChanged.connect(self.cambioG)
        self.hs_B.valueChanged.connect(self.cambioB)

        self.R = 0
        self.G = 0
        self.B = 0

        self.cambioColor()

    def cambioR(self):
            v = self.hs_R.value()
            self.R = v
            self.txt_R.setText(str(v))
            self.cambioColor()

    def cambioG(self):
            v = self.hs_G.value()
            self.G = v
            self.txt_G.setText(str(v))
            self.cambioColor()

    def cambioB(self):
        v = self.hs_B.value()
        self.B = v
        self.txt_B.setText(str(v))
        self.cambioColor()

    def cambioColor(self):
        comando = "background-color:rgb(" + str(self.R) + "," \
                                          + str(self.G) + "," \
                                          + str(self.B) + ");"
        self.btn_color.setStyleSheet(comando);

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())