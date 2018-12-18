#include <SoftwareSerial.h>
#include <PS2X_lib.h>
PS2X ps2x;
SoftwareSerial mySerial(6,7);//RX,TX

int error = 0;
byte type = 0;
byte vibrate = 0;
int base1_angle = 90;
String toSlave = "";

void setup(){
  mySerial.begin(9600);
  mySerial.listen();
  
  error = ps2x.config_gamepad(13,11,10,12,true,true); 
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
    }
    
    if(ps2x.Button(PSB_PAD_RIGHT)){
       RotateRight();
    }
    mySerial.print('a');
    mySerial.println(base1_angle);
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
