#include <Servo.h>
Servo lockServo;
Servo armServo;
Servo trayServo;
Servo baseServo;

#define lockOpen 110
#define lockClosed 20

#define armOpen 140
#define armArmed 45

#define trayClosed 180
#define trayOpened 150

void rest() //整体复位
{
  sweep(lockServo, lockServo.read(), lockOpen, 15);
  sweep(armServo, armServo.read(), armOpen, 5);
}

void prepareToShoot(int armArm)
{
  int armshoot;
  armshoot = (180 - armArm) / 3;
  sweep(lockServo, lockClosed, lockClosed, 15);
  sweep(armServo, armshoot, armshoot, 5);
  Serial.println("armshoot:");
  Serial.println(armshoot);
}

void shoot() //释放石块
{
  sweep(lockServo, lockServo.read(), lockOpen, 15);
}

void sweep(Servo servo, int from, int to, int speed)
{
  int pos = 0;
  if (from < to)
  {
    for (pos = from; pos <= to; pos += 1)
    {
      servo.write(pos);
      delay(speed);
    }
  }
  else
  {
    for (pos = from; pos >= to; pos -= 1)
    {
      servo.write(pos);
      delay(speed);
    }
  }
}

void trayClose()
{
  sweep(trayServo, trayServo.read(), trayClosed, 22);
}

void trayOpen()
{
  sweep(trayServo, trayServo.read(), trayOpened, 22);
}

void trayRelease() //装弹，两秒的时间
{
  trayClose();
  trayOpen();
  trayClose();
  delay(2000);
}

void baseMove(int jd) //底座转动一个角度
{
  sweep(baseServo, baseServo.read(), jd * 90 / 100 + 10, 15);
}

void setup()
{
  Serial.begin(9600);
  /// connect servo motors
  lockServo.attach(3); //9g舵机
  armServo.attach(5);  //995舵机
  trayServo.attach(6); //9g舵机
  baseServo.attach(9); //995舵机
  Serial.begin(9600);

  // 每次开启arudino时， 四个舵机都会复位到93度
  init_pos = 93;
  Serial.println(baseServo.read());
  Serial.println("I've pritened the baseServo position");
  Serial.println(trayServo.read());
  Serial.println("I've pritened the trayServo position");
  Serial.println(armServo.read());
  Serial.println("I've pritened the armServo position");
  Serial.println(lockServo.read());
  Serial.println("I've pritened the lockServo position");

  //sweep(baseServo, 0, 180, 15);
  //sweep(lockServo, 0, 180, 15);
  //sweep(armServo, 0, 180, 15);
  //sweep(trayServo, 0, 180, 15);



  trayClose();

  delay(250); /// you have time to load bullets
  trayRelease();
  Serial.begin(9600);
  Serial.println("Start");
  rest();
  prepareToShoot(armArmed);
  shoot();
  rest();
  Serial.begin(9600);
  Serial.println("Going to loop");
}

int auto_run(int jd, int aarm, int shooting)
{
  baseMove(jd); ///This is my magic!!
  trayRelease();
  prepareToShoot(aarm);
  Serial.println("auto_runint jd,int aarm,int shooting");
  Serial.println(jd);
  Serial.println(aarm);
  Serial.println(shooting);
  if (shooting >= 90)
  {
    shoot();
    rest();
  }
  Serial.println("tray is moving");
  Serial.println(trayServo.read());
  Serial.println("I've pritened the trayServo position");
}

void loop()
{
  long mylist[] = {0, 0, 0, 0, 0, 0, 0};
  long cur;
  String strshow;
  String item;
  long itemint;

  if (Serial.available() > 0)
  {
    item = Serial.readStringUntil(' ');
    if (String(item).equals(String("A")))
    {
      cur = 0;
    }
    else
    {
      itemint = String(item).toInt();
      cur = cur + 1;
      mylist[(int)(cur - 1)] = itemint;
      if (cur > 5)
      {
        cur = 5;
      }
    }
  }
  auto_run(mylist[1], mylist[2], mylist[3]);
}
