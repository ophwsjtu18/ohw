#include<Servo.h>
#define LIMIT(x) x>178?178:x<2?2:x
#define SERVO1 5
#define SERVO2 6
#define SERVO3 7
#define SERVO4 4

#define SERVO1_OPEN 135
#define SERVO1_CLOSE  158

#define SERVO2_OPEN 54
#define SERVO2_CLOSE 0

#define SERVO3_OPEN 91
#define SERVO3_CLOSE 178

Servo servo1;//supply-servo
Servo servo2;//lock-servo
Servo servo3;//stretch-servo
Servo servo4;//move-servo
int target=90;
void reset();
void initialise() {
  servo1.write(SERVO1_CLOSE);
  servo2.write(SERVO2_CLOSE);
  servo3.write(SERVO3_CLOSE);
}
void setup() {
  // put your setup code here, to run once:
  servo1.attach(SERVO1);
  servo2.attach(SERVO2);
  servo3.attach(SERVO3);
  servo4.attach(SERVO4);
  initialise();
  Serial.begin(9600);
  delay(1000);
}
void supply() {
  servo1.write(SERVO1_OPEN);
  delay(100);
  servo1.write(SERVO1_CLOSE);
}
void reset() {
  servo3.write(SERVO3_CLOSE);
  while (abs(servo3.read() - SERVO3_CLOSE) >= 2) {
    //alarm
  }
  delay(500);
  servo2.write(SERVO2_CLOSE);
  supply();//可能可以提前，要看能不能并发
}
void fire() {
  servo3.write(SERVO3_OPEN);
  while (abs(servo3.read() - SERVO3_OPEN) >= 2) {
    //alarm
  }
  delay(1000);
  servo2.write(SERVO2_OPEN);
  delay(1000);
  reset();
}
char getData() {
  char tmp = 0;
  delay(10);
  if (Serial.available() > 0) {
    tmp = Serial.read();
  }
  return tmp;
}
char tmp;
int finished=0;
void empty_memory(){
    while(Serial.read() > 0);
}
void asd(){
    if(getData()=='s'){
      if(getData()=='t'){
        tmp=getData();
        if(tmp=='+')target+=1,empty_memory();
        if(tmp=='-')target-=1,empty_memory();
        if(tmp=='*')fire(),empty_memory();
      }
  }
  LIMIT(target);
  servo4.write(target);
}
void loop() {
  // put your main code here, to run repeatedly:
    asd();
//  if(finished==1)Serial.print('o');
    Serial.print('o');
}
