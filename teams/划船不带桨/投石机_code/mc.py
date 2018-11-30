# coding:utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
# import mcpi.minecraftstuff as minecraftstuff
import time
from random import *
from math import *
import serial

'''
打击钻石块时会向串口（com5）发送一个字符串，格式为“角度，1”
'''

#ser=serial.Serial("COM5",115200,timeout=0.5)

mc=minecraft.Minecraft.create()

def build():
    mc.setBlocks(0,19,0,100,19,100,block.DIAMOND_BLOCK.id)
    mc.setBlocks(0,20,0,0,20,100,block.DIAMOND_BLOCK.id)
    mc.setBlocks(1,20,0,100,20,0,block.DIAMOND_BLOCK.id)
    mc.setBlocks(1,20,100,100,20,100,block.DIAMOND_BLOCK.id)
    mc.setBlocks(100,20,1,100,20,99,block.DIAMOND_BLOCK.id)
    mc.player.setTilePos(50,20,49)
    mc.setBlock(50,20,50,block.DIAMOND_BLOCK.id)

def checkhit():
    events=mc.events.pollBlockHits()
    for e in events:
        pos=e.pos
        if pos.x==50 and pos.y==20 and pos.z==50:
            fire()
            #info=str(dir())+',1'
            #ser.write(info.encode())


def house(x,y,z):
    midx=x+size/2
    midy=y+size/2
    mc.setBlocks(x,y,z,x+size,y+size,z+size,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+size-2,y+size-1,z+size-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+size-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+size-3,z,x+size-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+size-1,z,x+size,y+size-1,z+size,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z+1,x+size-2,y-1,z+size-2,block.WOOL.id,14)


def boom(x,y,z):
    mc.setBlock(x,y,z,block.TNT.id)
    mc.setBlock(x+1, y, z+1, block.TNT.id)
    mc.setBlock(x+1, y, z, block.TNT.id)
    mc.setBlock(x, y, z+1, block.TNT.id)
    mc.setBlock(x,y+1,z,block.FIRE.id)
    mc.setBlock(x+1, y + 1, z+1, block.FIRE.id)
    mc.setBlock(x+1, y + 1, z, block.FIRE.id)
    mc.setBlock(x, y + 1, z+1, block.FIRE.id)

def fire():
    x=randrange(20,50)
    y=randrange(20,30)
    mc.postToChat(str(50+x*sin(dir()))+","+str(50+x*cos(dir())))
    boom(50+x*sin(dir()),y,50+x*cos(dir()))
    mc.postToChat(str(50+x*sin(dir()))+'='+str(50+x*cos(dir())))
    mc.postToChat("fire!")



def dir():
    pos=mc.player.getPos()
    if(pos.x>50):
        arr=acos((50-pos.z)/sqrt((50-pos.z)**2+(50-pos.x)**2))
    else:
        arr = -acos((50 - pos.z) / sqrt((50 - pos.z) ** 2 + (50 - pos.x) ** 2))
    return arr

def person(x,y,z):
    mc.setBlocks(x-1,y,z,x-1,y+2,z,block.DIAMOND_BLOCK.id)
    mc.setBlocks(x+1,y,z,x+1,y+2,z,block.DIAMOND_BLOCK.id)
    mc.setBlocks(x-1,y+2,z,x+1,y+6,z,block.DIAMOND_BLOCK.id)
    mc.setBlock(x,y+7,z,block.DIAMOND_BLOCK.id)
    mc.setBlocks(x-2,y+4,z,x-2,y+6,z,block.DIAMOND_BLOCK.id)
    mc.setBlocks(x+2,y+4,z,x+2,y+6,z,block.DIAMOND_BLOCK.id)

size=10
for i in range(3):
    for j in range(3):
        house((i+1)*25,20,(j+1)*25)


mc.setBlocks(50,20,50,60,30,60,block.AIR.id)
mc.setBlocks(51, 19, 51, 58, 19, 58, block.DIAMOND_BLOCK.id)
build()
person(60,20,60)


while True:
    checkhit()
#ser.close()