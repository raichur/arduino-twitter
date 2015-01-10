int relayPin = 13; // LED connected to pin 13
int inputByte = 0; // Incoming byte

// Setup (runs when sketch starts)
void setup(){
  pinMode(relayPin, OUTPUT); // Initialize relayPin as output
  Serial.begin(9600); // Set up Serial at 9600 bps
  Serial.println("The Arduino is ready.");
}

// Check for incomingByte loop
void loop(){
  if(Serial.available() > 0){
    inputByte = Serial.read(); // If it's avaiable (there's a new Tweet), read it
    Serial.println(inputByte);

    if(inputByte == 49){
      digitalWrite(relayPin, HIGH); // 5V on relayPin
    } else {
      digitalWrite(relayPin, LOW); // 0V on relayPin
    }

    Serial.println("I received"); // Print what it received
    Serial.println(inputByte, DEC); // DEC stands for Decimal
  }
}
