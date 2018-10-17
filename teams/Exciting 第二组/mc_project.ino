 // Visual Micro is in vMicro>General>Tutorial Mode
// 
/*
    Name:       mc_project.ino
    Created:	2018/5/30 18:11:23
    Author:     LAPTOP-AL5LKVV4\lenovo
*/

// Define User Types below here or use a .h file
//


// Define Function Prototypes that use User Types below here or use a .h file
//


// Define Functions below here or use other .ino or cpp files
#include<Servo.h>

Servo arm,root,board,stopper;

// The setup() function runs once each time the micro-controller starts
void setup()
{
	Serial.begin(9600);
	Serial.setTimeout(1000); 
  arm.attach(6);
  root.attach(9);
  board.attach(10);
  stopper.attach(11);
  board.write(160);
  arm.write(130);
  stopper.write(90);
}
void boarder(bool act)
{
  if(act)
  board.write(70);
  else
  board.write(160);
}
void stopperer(bool act){
  if(act)
  stopper.write(15);
  else
  stopper.write(90);
}
void armer(bool act){
if(act)
arm.write(0);
else
arm.write(140);
}
// Add the main program code into the continuous loop() function
void loop()
{
  String comdata = "";
	//接受python串口指令，发送至arduino串口，控制舵机
	while (Serial.available() > 0) {
		comdata += char(Serial.read());
		delay(2);
	}
	if (comdata.length() > 0) {
		Serial.println(comdata);
	}

	if (comdata == "0")   // board还原
    boarder(false);
  if(comdata == "1")  // board shoot
    boarder(true);
    if(comdata == "2"){ // arm还原
      armer(false);
      delay(1000);
      stopperer(false);
    }
   if(comdata == "3") // arm ready
    armer(true);
   if(comdata=="4"){  // shoot
    stopperer(true);
   }
   if(comdata=="5"){
    boarder(true);
    delay(1000);
    boarder(false);
    delay(1000);
    armer(true);
    delay(1000);
    stopperer(true);
    delay(1000);
    armer(false);
      delay(1000);
      stopperer(false);
   }
} 
