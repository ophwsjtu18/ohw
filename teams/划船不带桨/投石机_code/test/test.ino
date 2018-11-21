#include <Servo.h>
Servo lockServo;
Servo armServo;
Servo trayServo;
Servo baseServo;

void setup()
{
  Serial.begin(9600);
  /// connect servo motors
  lockServo.attach(3); //9g舵机
  armServo.attach(5);  //995舵机
  trayServo.attach(6); //9g舵机
  baseServo.attach(9); //995舵机
  Serial.begin(9600);
  Serial.println(baseServo.read());
  Serial.println("I've pritened the baseServo position");
  Serial.println(trayServo.read());
  Serial.println("I've pritened the trayServo position");
  Serial.println(armServo.read());
  Serial.println("I've pritened the armServo position");
  Serial.println(lockServo.read());
  Serial.println("I've pritened the lockServo position");
}

void servo_angle(Servo servo, int pos)
{
  servo.write(pos);
}

void loop()
{
  Serial.println(baseServo.read());
  Serial.println("I've pritened the baseServo position");
  Serial.println(trayServo.read());
  Serial.println("I've pritened the trayServo position");
  Serial.println(armServo.read());
  Serial.println("I've pritened the armServo position");
  Serial.println(lockServo.read());
  Serial.println("I've pritened the lockServo position");
  delay(1000);
  servo_angle(baseServo, 100);
}
