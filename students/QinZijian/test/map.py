from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
pos = mc.player.getTilePos()

f = open('map_point.csv', 'r')
map_point = f.read().split('\n')

print(map_point)
for y in len(map_point):
    for x in len(map_point[0]):
        if map_point[y][x] == 0:
            mc.setBlock(pos.x, pos.y, pos.z, 0)
        elif map_point[y][x] == 1:
            mc.setBlock(pos.x + x, pos.y + y, pos.z, 1)

