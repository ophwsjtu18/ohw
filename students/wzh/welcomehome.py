from mcpi.minecraft import Minecraft
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0




while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home -31<=x<=-29 y=-6 -41<=z<=-39 for 5s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if (-31<=pos.x<=-29) and pos.y==-6 and (-41<=pos.z<=-39):
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0

    mc=minecraft.Minecraft.create()
    pos=mc.player.getTilePos()
    mc.setBLock(pos.x+3,pos.y,pos.z,block.STONE.id)    
