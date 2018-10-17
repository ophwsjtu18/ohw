from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
H=True

while True:

    set = 12
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()

    if H==True:
        for x in range(11):
            for z in range(11):
                mc.setBlock(pos.x+x, pos.y, pos.z+z,1)
        for y in range(11):
            for z in range(11):
                mc.setBlock(pos.x, pos.y+y, pos.z+z,1)
        for x in range(11):
            for y in range(11):
                mc.setBlock(pos.x+x, pos.y+y, pos.z,1)
        for x in range(11):
            for z in range(11):
                mc.setBlock(pos.x+x, pos.y+11, pos.z+z,1)
        for y in range(11):
            for z in range(11):
                mc.setBlock(pos.x+11, pos.y+y, pos.z+z,1)
        for x in range(11):
            for y in range(11):
                mc.setBlock(pos.x+x, pos.y+y, pos.z+11,1)
        for y in range(4,7):
            for z in range(4,7):
                mc.setBlock(pos.x+11, pos.y+y, pos.z+z,20)

        H = False









        




    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))




    if pos.x>=29 and pos.x<=32 and pos.z>=14 and pos.z<=17:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=5:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
