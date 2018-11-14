from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
def elect(x0,y0,z0,L,W,H,S):
    for i in range(L):
        for j in range(H):
            for t in range(W):
                mc.setBlock(x0+i+2,y0+j,z0+t,S)
    for i in range(L-2):
        for j in range(H-2):
            for t in range(W-2):
                mc.setBlock(x0+i+3,y0+1+j,z0+t+1,0)

    for j in range(3):
        for i in range(2):
            mc.setBlock(x0+2,y0+1+j,z0+5+i,0)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x0+11,y0+1+j,z0+8-i,0)
    mc.setBlock(x0+6,y0+2,z0,0)
    mc.setBlock(x0+5,y0+3,z0,0)
    mc.setBlock(x0+7,y0+3,z0,0)
    mc.setBlock(x0+6,y0+4,z0,0)
    
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
        elect(pos.x,pos.y,pos.z,10,10,8,57)
        elect(pos.x+20,pos.y,pos.z+20,10,10,8,57)
