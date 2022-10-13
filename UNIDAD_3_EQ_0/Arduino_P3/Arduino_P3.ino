//Leer un numero e imprimir su cuadrado
//El se reiniciara una vez que hay culminado

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}

int cuadrado;
int valor;
void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()>0){ //si existe informacion en el buffer
    valor = Serial.readString().toInt();

    cuadrado = valor * valor;
    Serial.println("El cuadrado de " + String(valor) + " es: " + String(cuadrado));
  }


  delay(100);

}
