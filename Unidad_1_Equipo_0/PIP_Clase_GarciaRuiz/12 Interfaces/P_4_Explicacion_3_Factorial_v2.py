import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Factorial.ui"  # Nombre del archivo aquí.

Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

