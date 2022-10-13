

//Leer dos numeros e imprimir la suma
//El se reiniciara una vez que hay culminado

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //UART
  //9600 baudios 

  Serial.setTimeout(100);//ms
}

int estado  = 0 ;

int cuadrado;
int valor = 0;
void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()>0){ //si existe informacion en el buffer
    valor += Serial.readString().toInt();

    estado++;
  }

  if(estado==2){
    Serial.println("La suma de los numeros es: " + String(valor));
    estado = 0;
    valor = 0; 
  }

  delay(100);

}
