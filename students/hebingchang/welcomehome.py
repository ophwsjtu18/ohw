<<<<<<< HEAD
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
        
     
=======
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
stayed_time = 0
pos = mc.player.getTilePos()

for i in range(-5, 6):
    for j in range(-5, 6):
        mc.setBlock(pos.x + i, pos.y - 1, pos.z + j, 5)
        mc.setBlock(pos.x + i, pos.y + 6, pos.z + j, block.GLASS.id)

for x in range(pos.x - 5, pos.x + 6):
    for z in range(pos.z - 5, pos.z + 6):
        for i in range(1, 7):
            mc.setBlock(x, pos.y + i - 1, pos.z - 5, block.STONE.id)
            mc.setBlock(x, pos.y + i - 1, pos.z + 5, block.STONE.id)
            mc.setBlock(pos.x - 5, pos.y + i - 1, z, block.STONE.id)
            mc.setBlock(pos.x + 5, pos.y + i - 1, z, block.STONE.id)

for i in range(2):
    for j in range(2):
        mc.setBlock(pos.x + j, pos.y + i + 1, pos.z - 5, block.GLASS.id)

mc.setBlock(pos.x + 5, pos.y, pos.z, 0)
mc.setBlock(pos.x + 5, pos.y + 1, pos.z, 0)
>>>>>>> e7405fab035d8fe060491f4cc6a54336309375b6
