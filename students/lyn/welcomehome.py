from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = minecraft.Minecraft.creat()
pos=mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x>=29 and pos.x<=32 and pos.z>=14 and pos.z<=17:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=5:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time==
