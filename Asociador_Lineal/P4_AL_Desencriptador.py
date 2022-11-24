
#Asociador Lineal

#X = Entradas
#Y = Salidas
#W = Y*XPseudoInversa

import numpy as n

archivo = open("instancia_desencriptador.txt")
contenido = archivo.readlines()

print(contenido)

X = contenido[3:3+int(contenido[1])]
X = [i.split(",") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3+int(contenido[1]):]
Y = [i.split(",") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

print("X:")
print(X)

print("Y:")
print(Y)

Paso1 = X.dot(X.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = X.T.dot(Paso2)

W = Y.dot(Xpseudo)

print("W:")
print(W)


###PRUEBA DE LA FUNCIOANLIDA DEL ASOCIADOR LINEA
#VAMOS A PROBAR CADA UNO DE LOS CASOS PARA OBSERVAR SI LA RED ES CAPAZ DE
#CLASIFICAR CORRECTAMENTE

print("Prueba...")

casosCorrectos = 0


for i in range(X.shape[1]):
    print("Prueba del Caso ", i + 1)
    casoi = X[:,i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    import math as m
    Ycasoi = [list(map(m.ceil, Ycasoi))]
    print("Salidas Generadas Redondeadas hacia arriba")
    print(Ycasoi)

    print("Salidas Real: ")
    Yrealcasoi = Y[:,i]
    print(Yrealcasoi)

    r = True
    for j in range(len(Yrealcasoi)):
        if Yrealcasoi[j] != Ycasoi[0][j]: #Ycasoi se esta considerando como una matriz de 1 x n
            r = False
            break

    casosCorrectos += 1 if r else 0



    print("Clave Asignada: ", list(map(chr, Ycasoi[0])))
    print("Clave Real: ", list(map(chr, Yrealcasoi)))
    print()

print("Total de Casos Analizados: ", X.shape[1])
print("Total de Casos Correctos: ", casosCorrectos)

print("Eficiencia del Asociador Lineal: ", casosCorrectos/X.shape[1]*100.0)


#UTILIZACIÓN DEL ASOCIADOR LINEAL...
print("\n\nPrueba de funcionamiento del asociador lineal: ")

#x = [106, 117, 97, 110]
x = [112, 97, 99, 111]
#x = [49, 57, 57, 49]

#x = [49, 117, 99, 112]
x = n.array(x)
print("x: ")
print(x)

Ycasox = W.dot(x)

print("y: ")
print(Ycasox)
#119, 130, 110, 123
#125 110 112 124
#62 70 70 62

Ycasox = [list(map(m.ceil, Ycasox))]
print(Ycasox)
print("Clave Asignada: ", list(map(chr, Ycasox[0])))

print("valor diferencia: ")
valorClave = Ycasox - x
print(valorClave)