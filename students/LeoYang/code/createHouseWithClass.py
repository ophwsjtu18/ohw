import mcpi.minecraft as minecraft
import mcpi.block as block

class house():
    def __init__(self,pos):
        self.pos=pos

    def wall(self):
        xo = self.pos[0]
        yo = self.pos[1]
        zo = self.pos[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(xo+x,yo+z,zo,89)
                mc.setBlock(xo+x,yo+z,zo+10,89)
        for y in range(11):
            for z in range(11):
                mc.setBlock(xo,yo+z,zo+y,89)
                mc.setBlock(xo+10,yo+z,zo+y,89)

    def roof(self):
        xo = self.pos[0]
        yo = self.pos[1]
        zo = self.pos[2]
        for x in range(11):
            for y in range(11):
                mc.setBlock(xo+x,yo+11,zo+y,89)

    def floor(self):
        xo = self.pos[0]
        yo = self.pos[1]
        zo = self.pos[2]
        for x in range(11):
            for y in range(11):
                mc.setBlock(xo+x,yo,zo+y,89)

    def door(self):
        xo = self.pos[0]
        yo = self.pos[1]
        zo = self.pos[2]
        for z in range(5):
            mc.setBlock(xo+5,yo+z,zo,0)
            mc.setBlock(xo+5,yo+z+1,zo,0)

    def window(self):
        xo = self.pos[0]
        yo = self.pos[1]
        zo = self.pos[2]
        for z in range(4):
            mc.setBlock(xo+10,yo+z+3,zo+5,0)
            mc.setBlock(xo+10,yo+z+3,zo+5-1,0)
            mc.setBlock(xo+10,yo+z+3,zo+5+1,0)
            mc.setBlock(xo+10,yo+z+3,zo+5+2,0)

    def allInOne(self):
        self.wall()
        self.roof()
        self.floor()
        self.door()
        self.window()


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
#mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)
for i in range(3):
    for j in range(3):
        for k in range(3):
            newHouse = house([pos.x+20*i,pos.y+20*j,pos.z+15*k])
            newHouse.allInOne()
