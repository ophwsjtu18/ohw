# coding:utf-8
#导入我的世界包 及 串口通信包
from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
import time

#匹配单片机串口
print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)

mc=Minecraft.create() #连接bukkit 服务器
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser = serial.Serial(port=p[0])
    else:
        print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)


#读入歌曲；转为字典
rows = open("songs.csv").read().split('\n')
songs = {}
for row in rows:
    songs[row.split(',')[0]]=row.split(',')[1:]
for key, value in songs:
    print(key,value)

action = "empty"

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home -193<=x<=-180 y=25 112<=z<=122 for 5s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if -193<=pos.x<=-180 and pos.y==25 and 112<=pos.z<=122:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=5:
            mc.player.setTilePos(pos.x, pos.y+3, pos.z)
            stayed_time=0

            while True:
                for i in lyric[1]:
                   ser.write(i.encode())
                   ser.write('a'.encode())
                break
    else:
        stayed_time=0
