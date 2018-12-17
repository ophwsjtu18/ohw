import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

class wallbuild():
    def __init__(self, pos,size):
        self.pos=pos
        self.size=size
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        L=self.size[0]
        W=self.size[1]
        H=self.size[2]
        for x in range(L):
            for y in range(H):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+W,89)
        for z in range(W):
            for y in range(H):
                mc.setBlock(x0,y0+y,z0+z,89)
                mc.setBlock(x0+L,y0+y,z0+z,89)
