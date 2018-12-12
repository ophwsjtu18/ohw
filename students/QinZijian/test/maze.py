from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
pos = mc.player.getTilePos()

map_point = open('maze.csv', 'r').read().split('\n')

print(map_point)

for y in len(map_point): #列
    for x in len(map_point[0]): #行
        if map_point[y][x] == 0:
            mc.setBlock(pos.x + x, pos.y + y, pos.z, 0)
        elif map_point[y][x] == 1:
            mc.setBlock(pos.x + x, pos.y + y, pos.z, 1)

