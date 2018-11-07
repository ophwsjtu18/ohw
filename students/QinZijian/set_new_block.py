from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos = mc.player.getTilePos()

def house(x0, y0, z0, L, W, H, M):
    for x in range(L):
        mc.setBlock(x0 + x, y0, z0, M)
    for y in range(H):
        mc.setBlock(x0, y0 + y, z0, M)
    for z in range(W):
        mc.setBlock(x0, y0, z0 + z, M)

house(40, 20, 50, 10, 10, 6, 1)
