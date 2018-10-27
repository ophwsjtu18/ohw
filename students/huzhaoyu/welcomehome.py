<<<<<<< HEAD
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     
=======
from mcpi.minecraft import Minecraft
<<<<<<< HEAD
import mcpi.minecraft as minecraft
import mcpi.block as block
=======
>>>>>>> e8aed27c6d267be7dd65c3a282f6000dcba73f2a
import time

mc=Minecraft.create()

stayed_time=0
<<<<<<< HEAD
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for i in range(10):
    for j in range(6):
        mc.setBlock(pos.x+i,pos.y+j,pos.z,87)
        mc.setBlock(pos.x+i,pos.y+j,pos.z+10,85)
        mc.setBlock(pos.x,pos.y+j,pos.z+i,86)
        mc.setBlock(pos.x+10,pos.y+j,pos.z+i,83)
for i in range(10):
    for j in range(6):
        mc.setBlock(pos.x+i,pos.y,pos.z+j,81)

mc.setBlock(pos.x+5,pos.y+1,pos.z,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z,0)
mc.setBlock(pos.x,pos.y+2,pos.z+2,20)
mc.setBlock(pos.x,pos.y+2,pos.z+1,20)
mc.setBlock(pos.x,pos.y+3,pos.z+2,20)
mc.setBlock(pos.x,pos.y+3,pos.z+1,20)
        
        
    

=======
>>>>>>> e8aed27c6d267be7dd65c3a282f6000dcba73f2a

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
<<<<<<< HEAD
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
=======
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
>>>>>>> e8aed27c6d267be7dd65c3a282f6000dcba73f2a
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
<<<<<<< HEAD
=======
        
     
>>>>>>> e8aed27c6d267be7dd65c3a282f6000dcba73f2a
>>>>>>> e7405fab035d8fe060491f4cc6a54336309375b6
