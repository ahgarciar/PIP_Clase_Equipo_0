int indice = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println("Mensaje " + String(indice));
  indice++;

  delay(100);

}
