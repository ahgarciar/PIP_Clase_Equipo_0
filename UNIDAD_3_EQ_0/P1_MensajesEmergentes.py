import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_1_MensajesEmergentes.ui" # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_basico.clicked.connect(self.basico)

        self.btn_op_defecto.clicked.connect(self.op_defecto)
        self.btn_texto_detallado.clicked.connect(self.texto_detallado)

        self.btn_informacion.clicked.connect(self.informacion)
        self.btn_pregunta.clicked.connect(self.pregunta)
        self.btn_advertencia.clicked.connect(self.advertencia)
        self.btn_critico.clicked.connect(self.critico)

        self.btn_botones_personalizados.clicked.connect(self.botones_personalizados)



    def basico(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hola Mundo")
        resp = msgBox.exec_()
        print(f"Respuesta: {resp}")

    def op_defecto(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Save |
                                  QtWidgets.QMessageBox.Discard |
                                  QtWidgets.QMessageBox.Cancel |
                                  QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Save)
        resp = msgBox.exec()
        print(f"Respuesta: {resp}");


    def texto_detallado(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hola Mundo")
        msgBox.setDetailedText("Texto Descriptivo")
        resp = msgBox.exec_()
        print(f"Respuesta: {resp}");

    def informacion(self):
        resp = QtWidgets.QMessageBox.information(self, "Informacion",
                                             '''Informacion!!!!
                                               
                                             ''',
                                             QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Abort)

        if resp == QtWidgets.QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")

    def pregunta(self):
        resp = QtWidgets.QMessageBox.question(self, "Pregunta",
                                                 '''Pregunta!!!!
                                                   
                                                 ''',
                                                 QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Abort)

        if resp == 1024: #QtWidgets.QMessageBox.Ok:
            print("ok")
        elif resp == QtWidgets.QMessageBox.Cancel:
            print("cancel")
        else:
            print("abort")

    def advertencia(self):
        resp = QtWidgets.QMessageBox.warning(self, "Advertencia",
                                         '''Advertencia!!!!
                                           
                                         ''', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Abort)

        if resp == QtWidgets.QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")

    def critico(self):
        resp = QtWidgets.QMessageBox.critical(self, "Critico",
            '''Este es el contenido
                del Mensaje critico!! :D! 
            ''',
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        if resp == QtWidgets.QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")

    def botones_personalizados(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Personalizado?")

        btnSi = QtWidgets.QPushButton('Si')
        msgBox.addButton(btnSi, QtWidgets.QMessageBox.YesRole)

        btnNo = QtWidgets.QPushButton('No')
        msgBox.addButton(btnNo, QtWidgets.QMessageBox.NoRole)

        resp = msgBox.exec_()
        print(f"Respuesta: {resp}");



    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Mensaje", "Seguro quiere salir?", QtWidgets.QMessageBox.Yes,
                                           QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())