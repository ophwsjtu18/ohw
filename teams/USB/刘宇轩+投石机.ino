#include <Servo.h>

Servo lockServo ; //发射锁舵机
Servo armServo ; //胳膊舵机
Servo trayServo ; //托盘舵机
Servo baseServo ;//底座舵机


int pos = 0;

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

void prepareToShoot() {

  sweep(lockServo,lockServo.read(),lockClosed,15) ; 
  sweep(armServo,armServo.read(),armArmed,15) ; 
  
}

void shoot() {

  sweep(lockServo,lockServo.read(),lockOpen,15) ; 
  
}

void rest() {
  
  sweep(lockServo,lockServo.read(),lockOpen,15) ; 
  sweep(armServo,armServo.read(),armOpen,15) ; 
 
}

void setup() {
  Serial.begin(9600);
  lockServo.attach(3); 
  armServo.attach(5); 
  trayServo.attach(6);
  baseServo.attach(9);
}

void loop() {  
  char a;
  int counter = 0;
  
  if (Serial.available()){
    a = Serial.read();
    Serial.println(a);
    if(a == 'L' and baseServo.read() < 176){
      sweep(baseServo,baseServo.read(),baseServo.read() + 60,15);
    }
  
    if(a == 'R' and baseServo.read() > 4){
      sweep(baseServo,baseServo.read(),baseServo.read() - 60,15);
    }
  
  
  sweep(trayServo, trayServo.read(), 90 ,3);
  delay(1000);
  sweep(lockServo, lockServo.read(), 50, 15);
  sweep(armServo, armServo.read(), 180, 15);
  
  sweep(trayServo, trayServo.read(), 0, 3);
  sweep(trayServo, trayServo.read(), 90 ,3);

  sweep(lockServo, lockServo.read(), 10, 15);
  sweep(armServo, armServo.read(), 0, 15);
  
  sweep(lockServo, lockServo.read(), 50, 15);
  }
}
