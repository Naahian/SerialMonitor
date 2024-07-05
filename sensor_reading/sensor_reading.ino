//install ArduinoJson library
#include <ArduinoJson.h>

#define trig_pin 2
#define echo_pin 3

JsonDocument sensor_data;

void setup() {
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  digitalWrite(trig_pin, HIGH);
  digitalWrite(echo_pin, HIGH);
  Serial.begin(9600);
}

void loop() {
  String json;
  sensor_data["distance"] = getDistance();
  sensor_data["others"] = 0;

  serializeJson(sensor_data, json);
  Serial.println(json);
  delay(100);
}

float getDistance(){
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  float duration = pulseIn(echo_pin, HIGH);
  return  (duration*.0343)/2; 
}