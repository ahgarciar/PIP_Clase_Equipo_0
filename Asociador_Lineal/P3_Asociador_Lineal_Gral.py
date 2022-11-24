
#Asociador Lineal

#X = Entradas
#Y = Salidas
#W = Y*XPseudoInversa

import numpy as n

archivo = open("instancia_claseExplicacion.txt")
contenido = archivo.readlines()

X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3+int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

Paso1 = X.dot(X.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = X.T.dot(Paso2)

W = Y.dot(Xpseudo)

print("X:")
print(X)

print("Y:")
print(Y)

print("W:")
print(W)


###PRUEBA DE LA FUNCIOANLIDA DEL ASOCIADOR LINEA
#VAMOS A PROBAR CADA UNO DE LOS CASOS PARA OBSERVAR SI LA RED ES CAPAZ DE
#CLASIFICAR CORRECTAMENTE

print("Prueba...")

casosCorrectos = 0

#CLASE SALIDA1  SALIDA 2  SALIDA 3
Clases = ["MAGO", "DUELISTA", "GUERRERO"]

for i in range(X.shape[1]): #para cada uno de los casos/registros de prueba
    print("Prueba del Caso ", i + 1)
    casoi = X[:,i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    print("Salidas Real: ")
    Yrealcasoi = Y[:,i]
    print(Yrealcasoi)

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos +=1

    print("Clase Asignada: ", Clases[IndexMaxYcasoi])
    print("Clase Real: ", Clases[IndexMaxYrealcasoi])
    print()

print("Total de Casos Analizados: ", X.shape[1])
print("Total de Casos Correctos: ", casosCorrectos)

print("Eficiencia del Asociador Lineal: ", casosCorrectos/X.shape[1]*100.0)


#UTILIZACIÓN DEL ASOCIADOR LINEAL...
print("\n\nPrueba de funcionamiento del asociador lineal: ")

#0 0 1  = GUERRERO
x = [78, 53, 11, 30, 86, 23]
y = "GUERRERO"

x = n.array(x)
Ycasox = W.dot(x)

print(Ycasox)
IndexMaxYcasoi = list(Ycasox).index(max(Ycasox))

print("Clase Asignada: ", Clases[IndexMaxYcasoi])

print("Correcto " if Clases[IndexMaxYcasoi] == y else "Incorrecto")
