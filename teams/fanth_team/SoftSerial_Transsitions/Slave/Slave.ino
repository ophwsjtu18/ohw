#include <SoftwareSerial.h>
#include <Servo.h>
SoftwareSerial mySerial(10,11);//RX,TX
Servo myServo;

int angle = 90;
String fromMaster = ""; 

void setup(){
  Serial.begin(9600);
  mySerial.begin(9600);
  mySerial.listen();
  myServo.attach(9);
  myServo.write(90);
  }

void loop(){
  mySerial.listen();
  if(mySerial.isListening()){
    while(mySerial.read() != 'a'){
      continue;
      }//等待缓冲区出现一个a
    while(mySerial.peek()!='\n'){
      fromMaster += (char)mySerial.read();
       }
     Serial.println(fromMaster);
     
     fromMaster = "";
      }
     delay(100);
    }
   
