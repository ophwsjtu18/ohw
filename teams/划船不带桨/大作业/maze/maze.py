from mcpi.minecraft import Minecraft
import mcpi.block as block


def build_maze():
    mc = Minecraft.create()
    pos = mc.player.getTilePos()

    GAP = block.AIR.id
    WALL = block.GOLD_BLOCK.id
    FLOOR = block.GRASS.id

    origin_x = pos.x + 1
    origin_y = pos.y
    origin_z = pos.z + 1

    z = origin_z

    f = open('maze.csv', 'r')
    for line in f.readlines():
        data = line.split(',')
        #print(data)
        x = origin_x
        for cell in data:
            #print(cell)
            if cell == " " or cell == '+':
                b = GAP
            else:
                b = WALL
            for i in range(2):
                for j in range(2):
                    mc.setBlock(x + i, origin_y, z + j, b)
                    mc.setBlock(x + i, origin_y + 1, z + j, b)
                    mc.setBlock(x + i, origin_y - 1, z + j, FLOOR)

            x = x + 2
        z = z + 2
#build_maze()


'''
map_point = open('maze.csv', 'r').read().split('\n')

print(map_point)

for y in len(map_point): #列
    for x in len(map_point[0]): #行
        if map_point[y][x] == 0:
            mc.setBlock(pos.x + x, pos.y + y, pos.z, 0)
        elif map_point[y][x] == 1:
            mc.setBlock(pos.x + x, pos.y + y, pos.z, 1)
'''
