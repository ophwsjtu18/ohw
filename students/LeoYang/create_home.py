import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

for i in [1,10] :
    mc.setBlock(pos.x+3,pos.y,pos.z+i/10,block.STONE.id)
