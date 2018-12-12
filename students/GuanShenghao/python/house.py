from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,1)

def house(x0,y0,z0,L,W,H,M):   #M means material
    for x in range(L):
        for z in range(W):
            for y in range(H):
                mc.setBlock(x0+x,y0+y,z0+z,M)
    for x in range(L-2):
        for z in range(W-2):
            for y in range(H-2):
                mc.setBlock(x0+1+x,y0+1+y,z0+1+z,0)
    #door
    x1=int(L/2)
    mc.setBlock(x0+x1,y0+1,z0,0)
    mc.setBlock(x0+x1,y0+2,z0,0)
    #window
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0+4,z0+z,20)
    for x in range(L-2):
        for z in range(W-2):
            mc.setBlock(x0+1+x,y0+4,z0+z+1,0)
    #light
    for x in range(L-2):
        for z in range(W-2):
            mc.setBlock(x0+1+x,y0+H-1,z0+z+1,89)
for i in range(30):
    m=12*i
    house(pos.x+m,pos.y,pos.z,9,9,6,5)
