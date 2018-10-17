from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home -3<=x<=0 35<=y<=37 -10<=z-7 for 5s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if -3<=pos.x<=0 and 35<=pos.y<=37 and -10<=pos.z<=-7:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=5:
            mc.player.setTilePos(pos.x, pos.y+3, pos.z)
            stayed_time=0
    else:
        stayed_time=0
        
     
