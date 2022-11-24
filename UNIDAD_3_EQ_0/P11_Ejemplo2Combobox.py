import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P11_Ejemplo2Combobox.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.comboBox.addItem("Gato",11) #Texto, data
        self.comboBox.addItem("Cuyo", 9)  # Texto, data
        self.comboBox.addItem("Perro", 19)  # Texto, data

        self.txt_totalElementos.setEnabled(False)

        totElementos = self.comboBox.count()
        self.txt_totalElementos.setText(str(totElementos))

        self.comboBox.setCurrentIndex(0)

        ##################################################################

        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_findData.clicked.connect(self.findData)
        self.btn_findText.clicked.connect(self.findText)
        self.btn_itemData.clicked.connect(self.itemData)
        self.btn_itemText.clicked.connect(self.itemText)

    def eliminar(self):
        indice = int(self.txt_indiceEliminar.text())
        self.comboBox.removeItem(indice)
        self.txt_totalElementos.setText(str(self.comboBox.count()))

    def findData(self):
        #   RETORNA EL INDICE EN EL QUE SE ENCUENTRA EL DATA QUE SE ESTA BUSCANDO
        data = int(self.txt_dataFind.text())
        v = self.comboBox.findData(data)
        self.mensaje(str(v))

    def findText(self):
        #   RETORNA EL INDICE EN EL QUE SE ENCUENTRA EL TEXTO QUE SE ESTA BUSCANDO
        texto = self.txt_TextFind.text()
        v = self.comboBox.findText(texto)
        self.mensaje(str(v))

    def itemData(self):
        #   RETORNA EL DATA ASOCIADO AL INDICE QUE SE INGRESA
        indice = int(self.txt_indiceItemData.text())
        v = self.comboBox.itemData(indice)
        self.mensaje(str(v))

    def itemText(self):
        #   RETORNA EL TEXTO ASOCIADO AL INDICE QUE SE INGRESA
        indice = int(self.txt_indiceItemText.text())
        v = self.comboBox.itemText(indice)
        self.mensaje(v)


    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()
        ##################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())