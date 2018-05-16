from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0

#-15,0,42

mc.setBlock(-9,0,42,block.DIAMOND_BLOCK.id)
for y in range(4):
    for z in range(10):
        mc.setBlock(-9,y,z+37,block.DIAMOND_BLOCK.id)
        mc.setBlock(-19,y,z+37,block.DIAMOND_BLOCK.id)
    for x in range(11):
        mc.setBlock(x-19,y,47,block.DIAMOND_BLOCK.id)
        mc.setBlock(x-19,y,37,block.DIAMOND_BLOCK.id)
for x in range(11):
    for z in range(10):
        mc.setBlock(x-19,4,z+37,block.DIAMOND_BLOCK.id)

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-9 y=0 z=42 for 15s to find the diamond")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x<=-6 and  pos.x>=-12 and pos.y==-0 and pos.z>=39 and pos.z<=42:
        mc.postToChat("welcome")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.setBlock(-9,0,42,block.DIAMOND_BLOCK.id)
            stayed_time=0
    else:
        stayed_time=0
        
     
