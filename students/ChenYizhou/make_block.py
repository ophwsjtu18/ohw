import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
# mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)

for i in range(1, 11):
    for j in range(1,11):
        # walls
        mc.setBlock(pos.x, pos.y+i, pos.z+j, block.STONE.id)
        mc.setBlock(pos.x+i, pos.y+j, pos.z, block.STONE.id)
        mc.setBlock(pos.x+10, pos.y+i, pos.z+j, block.STONE.id)
        mc.setBlock(pos.x+i, pos.y+j, pos.z+10, block.STONE.id)
        # glass ceiling
        mc.setBlock(pos.x+i, pos.y+10, pos.z+j, block.GLASS.id)
        # floor
        mc.setBlock(pos.x+i, pos.y, pos.z+j, 5)
# door
for i in range(3,5):
    for j in range(4):
        mc.setBlock(pos.x, pos.y+j, pos.z+i, 0)
