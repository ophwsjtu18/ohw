# -*- coding: utf-8 -*-
#我的世界初始化
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
stayed_time = 0
pos = mc.player.getTilePos()

#建房屋

#上下面
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+i,pos.y+5,pos.z+j,49)
        mc.setBlock(pos.x+i,pos.y,pos.z+j,49)
#左右面
for i in range(10):
    for j in range(6):
        if ((i==4 or i ==5) and (j==2 or j==3)):  #窗户
            mc.setBlock(pos.x,pos.y+j,pos.z+i,20)
            mc.setBlock(pos.x+9,pos.y+j,pos.z+i,20)
        else:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,49)
            mc.setBlock(pos.x+9,pos.y+j,pos.z+i,49)

#前后面
for i in range(10):
    for j in range(6):
        mc.setBlock(pos.x+i,pos.y+j,pos.z+9,49)
        if ((i==4 or i ==5) and (j==1 or j==2 or j==3)):  #门
            continue
        else:
            mc.setBlock(pos.x+i,pos.y+j,pos.z,49)
#门前火把
mc.setBlock(pos.x+4,pos.y+3,pos.z,50)
mc.setBlock(pos.x+5,pos.y+3,pos.z,50)


#Arduino通信初始化
import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#wait 2 seconds for arduino board restart
time.sleep(2)

#进门开灯

#歌单
MusicFile = open("songs.txt",'r').read().split('\n')
songs = {}
for i in MusicFile[:-1]:
    songs[i.split(' ')[0]] = i.split(' ')[1].split(',')

#回到小屋
mc.postToChat("welcome home")
#迎接音乐
def DoorMusic():
    MusicName = 'backhome'
    for i in songs[MusicName]:
        ser.write(i.encode())
        ser.write('a'.encode())
        time.sleep(0.25)

#屋内音乐
def RoomMusic():
    MusicName = 'stayhome'
    for i in songs[MusicName]:
        ser.write(i.encode())
        ser.write('a'.encode())
        time.sleep(0.25)

#开关弹跳


while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    stayed_time=stayed_time+1
