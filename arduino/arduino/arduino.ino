#define lpin_message 3 //digital
#define lpin_women 5 //digital
#define lpin_data 4 //digital

#define door_pin 2 //digital
#define led_pin 13 //digital
boolean doorClosed = false;
boolean waitForDoorClose = false;

void setup() {
  pinMode(lpin_message, OUTPUT);
  pinMode(lpin_women, OUTPUT);
  pinMode(lpin_data, OUTPUT);

  pinMode(door_pin, INPUT);
  digitalWrite(door_pin, HIGH); //??? I'd love to get why this works...
  
  pinMode(led_pin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  //reads from python
  if(Serial.available() > 0) {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    if (String(str) == "w") // "w": waiting for door to close
      waitForDoorClose = true;
    else  
      lightControl(str);
  }
  
  //door
  if (waitForDoorClose && doorClosed){
    Serial.println("r"); // "r" for ready
    waitForDoorClose = false;
  }
  
  if (digitalRead(door_pin)==LOW){
    doorClosed = true;
    digitalWrite(led_pin, HIGH);
  }
  else {
    doorClosed = false;
    digitalWrite(led_pin, LOW);
  } 
  
}

void lightControl(String str){
  /* "f": female on "o": female off
   * "m": message on "n": message off 
   * "d": data on "s": data off
   */
  if (str == "f") 
    digitalWrite(lpin_women, HIGH);
  if (str == "o")
    digitalWrite(lpin_women, LOW);
  if (str == "m")
    digitalWrite(lpin_message, HIGH);
  if (str == "n")
    digitalWrite(lpin_message, LOW);
  if (str == "d")
    digitalWrite(lpin_data, HIGH);
  if (str == "s")
    digitalWrite(lpin_data, LOW);
}
