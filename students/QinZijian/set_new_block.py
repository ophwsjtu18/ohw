from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x + 3, pos.y, pos.z, 1)
