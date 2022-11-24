import sys

from PyQt5 import QtWidgets

from P3_Graficacion import Plantilla_Grafica as grafica

import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_graficar.clicked.connect(self.graficar)
        self.btn_titulo.clicked.connect(self.titulo)
        self.btn_grilla.clicked.connect(self.grilla)
        self.btn_limpiar.clicked.connect(self.limpiar)

        #                              text      data
        self.cb_estiloLinea.addItem("Estilo: :", ":")
        self.cb_estiloLinea.addItem("Estilo: -", "-")
        self.cb_estiloLinea.addItem("Estilo: --", "--")
        self.cb_estiloLinea.addItem("Estilo: -.", "-.")
        self.cb_estiloLinea.currentIndexChanged.connect(self.estiloLinea)

        self.cb_ColorLinea.addItem("Negro", "black")
        self.cb_ColorLinea.addItem("Rojo", "red")
        self.cb_ColorLinea.addItem("Azul", "blue")
        self.cb_ColorLinea.addItem("Verde", "green")
        self.cb_ColorLinea.currentIndexChanged.connect(self.colorLinea)

        self.sp_anchoLinea.setValue(1)
        self.sp_anchoLinea.setMaximum(10)
        self.sp_anchoLinea.setMinimum(1)
        self.sp_anchoLinea.setSingleStep(1)
        self.sp_anchoLinea.valueChanged.connect(self.anchoLinea)

        #PARAMETROS SELECCIONADOS:
        self.estiloLinea = ":"
        self.colorLinea = "black"
        self.anchoLinea = 1

        ################################################################################

        self.sp_Xmin.setValue(0)
        self.sp_Xmin.setMaximum(10000)
        self.sp_Xmin.setMinimum(-10000)
        self.sp_Xmin.setSingleStep(1)
        self.sp_Xmin.valueChanged.connect(self.minX)

        self.sp_Xmax.setValue(10)
        self.sp_Xmax.setMaximum(10000)
        self.sp_Xmax.setMinimum(-10000)
        self.sp_Xmax.setSingleStep(1)
        self.sp_Xmax.valueChanged.connect(self.maxX)

        self.sp_divisionesX.setValue(10)
        self.sp_divisionesX.setMaximum(10)
        self.sp_divisionesX.setMinimum(1)
        self.sp_divisionesX.setSingleStep(1)
        self.sp_divisionesX.valueChanged.connect(self.divisionesX)

        self.sp_Ymin.setValue(0)
        self.sp_Ymin.setMaximum(10000)
        self.sp_Ymin.setMinimum(-10000)
        self.sp_Ymin.setSingleStep(1)
        self.sp_Ymin.valueChanged.connect(self.minY)

        self.sp_Ymax.setValue(10)
        self.sp_Ymax.setMaximum(10000)
        self.sp_Ymax.setMinimum(-10000)
        self.sp_Ymax.setSingleStep(1)
        self.sp_Ymax.valueChanged.connect(self.maxY)

        self.sp_divisionesY.setValue(10)
        self.sp_divisionesY.setMaximum(10)
        self.sp_divisionesY.setMinimum(1)
        self.sp_divisionesY.setSingleStep(1)
        self.sp_divisionesY.valueChanged.connect(self.divisionesY)

        #PARAMETROS POR DEFECTO
        self.xMax = 10
        self.xMin = 1
        self.xDivisiones = 10
        self.yMax = 10
        self.yMin = 1
        self.yDivisiones = 10

        #PARA CORREGIR EL ERROR DE LA GRILLA
        self.btn_grilla.setText("ON")

    # Área de los Slots
    def minX(self):
        self.xMin = self.sp_Xmin.value()
        self.limpiar()
        self.graficar()
    def maxX(self):
        self.xMax = self.sp_Xmax.value()
        self.limpiar()
        self.graficar()
    def divisionesX(self):
        self.xDivisiones = self.sp_divisionesX.value()
        self.limpiar()
        self.graficar()
    def minY(self):
        self.yMin = self.sp_Ymin.value()
        self.limpiar()
        self.graficar()
    def maxY(self):
        self.yMax = self.sp_Ymax.value()
        self.limpiar()
        self.graficar()
    def divisionesY(self):
        self.yDivisiones = self.sp_divisionesY.value()
        self.limpiar()
        self.graficar()


    def estiloLinea(self):
        estilo = self.cb_estiloLinea.currentData()
        self.estiloLinea =  estilo

        self.limpiar()
        self.graficar()

    def colorLinea(self):
        color = self.cb_ColorLinea.currentData()
        self.colorLinea = color

        self.limpiar()
        self.graficar()


    def anchoLinea(self):
        ancho = self.sp_anchoLinea.value()
        self.anchoLinea = ancho

        self.limpiar()
        self.graficar()


    def limpiar(self):
        plt.cla()    #borra_todo
        self.canvas.draw()  #vuelve a dibujar

    def titulo(self):
        t = self.txt_titulo.text()
        self.ax.set_title(t)  #establece el titulo

        self.canvas.draw()    # aplica los cambios

    def grilla(self):
        texto = self.btn_grilla.text()
        if texto == "OFF":
            self.btn_grilla.setText("ON")
            plt.grid(False)
        else:
            self.btn_grilla.setText("OFF")
            plt.grid(True)

        self.canvas.draw()

    def graficar(self):
        polinomio = self.txt_polinomio.text()
        polinomio = polinomio.replace("^","**")

        #x = [i for i in range(-5,6)] #[-5 5]

        #x = []
        #for i in range(self.xMin, self.xMax+1):
        #    x.append(i)

        x = [i for i in range(self.xMin, self.xMax+1)]
        print("Valores de X: ")
        print(x)

        #y = polinomio.replace("x","*("+str(x[0])+")")
        y = [eval(polinomio.replace("x","*("+str(i)+")")) for i in x]
        print("Valores de Y: ")
        print(y)

        #self.ax.plot(x,y)
        #self.ax.plot(x, y,"g*--")
        self.ax.plot(x, y,

                 linestyle= self.estiloLinea,  #: - -- -.
                 color= self.colorLinea,  # color de la linea
                 linewidth= self.anchoLinea,  # tamaño de la linea
                 marker="x",  # o . *  x   1
                 markersize=12,
                 markerfacecolor="yellow",  # color interno del marcador
                 markeredgewidth=2,  # tamaño del borde del marcador
                 markeredgecolor="red",  # color del borde del marcador
                 dash_capstyle="butt",  # dash or solid : "butt" "round" "projecting"
                 dash_joinstyle="miter"  # dash or solid : "miter" "round" "bevel"
                 )

        #Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax+1)
        self.ax.set_ylim(self.yMin, self.yMax + 1)

        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")

        #####################################################-->> EQUAL WIDTH
        #Op1:
        # una posibilidad para establecer los ticks sería:
        # Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee
        totalelementoX  = 100
        totalDivisiones = 10
        #totalelementosenX/totaldivisionesDeseadas = 10
        #mediante un ciclo se obtiene:

        #si comienzo con xmin en 0 seria:
        #xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        #Op2: si comienzo con xmin en n seria:
        xtick = []
        for i in range(-30, 30+1, 10):
            xtick.append(i)
        print("Ticks para X: ")
        print(xtick)

        #Op3:
        xtick = [2, 5, 15, 25, 35, 45, 55, 65, 75, 85]
        #self.ax.set_xticks(xtick)

        #Op4:
        #self.ax.set_yticks(y)   #NOTA.. CHECK!


        #####################################################

        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
