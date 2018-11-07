from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

W_house=False
stayed_time=0

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
    if(W_house==False):
        for x in range(10):
            for z in range(10):
                mc.setBlock(pos.x+x,pos.y,pos.z+z,5)
        for x in range(10):
            for y in range(10):
                mc.setBlock(pos.x+x,pos.y+y,pos.z,5)
        for x in range(10):
            for z in range(10):
                mc.setBlock(pos.x+x,pos.y+9,pos.z+z,5)
        for x in range(10):
            for y in range(10):
                mc.setBlock(pos.x+x,pos.y+y,pos.z+9,5)
        for z in range(10):
            for y in range(10):
                mc.setBlock(pos.x+9,pos.y+y,pos.z+z,5)
        for z in range(10):
            for y in range(10):
                mc.setBlock(pos.x,pos.y+y,pos.z+z,5)
        for y in range(2):
                mc.setBlock(pos.x+4,pos.y+y+1,pos.z+z,0)
        W_house=True
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
    for song in song_lst:
    if action == song[0]:
        for i in song:
            i = i + 'a'
            ser.write(i.encode())
            time.sleep(0.25)
    stayed_time=stayed_time + 1
    if stayed_time>=10:
    mc.player.setTilePos(50,25,10)
        stayed_time=0
    else:
        stayed_time=0
