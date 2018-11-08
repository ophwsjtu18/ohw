from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
import csv

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "USB-SERIAL" or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

p = open("songs.csv",'r').read()
song=[]
g=p.split('\n')
for i in g:
    song.append(i.split(','))
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
times=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    s=0
    if(ser.inWaiting()):                  #task 5
        s=str(ser.read().decode())
        print(s)
        if (s=='a'):
            mc.player.setTilePos(pos.x,pos.y+10,pos.z)     #
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=15:
            mc.player.setTilePos(-30,10,-40)
            times = times +1
            for a in song[times%3]:       #task 4
                ser.write(a.encode())
                ser.write('a'.encode())
                time.sleep(0.150)         #
            stayed_time=0
    else:
        stayed_time=0
