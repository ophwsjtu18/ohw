from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
import serial
import serial.tools.list_ports

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
pos = mc.player.getTilePos()

mc=Minecraft.create()

pos = mc.player.getTilePos()

ports = list(serial.tools.list_ports.comports())

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")




f = open('songs.csv', 'r')
songs = f.read().split('\n')
song = [song.split(',') for song in songs]
action = "empty"

stayed_time=0
times=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home pos.x>30 and pos.x<100 and pos.y>0 and pos.y<10 and pos.z>-100 and pos.z<100")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x>30 and pos.x<100 and pos.y>0 and pos.y<10 and pos.z>-100 and pos.z<100 :
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(50,12,0)
            times = times +1
            for time_n in song[times%3]:
                ser.write((str(time_n) + 'a').encode())
                time.sleep(0.05)
                ser.write(('0a').encode())
                time.sleep(0.05)
            
            stayed_time=0
    else:
        stayed_time=0
