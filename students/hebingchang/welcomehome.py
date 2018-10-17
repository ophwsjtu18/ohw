from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if 49<=pos.x<=51 and 268<=pos.z<=270:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=1:
            mc.player.setTilePos(pos.x,pos.y+1,pos.z)
            stayed_time=0
    else:
        stayed_time=0
        
     
