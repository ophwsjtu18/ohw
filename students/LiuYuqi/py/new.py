import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create() # 和服务器建立连接
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)


def house(x0,y0,z0,L,W,H,M):
    for x in range(L):
        for y in range(H):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W,M)
    for z in range(W):
        for y in range(H):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L,y0+y,z0+z,M)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0,z0+z,M)
            mc.setBlock(x0+x,y0+H,z0+z,M)

    mc.setBlock(x0+2,y0,z0+2,50) #火把

    for x in range(int(L/4),int(3*L/4)):
        for y in range(int(H/2)):
            mc.setBlock(x0+x,y0+y,z0,0)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0,y0+int(3*H/4)+y,z0+int(3*W/4)+z,20)


for i in range(3):
    for j in range(3):
        for k in range(3):
            house(pos.x+i*16+16,pos.y+j*16+16,pos.z+k*16+16,16,16,16,42)
