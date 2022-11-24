

nombre_archivo = "potenciometro.txt"
archivo = open(nombre_archivo)

contenido = archivo.readlines()

print(contenido)

##conversion a lista de numeros

datos = [int(i) for i in contenido]

print(datos)

prom = sum(datos)/len(datos)
