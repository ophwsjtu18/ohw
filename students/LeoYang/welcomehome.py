from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>=30 and pos.x <= 32 and pos.y==5 and pos.z>=-82 and pos.z <= -80:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(30,20,-80)
            stayed_time=0
    else:
        stayed_time=0
        
     
