# coding:utf-8
"""
将完成以下功能：
识别电子积木，并完成串口通信（唱歌，按钮飞天）。
MC中，回家提示，回家跳跃，回家播放音乐，音乐按跳跃次数不同变化。
house类建房子。
"""
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


def jump():
    mc.player.setTilePos(pos.x, pos.y+3, pos.z)

def music(times):
    choice = times % 3
    name = songs.keys()[choice]
    for i in songs[name]:
        ser.write(i.encode())
        ser.write('a'.encode())



while True:
    #提示回家
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go back home -193<=x<=-180 y=25 112<=z<=122 for 5s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    times = 0 #起跳次数

    if -193 <= pos.x <= -180 and pos.y== 25 and 112 <= pos.z <= 122:
        mc.postToChat("welcome home")
        stayed_time = stayed_time + 1
        if stayed_time >= 5:
            jump()
            music(times)
            stayed_time = 0
            times += 1

    else:
        stayed_time = 0
