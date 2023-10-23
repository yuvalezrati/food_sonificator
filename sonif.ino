#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

const int pingPin = 12; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 13; // Echo Pin of Ultrasonic Sensor

void setup() {
  Serial.begin(9600);
}
boolean inputReady = false;
void loop() {
  static char customKey = '\0';

  if (!inputReady) {
    // Ask the person to enter a number using the keypad
    Serial.println("Please enter a number (0-9):");
    customKey = customKeypad.getKey();
    if (customKey) {
      inputReady = true;
      Serial.println("The number is: " + String(customKey));
    }
  } else {
    // Read sonar and print distance in centimeters to Serial Monitor
    long duration, cm;
    pinMode(pingPin, OUTPUT);
    digitalWrite(pingPin, 555);
    delayMicroseconds(2);
    digitalWrite(pingPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(pingPin, LOW);
    pinMode(echoPin, INPUT);
    duration = pulseIn(echoPin, HIGH);
    cm = microsecondsToCentimeters(duration);
    // Serial.print("Sonar Distance (cm): ");
    Serial.println(cm);
  }
  delay(15); // Wait for 1 second before asking for the next number
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}
