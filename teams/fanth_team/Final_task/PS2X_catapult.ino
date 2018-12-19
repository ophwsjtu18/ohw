#include <Servo.h>
#include <PS2X_lib.h>

Servo lockServo ;
Servo armServo ;
Servo trayServo ;
Servo baseServo ;
PS2X ps2x;
int error = 0;
byte type = 0;
byte vibrate = 0;

#define lockOpen    180
#define lockClosed  90

#define armOpen     180
#define armArmed    90

#define trayClosed  98
#define trayOpened  70

#define basePoint 95

void sweep ( Servo servo , int from , int to , int step_time  ) {
    int pos = 0 ;
    if (from < to) {
    for (pos = from; pos <= to; pos += 1) {
        servo.write(pos);
        delay(step_time);
        }
    }
    else {
    for (pos = from; pos >= to; pos -= 1) {
        servo.write(pos);
        delay(step_time);
        }
    }
}

void rest() {
    sweep(armServo,armServo.read(),armOpen,5) ;
    sweep(lockServo,lockServo.read(),lockClosed,10) ;
    sweep(trayServo,trayServo.read(),trayClosed,10);
    sweep(baseServo,baseServo.read(),basePoint,10);
    }

void shootprep(int strength) {
    sweep(trayServo,trayServo.read(),trayOpened,10) ;
    delay(1500);
    sweep(trayServo,trayServo.read(),trayClosed,10) ;
    if(strength<0)  strength = 0;
    if(strength>30) strength = 30;
    sweep(lockServo,lockServo.read(),lockClosed,10);
    sweep(armServo,armServo.read(),180-3*strength,5);
    delay(100);
    }
void shoot(){
    sweep(lockServo,lockServo.read(),lockOpen,10);
    delay(1000);
    sweep(armServo,armServo.read(),armOpen,5) ;
    }

void auto_run(int angle,int strength){
    sweep(baseServo,baseServo.read(),basePoint+angle,15);
    if(strength) {
        shootprep(strength);
        shoot();
        }
    }

void changemode(){
  error = (error+1)%2;
}

void setup() {
    Serial.begin(9600);
    /// connect servo motors
    error = ps2x.config_gamepad(13,11,10,12,true,true);  
    
    while(Serial.read() >=0){};
    lockServo.attach(3);
    armServo.attach(5) ;
    trayServo.attach(6);
    baseServo.attach(9) ;
    
    attachInterrupt(0,changemode,RISING);
    rest();
}


void loop(){
  //检测手柄是否连接
  int cmd[]={90,30};
  
  if(error == 1){
    //手柄没有连接，CV
    int cur;
    String item;
    int itemint;
  Serial.println("Mode0");
   /* while (Serial.available() > 0) {
        delay(100);
        item = Serial.readStringUntil(' ');
        if (String(item).equals(String("A"))) {
            cur = 0;
        } else {
          itemint = String(item).toInt();
          cur = cur + 1;
          cmd[(int)(cur - 1)] = itemint;
          }
       }
        auto_run(cmd[0],cmd[1]);*/
    }   
   else{
    //DualShock Ctrl
   Serial.println("Mode1");
   
    ps2x.read_gamepad(false,vibrate);
    vibrate = ps2x.Analog(PSAB_BLUE);
    
    if(ps2x.Button(PSB_PAD_LEFT)){
      if(cmd[0]>180) cmd[0] = 180;
      if(cmd[0]<0)   cmd[0] = 0;
      else           ++cmd[0];
    }
    if(ps2x.Button(PSB_PAD_RIGHT)){
      if(cmd[0]>180) cmd[0] = 180;
      if(cmd[0]<0)   cmd[0] = 0;
      else           --cmd[0];
      }
    if(ps2x.Button(PSB_PAD_UP)){
      if(cmd[1]>60)   cmd[1] = 60;
      if(cmd[1]<20)   cmd[1] = 20;
      else           ++cmd[1];
    }
    if(ps2x.Button(PSB_PAD_UP)){
      if(cmd[1]>60)   cmd[1] = 60;
      if(cmd[1]<20)   cmd[1] = 20;
      else           --cmd[1];
    }
    if(ps2x.Button(PSB_R2)){
      auto_run(cmd[0],cmd[1]);
    }
   }
}
