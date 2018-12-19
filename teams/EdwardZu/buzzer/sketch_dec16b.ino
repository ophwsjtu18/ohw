int buzzer_0=8;

float sinVal=0;
int toneVal=0;
void setup() {
  // put your setup code here, to run once:
    pinMode(buzzer_0,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 for(int x=0; x<180; x++){
           //将sin函数角度转化为弧度
           sinVal = (sin(x*(3.1412/180)));
           //用sin函数值产生声音的频率
           toneVal = 2000+(int(sinVal*1000));
           //给引脚8一个
           tone(8, toneVal,2);
           delay(2);
          }
}
