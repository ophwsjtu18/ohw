from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
import serial
import serial.tools.list_ports

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
pos = mc.player.getTilePos()

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
pos = mc.player.getTilePos()
for x in range(10):
    for y in range(10):
        mc.setBlock(pos.x + x, pos.y + y, pos.z, 1)
        mc.setBlock(pos.x + x, pos.y + y, pos.z + 10, 1)
for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x + x, pos.y, pos.z + z, 3)
        mc.setBlock(pos.x + x, pos.y + 10, pos.z + z, 1)
for y in range(10):
    for z in range(10):
            mc.setBlock(pos.x , pos.y + y, pos.z + z, 4)
            mc.setBlock(pos.x + 10, pos.y + y, pos.z + z, 5)
for x in range(3):
    for y in range(5):
        mc.setBlock(pos.x + 3 + x, pos.y + y, pos.z, 0)
for x in range(2):
    for z in range(2):
        mc.setBlock(pos.x + x + 3, pos.y, pos.z + z + 5, 20)

ports = list(serial.tools.list_ports.comports())

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

stayed_time=0
count = 0

f = open('songs.csv', 'r')
songs = f.read().split('\n')
song_lst = [song.split(',') for song in songs]
action = "first"

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home 30<x<50 0<y<10 0<z<20 for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    resp=ser.readline()
    rs=str(resp)


    if pos.x>=30 and pos.x <=50  and pos.y>=0 and pos.y<=10 and pos.z>=0 and pos.z<=20:
        mc.postToChat("welcome home")
        if 'ON' in rs:
            print("got ON")
            mc.player.setTilePos(pos.x, pos.y + 15, pos.z)
            count = count + 1
            mc.postToChat("fly")
        if 'OFF' in rs:
            print("got OFF")
            mc.player.setTilePos(pos.x, pos.y + 15, pos.z)
            mc.postToChat("down")
        if count % 3 == 1:
            action = "first"
        elif count % 3 == 2:
            action == "second"
        elif count % 3 == 0:
            action == "third"
        for song in song_lst:
            if action == song[0]:
                for i in song:
                    i = i + 'a'
                    ser.write(i.encode())
                    time.sleep(0.25)
        stayed_time=stayed_time + 1
        if stayed_time>=10:
            mc.player.setTilePos(40,25,10)
            stayed_time=0
    else:
        stayed_time=0
