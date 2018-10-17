from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-38 y=1 z=-49 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>=30 and pos.x <=50  and pos.y>=0 and pos.y<=10 and pos.z>=0 and pos.z<=20:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(47,20,11)
            stayed_time=0
    else:
        stayed_time=0
        
     
