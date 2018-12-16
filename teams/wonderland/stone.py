from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
def elect(x0,y0,z0,S):
    for i in range(15):
        for j in range(2):
            for t in range(15):
                mc.setBlock(x0+i,y0+j,z0+t,S)
    for i in range(9):
        for j in range(2):
            for t in range(9):
                mc.setBlock(x0+i+3,y0+j+2,z0+t+3,S)
    for i in range(5):
        for j in range(6):
            for t in range(5):
                mc.setBlock(x0+5+i,y0+4+j,z0+5+t,S)
    for j in range(6):
        mc.setBlock(x0+6,y0+9+j,z0+6,S)
        mc.setBlock(x0+6,y0+9+j,z0+8,S)
        mc.setBlock(x0+8,y0+9+j,z0+6,S)
        mc.setBlock(x0+8,y0+9+j,z0+8,S)
    for j in range(5):
        for i in range(3):
            for t in range(3):
                mc.setBlock(x0+6+i,y0+14+j,z0+6+t,S)
    for j in range(12):
        mc.setBlock(x0+7,y0+16+j,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-20+t,y0+16+7-t,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-14+t,y0+16+t+1,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-8+t,y0+16+7-t,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-2+t,y0+16+t+1,z0+7,S)
    for t in range(12):
        mc.setBlock(x0+16,y0+17+t,z0+7,S)
    for t in range(9):
        mc.setBlock(x0+16+t,y0+17,z0+7,S)
        
stayed_time=0   
pos=mc.player.getTilePos()

#mc.player.setTilePos(pos.x+7,pos.y+2,pos.z+5)       
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
    if pos.y%10==0:
        elect(pos.x+20,pos.y,pos.z+20,57)
        mc.player.setTilePos(pos.x,pos.y+5,pos.z)
