from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
pos = mc.player.getTilePos()
for x in range(10):
    for y in range(10):
        mc.setBlock(pos.x + x, pos.y + y, pos.z, 1)
        mc.setBlock(pos.x + x, pos.y + y, pos.z + 10, 1)

for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x + x, pos.y, pos.z + z, 2)
        mc.setBlock(pos.x + x, pos.y + 10, pos.z + z, 3)
for y in range(10):
    for z in range(10):
            mc.setBlock(pos.x , pos.y + y, pos.z + z, 4)
            mc.setBlock(pos.x + 10, pos.y + y, pos.z + z, 5)
for x in range(3): //门
    for y in range(5):
        mc.setBlock(pos.x + 5 + x, pos.y + y, pos.z, 0)
for x in range(2): //窗户
    for z in range(2):
        mc.setBlock(pos.x + x + 5, pos.y, pos.z + z + 5, 10)




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
