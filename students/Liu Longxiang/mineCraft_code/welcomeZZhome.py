from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()
pos = mc.player.getTilePos()

stayed_time=0

for i in range(10): //Front,Behind,Left,Right
    for j in range(6):
        mc.setBlock(pos.x,pos.y+6+j,pos.z+i,1)
        mc.setBlock(pos.x+10,pos.y+6+j,pos.z+i,1)
        mc.setBlock(pos.x+i,pos.y+6+j,pos.z,1)
        mc.setBlock(pos.x+i,pos.y+6+j,pos.z,1)

for i in range(10): // Floor,Platfond
    for j in range(10):
        mc.setBlock(pos.x+i,pos.y+6,pos.z+j)
        mc.setBlock(pos.x+i,pos.y+11,pos.z+j)

for i in range(1):  //Door
    for j in range(3):
        mc.setBlock(pos.x+5+i,pos.y+6+j,pos.z,0)

for i in range(2): //Window
    for j in range(2):
        mc.setBlock(pos.x,pos.y+9+j,pos.z+1+i,20)

for i in range(4):  //Roof
    for j in range(8-2*i):
        for k in range(8-2*i):
            mc.setBlock(pos.x+1+i+j,pos.y+12+i,pos.z+1+i+k,1)

for i in range(6): //Chimney
    mc.setBlock(pos.x+3,pos.y+14+i,pos.z+3) 

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
