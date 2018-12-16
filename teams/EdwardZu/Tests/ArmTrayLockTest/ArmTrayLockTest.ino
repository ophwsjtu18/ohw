#include<Servo.h>
#define armOpen     180 
#define armArmed    120

#define lockOpen    110 
#define lockClosed  20 

#define trayClosed  127
#define trayOpened  117

Servo armServo;
Servo lockServo;
Servo trayServo;


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
  trayServo.attach(1);
  armServo.attach(6);
  lockServo.attach(3);
  sweep(armServo, armServo.read(),armOpen, 15);
  sweep(lockServo, lockServo.read(),lockClosed, 10);
  sweep(trayServo, trayServo.read(), trayClosed, 10);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:

  sweep(armServo, armServo.read(),armArmed, 50);
  sweep(lockServo, lockServo.read(),lockOpen, 10);
  delay(1000);
  sweep(armServo, armServo.read(),armOpen, 10);
  sweep(trayServo, trayServo.read(), trayOpened, 20);
  sweep(trayServo, trayServo.read(), trayClosed, 20);
  sweep(lockServo, lockServo.read(),lockClosed, 10);
  delay(2000);
  
}
