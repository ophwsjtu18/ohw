#include <PS2X_lib.h>
#include <Servo.h>
PS2X ps2x;
Servo base1;

int error = 0;
byte type = 0;
byte vibrate = 0;
int base1_angle = 90;

void setup(){
  Serial.begin(9600);
  error = ps2x.config_gamepad(13,11,10,12,true,true);  
  base1.attach(9);
  base1.write(90);
}

void loop(){
  if(error == 1) return;
  //no controller found
  if(type == 2)return;
  // Guitar Hero Controller
  else{
    ps2x.read_gamepad(false,vibrate);
    vibrate = ps2x.Analog(PSAB_BLUE);
    
    if(ps2x.Button(PSB_PAD_LEFT)){
      RotateLeft();
      Serial.println("Left is pressed");
    }
    
    if(ps2x.Button(PSB_PAD_RIGHT)){
       RotateRight();
      Serial.println("Right is pressed"); 
    }
     base1.write(base1_angle);
  }
  delay(50);
}

void RotateLeft(){
  if(base1_angle>179)
    base1_angle = 179;
  if(base1_angle<1)
    base1_angle = 1;
  else
    base1_angle = base1_angle + 1;
}
void RotateRight(){
   if(base1_angle>179)
    base1_angle = 179;
  if(base1_angle<1)
    base1_angle = 1;
  else
    base1_angle = base1_angle - 1;
}
