int In1 = 7;
int In2 = 8; 
int ENA = 5;
int SPEED = 255;

void setup() {
  
  pinMode (In1,OUTPUT);
  pinMode (In2,OUTPUT);
  pinMode (ENA,OUTPUT);   

  digitalWrite(In1,LOW);
  digitalWrite(In2,HIGH);

  analogWrite(ENA,SPEED);
}

void loop() {
  // put your main code here, to run repeatedly:

}
