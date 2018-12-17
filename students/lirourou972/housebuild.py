import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
#mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)

#def hhouse(x0,y0,z0,L,W,H,M):
#    for x in range(L):
#        for y in range (H):
#            mc.setBlock(x0+x,y0+y,z0,M)
#            mc.setBlock(x0+x,y0+y,z0+W,M)
#    for z in range(W):
#        for y in range(H):
#            mc.setBlock(x0,y0+y,z0+z,M)
#            mc.setBlock(x0+L,y0+y,z0+z,M)
#    for x in range(L):
#        for y in range(W):
#            mc.setBlock(x0+x,y0+y,z0+H,M)

#house(pos.x+5,pos.y,pos.z+5,10,10,10,89)

class house():
    def __init__(self,data):
        self.data=data
    def roof(self):
        x0=self[0]
        z0=self[1]
        y0=self[2]
        for x in range(11):
            for z in range (11):
                mc.setBlock(x0+x,y+10,z0+z,89)

    def buildwallwithdoor(self):
        x0=self[0]
        z0=self[1]
        y0=self[2]
        for y in range(7):
            for z in range(5):
                mc.setBlock(x0+10,y0+y,z0+z,89)
            mc.setBlock(x0+10,y+10,z0+5,102)
            for z in range(6,11):
                mc.setBlock(x0+10,y0+y,z0+z,89)
        for y in range(7,11):
            for z in range(11):
                mc.setBlock(x0+10,y0+y,z0+z,89)

    def buildwall(self):
        x0=self[0]
        z0=self[1]
        y0=self[2]
        for y in range(11):
            for z in range(11):
                mc.setBlock(x0,y0+y,z0+z,89)

    def buildwallwithwindow(self):
        x0=self[0]
        z0=self[1]
        y0=self[2]
        for y in range(4):
            for x in range(11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
        for y in range(7,11):
            for x in range(11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
        for y in range(4,7):
            for x in range(4):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
            for x in range(4,7):
                mc.setBlock(x0+x,y0+y,z0,102)
                mc.setBlock(x0+x,y0+y,z0+10,102)
            for x in range(7,11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)



    def buildall(self):
        x0=self[0]
        z0=self[1]
        y0=self[2]
#buildroof
        for x in range(11):
            for z in range (11):
                mc.setBlock(x0+x,y+10,z0+z,89)
#buildwallwithdoor
        for y in range(7):
            for z in range(5):
                mc.setBlock(x0+10,y0+y,z0+z,89)
                mc.setBlock(x0+10,y+10,z0+5,102)
            for z in range(6,11):
                mc.setBlock(x0+10,y0+y,z0+z,89)
        for y in range(7,11):
            for z in range(11):
                mc.setBlock(x0+10,y0+y,z0+z,89)
#buildwall
        for y in range(11):
            for z in range(11):
                mc.setBlock(x0,y0+y,z0+z,89)
#buildwallwithwindow
        for y in range(4):
            for x in range(11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
        for y in range(7,11):
            for x in range(11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
        for y in range(4,7):
            for x in range(4):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)
            for x in range(4,7):
                mc.setBlock(x0+x,y0+y,z0,102)
                mc.setBlock(x0+x,y0+y,z0+10,102)
            for x in range(7,11):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+10,89)

mh1=house([pos.x+3,pos.z+3,pos.y])
mh1.buildwall()
mh1.buildroof()
mh1.buildwallwithdoor()
mh1.buildwallwithwindow()
