//install ArduinoJson library
#include <ArduinoJson.h>

JsonDocument sensor_data;

void setup() {
  Serial.begin(9600);
}

void loop() {
  String json;
  sensor_data["distance"] = rand()%100;
  sensor_data["rotation"] = rand()%360;

  serializeJson(sensor_data, json);
  Serial.println(json);
  delay(100);
}

