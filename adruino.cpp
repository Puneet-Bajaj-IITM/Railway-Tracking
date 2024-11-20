#include <Servo.h>

Servo motor;
int pos = 0;

void setup() {
    Serial.begin(9600);
    motor.attach(9); // Pin where the motor is connected
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        if (command == "OPEN") {
            // Rotate motor
            for (pos = 0; pos <= 90; pos += 5) {
                motor.write(pos);
                delay(15);
            }
            delay(5000); // Keep door open for 5 seconds

            // Rotate motor back to close door
            for (pos = 90; pos >= 0; pos -= 5) {
                motor.write(pos);
                delay(15);
            }
        }
    }
}
