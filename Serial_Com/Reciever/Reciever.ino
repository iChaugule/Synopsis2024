int In1 = 7;
int In2 = 8; 
int In3 = 2;
int In4 = 4;
int ENA = 5;
int ENB = 6;
int LightP = 12;
int SPEED = 255;

void setup() {
  
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  while (!Serial) {}

  pinMode (In1,OUTPUT);
  pinMode (In2,OUTPUT);
  pinMode (ENA,OUTPUT);   
  pinMode (In3,OUTPUT);
  pinMode (In4,OUTPUT);
  pinMode (ENB,OUTPUT);
  pinMode (LightP, OUTPUT);   
  
  analogWrite(ENA,SPEED);
  analogWrite(ENB,SPEED);
}

void loop() {
  // send data only when you receive data:

  //digitalWrite(ledPin, HIGH);
  
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    String incomingString = Serial.readStringUntil('\n');
    
    if (incomingString == "move front") {
      digitalWrite(In1,HIGH);
      digitalWrite(In2,LOW);
      digitalWrite(In3,HIGH);
      digitalWrite(In4,LOW);
    } else if (incomingString == "move back") {
      digitalWrite(In1,LOW);
      digitalWrite(In2,HIGH);
      digitalWrite(In3,LOW);
      digitalWrite(In4,HIGH); 
    } else if (incomingString == "stop moving") {
      digitalWrite(In1,LOW);
      digitalWrite(In2,LOW);
      digitalWrite(In3,LOW);
      digitalWrite(In4,LOW);  
    } else if (incomingString == "light on") {
      digitalWrite(LightP,HIGH);
    } else if (incomingString == "light off") {
      digitalWrite(LightP,LOW); 
    } 
    
     
    // say what you got:
    // Serial.print("I received: ");
    Serial.println("Echo:" + incomingString);
    // delay(3000);
  }
}
