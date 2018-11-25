#include<Servo.h>
#define trayClosed  127
#define trayOpened  122
Servo testServo;


void sweep ( Servo servo , int from , int to , int speed  ) {
  int pos = 0 ;
  if (from < to) {
    for (pos = from; pos <= to; pos += 1) { 
      servo.write(pos);              
      delay(speed);                       
    }  
  } else {
    for (pos = from; pos >= to; pos -= 1) { 
      servo.write(pos);              
      delay(speed);                       
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  testServo.attach(6);
  sweep(testServo, testServo.read(),trayOpened, 50);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:

  sweep(testServo, testServo.read(),trayClosed, 50);
  delay(2000);
  sweep(testServo, testServo.read(),trayOpened, 50);
  delay(2000);
}
