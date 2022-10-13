int contador;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 
  contador = 0;

  Serial.setTimeout(100);//ms
}

String valor;
void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()>0){ //si existe informacion en el buffer
    valor = Serial.readString();
    Serial.println(valor);
  }


  delay(100);

}
