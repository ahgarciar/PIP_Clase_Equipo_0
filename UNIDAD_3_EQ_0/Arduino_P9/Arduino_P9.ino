//izquierda
//derecha
//centro ->> A0

// Tierra / 5V van de manera intercambiable en izquierda o derecha

//Pin Digital -> Arduino UNO: 0 al 13. 
//El Pin 0 y 1, no se pueden utilizar como puertos digitales cuando se utilizara comunicacion serial

int LED = 13; //Arduino cuenta con un LED integrado en el Pin 13 que puede ser utilizado para pruebas



void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT); //Se debe establecer el modo de trabajo del Pin Digital

  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:

 if(Serial.available()>0) //Si hay informacion en el buffer
{
  valor = Serial.readString().toInt(); //Considerar usuarios perfectos

  digitalWrite(LED, valor); //valor => 0 = Apagado.  1 = Prendido
}

delay(100);


}
