from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print ("No Arduino Device was found connected to the computer")
    #ser=serial.Serial(port='COM4')
    #ser=serial.Serial(port='/dev/ttymodem542')
    #wait 2 seconds for arduino board restart
time.sleep(2)

def sing_songs(turns):
    f = open('music.csv','r')
    music = f.read().split('\n')
    dic = {}
    music_line = music[turns].split(',')
    for action in music_line:
        ser.write((action+'a').encode())
        time.sleep(0.25)

def house(x0,y0,z0,L,W,H,M):
    for x in range(L):
        for z in range(W):
            for y in range(H):
                mc.setBlock(x0+x,y0+y,z0+z,M)

    for x in range(L-2):
        for z in range(W-2):
            for y in range(H-2):
                mc.setBlock(x0+1+x,y0+1+y,z0+1+z,0)

    for z in range(2):
        for y in range(2):
            mc.setBlock(x0,y0+2+y,z0+2+z,0)

    for x in range(2):
        for y in range(4):
            mc.setBlock(x0+2+x,y0+y,z0,0)

mc=Minecraft.create()
pos = mc.player.getTilePos()

for x in range(3):
    for y in range(3):
        for z in range(3):
            house(pos.x+x*10,pos.y+y*10,pos.z+z*10,8,6,8,block.STONE.id)

stayed_time=0
turns = 0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.y==10 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=15:
            mc.player.setTilePos(-30,10,-40)
            sing_songs(turns%3)
            turns = turns + 1
            stayed_time=0
    else:
        stayed_time=0

