from mcpi.minecraft import Minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc=Minecraft.create()

stayed_time=0
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
# the wall
for i in range(11):
    for j in range(7):
        mc.setBlock(pos.x+i,pos.y+j,pos.z,89)
        mc.setBlock(pos.x+i,pos.y+j,pos.z+10,89)
for i in range(11):
    for j in range(7):
        mc.setBlock(pos.x,pos.y+j,pos.z+i,89)
        mc.setBlock(pos.x+10,pos.y+j,pos.z+i,89)
for i in range(6):
    for j in range(i):
        mc.setBlock(pos.x+i,pos.y+7+j,pos.z,89)
        mc.setBlock(pos.x+10-i,pos.y+7+j,pos.z,89)
        mc.setBlock(pos.x+i,pos.y+7+j,pos.z+10,89)
        mc.setBlock(pos.x+10-i,pos.y+7+j,pos.z+10,89)
# the floor
for i in range(11):
    for j in range(11):
        mc.setBlock(pos.x+i,pos.y,pos.z+j,1)
# the ceiling
for i in range(7):
    for j in range(13):
        mc.setBlock(pos.x+i-1,pos.y+6+i,pos.z+j-1,22)
        mc.setBlock(pos.x+11-i,pos.y+6+i,pos.z+j-1,22)
# the door
mc.setBlock(pos.x+5,pos.y,pos.z,44)
mc.setBlock(pos.x+5,pos.y+1,pos.z,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z,0)
# the window
for i in range(2):
    for j in range(2):    
        mc.setBlock(pos.x+1+i,pos.y+1+j,pos.z,20)

    
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

