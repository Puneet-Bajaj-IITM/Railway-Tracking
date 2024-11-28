#include <Servo.h>

Servo motorA;
Servo motorB;
Servo motorC;
int posA = 0, posB = 0, posC = 0;

void setup() {
    Serial.begin(9600);

    // Attach each motor to a different pin and enter the pin number here:
    motorA.attach(9);  // Pin for Camera A
    motorB.attach(10); // Pin for Camera B
    motorC.attach(11); // Pin for Camera C
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');

        if (command == "OPEN_A") {
            // open door for Camera A
            for (posA = 0; posA <= 90; posA += 5) {
                motorA.write(posA);
                delay(15);
            }
            delay(5000); // Keep door A open for 5 seconds
            for (posA = 90; posA >= 0; posA -= 5) {
                motorA.write(posA);
                delay(15);
            }
        }
        else if (command == "OPEN_B") {
            // Rotate motorB and open door for Camera B
            for (posB = 0; posB <= 90; posB += 5) {  
                motorB.write(posB);
                delay(15);
            }
            delay(5000); // Keep door B open for 5 seconds
            for (posB = 90; posB >= 0; posB -= 5) {
                motorB.write(posB);
                delay(15);
            }
        }
        else if (command == "OPEN_C") {
            // open door for Camera C
            for (posC = 0; posC <= 90; posC += 5) { 
                motorC.write(posC);
                delay(15);
            }
            delay(5000); // Keep door C open for 5 seconds
            for (posC = 90; posC >= 0; posC -= 5) {
                motorC.write(posC);
                delay(15);
            }
        }
    }
}
