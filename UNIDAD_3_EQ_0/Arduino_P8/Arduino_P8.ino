//izquierda
//derecha
//centro ->> A0

// Tierra / 5V van de manera intercambiable en izquierda o derecha

//Pin Digital -> Arduino UNO: 0 al 13. 
//El Pin 0 y 1, no se pueden utilizar como puertos digitales cuando se utilizara comunicacion serial

int LED = 13; //Arduino cuenta con un LED integrado en el Pin 13 que puede ser utilizado para pruebas

int valor;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT); //Se debe establecer el modo de trabajo del Pin Digital

  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}


void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);

}
