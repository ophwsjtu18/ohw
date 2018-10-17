from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
import mcpi.block as block
mc = Minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE,id)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
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
