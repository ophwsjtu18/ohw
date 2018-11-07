import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)

def house(x0,y0,z0,L,W,H,M):
    for x in range(L):
        for y in range (H):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W,M)
    for z in range(W):
        for y in range(H):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L,y0+y,z0+z,M)
    for x in range(L):
        for y in range(W):
            mc.setBlock(x0+x,y0+y,z0+H,M)

house(pos.x+5,pos.y,pos.z+5,10,10,10,89)

class hhouse():
    def __init__(self,data):
        self.data=data
    def
