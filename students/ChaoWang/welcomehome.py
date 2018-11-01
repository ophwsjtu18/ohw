# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time = 0
pos = mc.player.getTilePos()

#建房屋
#上下
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+i,pos.y+5,pos.z+j,block.STONE,89)
        mc.setBlock(pos.x+i,pos.y,pos.z+j,block.STONE,89)
#左右
for i in range(10):
    for j in range(6):
        if ((i==4 or i ==5) and (j==2 or j==3)):  #窗户
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.STONE,20)
        else:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.STONE,89)
#前后
for i in range(10):
    for j in range(6):
        mc.setBlock(pos.x+i,pos.y+j,pos.z+9,block.STONE,89)
        if ((i==4 or i ==5) and (j==0 or j==1 or j==2)):  #门
            mc.setBlock(pos.x+i,pos.y+j,pos.z,block.STONE,0)
        else:
            mc.setBlock(pos.x+i,pos.y+j,pos.z,block.STONE,89)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
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
