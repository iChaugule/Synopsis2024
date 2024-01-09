#define ledPin 3

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  
  digitalWrite(ledPin, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(5000);
  
  digitalWrite(ledPin, LOW);
}
