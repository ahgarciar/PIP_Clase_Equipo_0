int contador;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 
  contador = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola" + String(contador++));
  delay(1000); //ms
}
