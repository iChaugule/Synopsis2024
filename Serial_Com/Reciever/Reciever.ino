int In1 = 7;
int In2 = 8; 
int In3 = 2;
int In4 = 4;
int ENA = 5;
int ENB = 6;
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
  
  analogWrite(ENA,SPEED);
  analogWrite(ENB,SPEED);
}

void loop() {
  // send data only when you receive data:

  //digitalWrite(ledPin, HIGH);
  
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    String incomingString = Serial.readStringUntil('\n');
    
    if (incomingString == "forward") {
      digitalWrite(In1,LOW);
      digitalWrite(In2,HIGH);
      digitalWrite(In3,LOW);
      digitalWrite(In4,HIGH);
    } else if (incomingString == "reverse") {
      digitalWrite(In1,HIGH);
      digitalWrite(In2,LOW);
      digitalWrite(In3,HIGH);
      digitalWrite(In4,LOW); 
    } else if (incomingString == "stop") {
      digitalWrite(In1,LOW);
      digitalWrite(In2,LOW);
      digitalWrite(In3,LOW);
      digitalWrite(In4,LOW); 
    }
     
    // say what you got:
    // Serial.print("I received: ");
    Serial.println("Echo:" + incomingString);
    // delay(3000);
  }
}
