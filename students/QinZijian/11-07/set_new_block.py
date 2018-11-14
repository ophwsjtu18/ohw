from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos = mc.player.getTilePos()

def house(x0, y0, z0, L, W, H, M):
    for x in range(L):
        for y in range(H):
            for z in range(W):
                mc.setBlock(x0 + x, y0 + y, z0 + z, M)

#new

    for x in range(L - 2):
        for y in range(H - 2):
            for z in range(W - 2):
                mc.setBlock(x0 + x + 1, y0 + y + 1, z0 + z + 1, 0)
while True:
    mc.postToChat("x: " + str(pos.x) + "y: " + str(pos.y) + "z: " + str(pos.z))

house(pos.x, pos.y, pos.z, 3, 3, 3, 89)
