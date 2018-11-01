from mcpi.minecraft import Minecraft
import mcpi.block as block

import time
import Sing_A_Song

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
pos = mc.player.getTilePos()

'''
def build(x_range,y_range,z_range,material):
    for x in x_range:
        for y in y_range:
            for z in z_range:
                mc.setBlock(pos.x+x ,pos.y+y,pos.z+z,material)

build(range(-5,5),range(6),[-5,5],21) # wall
build([-5,5],range(6),range(-5,5),21) # wall
build(range(-5,5),[0,6], range(-5,5),22) # roof
build([5],range(3),range(-1,1),0) # door
build([5],[4,5],range(0,2),20) # window
'''

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
            Sing_A_Song.song()
            stayed_time=0
    else:
        stayed_time=0
