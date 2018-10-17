from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
stayed_time = 0
pos = mc.player.getTilePos()

for i in range(-5, 6):
    for j in range(-5, 6):
        mc.setBlock(pos.x + i, pos.y - 1, pos.z + j, 5)
        mc.setBlock(pos.x + i, pos.y + 6, pos.z + j, block.GLASS.id)

for x in range(pos.x - 5, pos.x + 6):
    for z in range(pos.z - 5, pos.z + 6):
        for i in range(1, 7):
            mc.setBlock(x, pos.y + i - 1, pos.z - 5, block.STONE.id)
            mc.setBlock(x, pos.y + i - 1, pos.z + 5, block.STONE.id)
            mc.setBlock(pos.x - 5, pos.y + i - 1, z, block.STONE.id)
            mc.setBlock(pos.x + 5, pos.y + i - 1, z, block.STONE.id)

for i in range(2):
    for j in range(2):
        mc.setBlock(pos.x + j, pos.y + i + 1, pos.z - 5, block.GLASS.id)

mc.setBlock(pos.x + 5, pos.y, pos.z, 0)
mc.setBlock(pos.x + 5, pos.y + 1, pos.z, 0)