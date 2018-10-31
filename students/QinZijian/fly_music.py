from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
import serial
import serial.tools.list_ports

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
pos = mc.player.getTilePos()


ports = list(serial.tools.list_ports.comports())

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

stayed_time=0

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
    if pos.x>=30 and pos.x <=50  and pos.y>=0 and pos.y<=10 and pos.z>=0 and pos.z<=20:
        mc.postToChat("welcome home")
        for song in song_lst:
            if action == song[0]:
                for i in song:
                    i = i + 'a'
                    ser.write(i.encode())
                    time.sleep(0.25)
        stayed_time=stayed_time + 1
        if stayed_time>=10:
            mc.player.setTilePos(40,5,10)
            stayed_time=0
    else:
        stayed_time=0
