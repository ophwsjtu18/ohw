from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
pos=mc.player.getTilePos()
for a in range(9):
    for j in range(9):
        mc.setBlock (pos.x+3+a,pos.y,pos.z+j,89)
for a in range(4):
    for j in range(9):
        mc.setBlock (pos.x+3,pos.y+1+a,pos.z+j,89)
for a in range(4):
    for j in range(8):
        mc.setBlock (pos.x+11,pos.y+a+1,pos.z+j,89)
for a in range(9):
    for j in range(9):
        mc.setBlock (pos.x+3+a,pos.y+5,pos.z+j,88)
for a in range(5):
    for j in range(9):
        mc.setBlock (pos.x+3+j,pos.y+a,pos.z+8,89)
for a in [1,2,3,4,6,7,8]:
    for j in range(5):
        mc.setBlock (pos.x+3+a,pos.y+j,pos.z,89)
for j in range(2):
    mc.setBlock (pos.x+3+5,pos.y+j+3,pos.z,89)
for a in range(2):
    for j in range(2):
        mc.setBlock (pos.x+3,pos.y+2+j,pos.z+4+a,20)


while True:
    print("stay_time"+str(stayed_time))
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
