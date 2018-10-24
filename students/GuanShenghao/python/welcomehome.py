from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

W_house=False
stayed_time=0

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
        
