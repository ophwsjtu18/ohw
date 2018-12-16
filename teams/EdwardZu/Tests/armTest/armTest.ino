#include<Servo.h>
#define armOpen     140 
#define armArmed    45
#define lockOpen    110 
#define lockClosed  20 
Servo armServo;
Servo lockServo;


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
  armServo.attach(6);
  lockServo.attach(3);
  sweep(armServo, armServo.read(),0, 15);
  sweep(armServo, armServo.read(),180, 15);
  //sweep(lockServo, lockServo.read(),lockClosed, 10);
}

void loop() {
  // put your main code here, to run repeatedly:

/*  sweep(armServo, armServo.read(),armArmed, 50);
  sweep(lockServo, lockServo.read(),lockOpen, 10);
  delay(1000);
  sweep(armServo, armServo.read(),armOpen, 10);
  sweep(lockServo, lockServo.read(),lockClosed, 10);
  delay(2000);
  */
  sweep(armServo, armServo.read(),0, 15);
  delay(3000);
  sweep(armServo, armServo.read(),180, 15);
  delay(3000);

}
