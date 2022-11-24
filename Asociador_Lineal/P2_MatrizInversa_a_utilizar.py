#procedimiento para obtener la matriz psuedoinversa cuando el numero de filas
# es menor que el numero de columnas

import numpy as n

archivo = open("instancia_claseExplicacion.txt")
contenido = archivo.readlines()

print("Entradas:")
X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]
print(X)

print("Salidas:")
Y = contenido[3+int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]
print(Y)

X = n.array(X)
Y = n.array(Y)

print("\n\n\n")
print("X: ")
print(X)
print("Y:")
print(Y)

print("\n\n\n")

#X^+ = X^t (X*X^t)^-1

Paso1 = X.dot(X.T)   #X*X^t
Paso2 = n.linalg.inv(Paso1)   #(X*X^t)^-1
Xpseudo = X.T.dot(Paso2)      #X^t (X*X^t)^-1

print("Pseudoinversa de X: ")
print(Xpseudo)

print("COMPROBACIÓN:")
#C = Xpseudo.dot(X)
#print(C)

#print("Obtencion de I:")
C = X.dot(Xpseudo)
print(C)
