from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0
import mcpi.block as block
pos= mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)

for y in range(6):
    for x in range(10):
        mc.setBlock(pos.x,pos.y+y,pos.z+x,57)
for y in range(6):
    for x in range (10):
        mc.setBlock(pos.x+x,pos.y+y,pos.z+10,57)
for y in range (6):
    for x in range(10):
        mc.setBlock(pos.x+10,pos.y+y,pos.z+x,57)
for y in range(2):
    for x in range(5):
        mc.setBlock(pos.x+x,pos.y+y,pos.z,57)
        mc.setBlock(pos.x+6,pos.y+y,pos.z,1)
    for x in range(3):
        mc.setBlock(pos.x+7+x,pos.y+y,pos.z+x,57)
for y in range(3):
    for x in range(10):
        mc.setBlock(pos.x+x,pos.y+y,pos.z,57)
for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x,pos.y+6,pos.z+z,57)


import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)




while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x=30 and  pos.y=-6  and pos.z=-40 :
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
