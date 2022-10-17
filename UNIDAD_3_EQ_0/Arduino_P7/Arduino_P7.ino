//izquierda
//derecha
//centro ->> A0

// Tierra / 5V van de manera intercambiable en izquierda o derecha

int potenciometro = A0;

int valor;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}


void loop() {
  // put your main code here, to run repeatedly:

  valor = analogRead(potenciometro); //0 1023.  -> 1024 valores posibles. -> ADC de 10 bits de resolucion

  Serial.println(valor);

  delay(100);

}
