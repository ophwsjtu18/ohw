from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
pos=mc.player.getTilePos()
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+i, pos.y, pos.z+j, block.WOOD.id)
        mc.setBlock(pos.x+i, pos.y+9, pos.z+j, block.STONE.id)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+i, pos.y+j, pos.z, block.WOOD.id)
        mc.setBlock(pos.x+i, pos.y+j, pos.z+9, block.WOOD.id)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x, pos.y+i, pos.z+j, block.WOOD.id)
        mc.setBlock(pos.x+9, pos.y+i, pos.z+j, block.WOOD.id)



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
