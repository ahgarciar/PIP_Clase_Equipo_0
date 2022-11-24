import sys

from PyQt5 import QtWidgets

from P6_Ejemplo_JuegoGrafica import Plantilla_Juego as grafica

import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action)

        self.btn_arriba.clicked.connect(self.arriba)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_centro.clicked.connect(self.centro)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_abajo.clicked.connect(self.abajo)

        ################################################################################

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5


        #################################################################################
        #                Jugador  Computadora
        self.personajes = [[0, 0], [0, 0], [0,0]]

        ##############################################

        self.limpiar()


    # Área de los Slots
    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.btn_action.setText("DETENER")

            #jugador
            self.personajes[0] = [0, 0] #vuelve al jugar al centro

            import random as rnd
            #computadora
            #self.personajes[1] = [rnd.randrange(self.xMin, self.xMax), rnd.randrange(self.yMin, self.yMax)]

            self.totalEnemigos = len(self.personajes)-1 #para saber cuando el juego ha terminado

           #Para ubicar  a los enemigos:
            for i in range(1, len(self.personajes)):
                self.personajes[i] = [
                    rnd.randrange(self.xMin, self.xMax),
                    rnd.randrange(self.yMin, self.yMax)
                ]

            self.graficar()
        else:
            self.btn_action.setText("INICIAR")
            self.limpiar()

    #Personajes[0] = Jugador
    #Personajes[0][0] = para X
    #Personajes[0][1] = para Y

    def arriba(self):#     v  => valor de y
        self.personajes[0][1] = self.personajes[0][1] + 1
        self.limpiar()
        self.graficar()

    def izquierda(self):#  v  => valor de x
        self.personajes[0][0] -= 1
        self.limpiar()
        self.graficar()

    def centro(self):
        self.personajes[0][0] = 0
        self.personajes[0][1] = 0
        self.limpiar()
        self.graficar()

    def derecha(self):#    v  => valor de x
        self.personajes[0][0] += 1
        self.limpiar()
        self.graficar()

    def abajo(self):#      v  => valor de y
        self.personajes[0][1] -= 1
        self.limpiar()
        self.graficar()

    def limpiar(self):
        plt.cla() #BORRA_TODO EL GRAFICO

        x = [i for i in range(self.xMin, self.xMax + 1)] #GENERA LOS TICKS
        y = [i for i in range(self.yMin, self.yMax + 1)] #GENERA LOS TICKS

        self.ax.set_xticks(y)
        self.ax.set_yticks(y)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)  #CUADRICULA

        self.canvas.draw() #DIBUJAR EL GRAFICO


    def graficar(self):

        # POSICIONA A LA COMPUTADORA EN EL GRAFICO
        for i in range(1, len(self.personajes)):
            self.ax.plot(self.personajes[i][0], self.personajes[i][1],
                         marker="o",  # o . *  x   1
                         markersize=8,
                         markerfacecolor="green",  # color interno del marcador
                         markeredgewidth=1,  # tamaño del borde del marcador
                         markeredgecolor="black",  # color del borde del marcador
                         )

        #POSICIONA AL USUARIO EN LA GRAFICA
        self.ax.plot(self.personajes[0][0], self.personajes[0][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="yellow",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )


        self.canvas.draw() #DIBUJA EL GRAFICO

        #COMPRUEBA CADA QUE SE GRAFICA SI EL USUARIO ALCANZO A LA COMPUTADORA
        #SI LAS COORDENADAS DE AMBOS ESTAN EN LA MISMA POSICION, ENTONCES EL USUARIO ALCANZO
        # A LA COMPUTADORA..
        for i in range(1, len(self.personajes)):
            if self.personajes[0][0] == self.personajes[i][0] and self.personajes[0][1] == self.personajes[i][1]:

                self.personajes[i][0] = 1000
                self.personajes[i][1] = 1000

                self.totalEnemigos -= 1
                print("Enemigos Restantes:" + str(self.totalEnemigos))

                break;

        if self.totalEnemigos == 0:
            m = QtWidgets.QMessageBox()
            m.setText("Has Ganado")
            m.exec_()
            self.limpiar()
            self.btn_action.setText("INICIAR")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
