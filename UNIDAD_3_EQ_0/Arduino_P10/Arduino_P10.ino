int led = 11;  //Cualquier pin digital que cuente con una virgulilla (Simbolo de ñ)

void setup() {
  // put your setup code here, to run once:
  
  //PWM no trabaja con PinMode

  //PWM =  modulacion por ancho de pulso 
  //Simulacion de una onda sinosoidal mediante la variacion del duty cycle de una onda cuadrada

  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:

for(int i  = 0; i<255; i++){
  analogWrite(led, i);  //PWM
  delayMicroseconds(10);
}

for(int i  = 255; i>0; i--){
  analogWrite(led, i);  //PWM
  delayMicroseconds(10);
}

delay(100);

}
