
import serial as Serial

#arduino = Serial.Serial(port="COM10")
arduino = Serial.Serial(port="/dev/cu.usbserial-10", baudrate=9600, timeout=1)

print("Estado conexion: ", arduino.isOpen())


nombre_archivo = "archivo.txt"
archivo = open(nombre_archivo, "w")

for i in range(1, 101,1):
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","")
    if cadena != "":
        print(cadena)
        archivo.write(cadena)
        archivo.write("\n")

archivo.close()
