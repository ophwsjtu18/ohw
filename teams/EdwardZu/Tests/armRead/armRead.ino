#include<Servo.h>
Servo armServo;
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
  Serial.begin(9600);
  armServo.attach(6);
  sweep(armServo, armServo.read(), armServo.read(), 10);
  Serial.println(armServo.read());
}

void loop() {
  // put your main code here, to run repeatedly:

}
