#include <Servo.h>
Servo lockServo ; 
Servo armServo ; 
Servo trayServo ; 
Servo baseServo ; 

#define lockOpen    110 
#define lockClosed  20 

#define armOpen     140 
#define armArmed    45

#define trayClosed  177
#define trayOpened  172

int armPosition = 0;
int lockPosition = 0;
int basePosition = 0;
int state = 0;

void setPosition ( Servo servo, int pos, int sleep = 0 ) {
  delay(sleep);
  servo.write(pos);
}

void setup() {
  Serial.begin(9600);
  /// connect servo motors
  lockServo.attach(3); 
  armServo.attach(5); 
  trayServo.attach(6);
  baseServo.attach(9);

  keep_status(2);
  keep_status(0);

  // initServo();
  Serial.println("Going to loop");
}

int keep_base_position()
{
  setPosition(baseServo, basePosition);
}

int keep_status(int state)
{
  if (state == 0) {
    // Idle
    armPosition = 180;
    lockPosition = 60;
    setPosition(armServo, armPosition);
    setPosition(lockServo, lockPosition, 1000);
  } else if (state == 1) {
    // Ready for shoot
    armPosition = 30;
    lockPosition = 60;
    setPosition(armServo, armPosition);
    setPosition(lockServo, lockPosition);
  } else if (state == 2) {
    // Shoot!
    armPosition = 30;
    lockPosition = 0;
    setPosition(armServo, armPosition);
    setPosition(lockServo, lockPosition);
  }
}

void loop() {  
    long mylist[]={0, 0, 0, 0, 0, 0, 0};
    long cur;
    String strshow;
    String item;
    long itemint;
  
    if (Serial.available() > 0) {
        item = Serial.readStringUntil(' ');
        if (String(item).startsWith(String("B"))) {
          item.replace("B", "");
          basePosition = item.toInt();
        } else {
          state = String(item).toInt();
          
          /*itemint = String(item).toInt();
          cur = cur + 1;
          mylist[(int)(cur - 1)] = itemint;
          if (cur > 5) {
              cur = 5;
          }*/
       }
    }
    keep_status(state);
    keep_base_position();
}
