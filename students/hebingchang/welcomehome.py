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
            b = block.STONE.id
            if 3 <= i <= 4:
                b = block.GLASS.id
            mc.setBlock(x, pos.y + i - 1, pos.z - 5, b)
            mc.setBlock(x, pos.y + i - 1, pos.z + 5, b)
            mc.setBlock(pos.x - 5, pos.y + i - 1, z, b)
            mc.setBlock(pos.x + 5, pos.y + i - 1, z, b)

mc.setBlock(pos.x + 5, pos.y, pos.z, 0)
mc.setBlock(pos.x + 5, pos.y + 1, pos.z, 0)