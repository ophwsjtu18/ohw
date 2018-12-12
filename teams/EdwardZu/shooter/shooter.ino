#include <Servo.h>
Servo lockServo ;
Servo armServo ;
Servo trayServo ;
Servo baseServo ;

#define lockOpen    110
#define lockClosed  20

#define armOpen     180
#define armArmed    20

#define trayClosed  127
#define trayOpened  122

void rest() {
  sweep(armServo,armServo.read(),armOpen,50) ;
  delay(1000);
  sweep(lockServo,lockServo.read(),lockClosed,15) ;
 }

void prepareToShoot(int armArm) {
  int armshoot;
  armshoot=(180-armArm);
//  sweep(lockServo,lockClosed,lockClosed,15) ;
  sweep(armServo,armServo.read(),armshoot,50) ;
  Serial.println("armshoot:");
  Serial.println(armshoot);
  delay(1000);
}

void shoot() {
  sweep(lockServo,lockServo.read(),lockOpen,15) ;
}

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


void trayClose(){
  sweep(trayServo,trayServo.read(),trayClosed,22) ;
}

void trayOpen() {
  sweep(trayServo,trayServo.read(),trayOpened,22) ;
}

void trayRelease() {
    trayOpen() ;
    trayClose() ;
}

void baseMove(int jd) {
  sweep(baseServo,baseServo.read(),jd,50);
}

void setup() {
Serial.begin(9600);
    /// connect servo motors
    lockServo.attach(3);
    armServo.attach(5) ;
    trayServo.attach(6);
    baseServo.attach(9) ;
    Serial.begin(9600);
    Serial.println(baseServo.read());
    Serial.println("I've pritened the baseServo position");
    Serial.println(trayServo.read());
    Serial.println("I've pritened the trayServo position");
    Serial.println(armServo.read());
    Serial.println("I've pritened the armServo position");
    Serial.println(lockServo.read());
    Serial.println("I've pritened the lockServo position");
    //sweep(baseServo,0,180,50);
    //sweep(lockServo,0,180,50);
    //sweep(armServo,0,180,50);
    //sweep(trayServo,0,180,50);
    sweep(baseServo,baseServo.read(), 90, 50);
    delay(1000);
    trayClose();
    delay(1000); /// you have time to load bullets
    trayRelease();
    Serial.begin(9600);
    Serial.println("Start");
    rest();
    delay(1000);
    prepareToShoot(armArmed) ;
    delay(1000);
    shoot();
    rest();
    Serial.begin(9600);
    Serial.println("Going to loop");
}

int auto_run(int jd,int aarm,int shooting)
{
    baseMove(jd);
    trayRelease();
    prepareToShoot(aarm) ;
    Serial.println ("auto_runint jd,int aarm,int shooting");
    Serial.println(jd);
    Serial.println(aarm);
    Serial.println(shooting);
    if(shooting>=90){
       shoot();
       rest();
    }
    Serial.println("tray is moving");
    Serial.println(trayServo.read());
    Serial.println("I've pritened the trayServo position");
    Serial.println("OVER")
}

void loop() {

    long mylist[]={0, 0, 0, 0, 0, 0};
    long cur;
    String strshow;
    String item;
    long itemint;
    while (Serial.available() > 0) {
        item = Serial.readStringUntil(' ');
        Serial.println(item);
        if (String(item).equals(String("A"))) {
            cur = 0;
        } else {
          itemint = String(item).toInt();
          cur = cur + 1;
          mylist[(int)(cur)] = itemint;
          if (cur > 5) {
              cur = 5;
          }
       }
    }
    auto_run(mylist[1], mylist[2], mylist[3]);
}
