import mcpi.minecraft as minecraft
import mcpi.block as block

class House(object):
    def __init__(self, mc, x, y, z, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.mc = mc

    def build_ceiling_floor(self):
        for i in range(self.width):
            for j in range(self.width):
                self.mc.setBlock(self.x + i, self.y, self.z + j, block.GRASS.id)
                self.mc.setBlock(self.x + i, self.y + self.height, self.z + j, block.TNT.id)

    def build_walls(self):
        for i in range(self.width):
            for k in range(self.height):
                self.mc.setBlock(self.x + i, self.y + k, self.z, 89)
                self.mc.setBlock(self.x + i, self.y + k, self.z + self.width - 1, 89)
                self.mc.setBlock(self.x, self.y + k, self.z + i, 89)
                self.mc.setBlock(self.x + self.width - 1, self.y + k, self.z + i, 89)

    def build_windows_door(self):
        # windows
        window_length = 4
        window_margin = (int(self.width / 2) - window_length / 2, int(self.height / 2) - window_length / 2)
        for m in range(window_length):
            for n in range(window_length):
                self.mc.setBlock(self.x + window_margin[0] + m, self.y + window_margin[1] + n, self.z, block.GLASS.id)
                self.mc.setBlock(self.x + window_margin[0] + m, self.y + window_margin[1] + n, self.z + self.width - 1, block.GLASS.id)
                self.mc.setBlock(self.x, self.y + window_margin[1] + n, self.z + window_margin[0] + m, block.GLASS.id)
        # door
        door_length = 3
        door_height = 4
        for a in range(door_height):
            for b in range(door_length):
                self.mc.setBlock(self.x + self.width - 1, self.y + 1 + a, self.z + int(self.width / 2) + b, 0)

    def build_all(self):
        self.build_ceiling_floor()
        self.build_walls()
        self.build_windows_door()

def main():
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    house_num = 3
    interval = 20
    for i in range(house_num):
        for j in range(house_num):
            for k in range(house_num):
                house = House(mc, pos.x+i*interval, pos.y+j*interval, pos.z+k*interval, 12, 8)
                house.build_all()

main()


