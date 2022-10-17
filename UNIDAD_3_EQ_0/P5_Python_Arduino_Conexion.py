
import serial as Serial

#arduino = Serial.Serial(port="COM10")
arduino = Serial.Serial(port="/dev/cu.usbserial-10", baudrate=9600, timeout=1)

print("Estado conexion: ", arduino.isOpen())

while True:
    cadena = arduino.readline()
    print(cadena)
    cadena = cadena.decode()
    print(cadena)
    print("\n")
