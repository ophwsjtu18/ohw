from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
pos = mc.player.getTilePos()


def HouseBuild(x0,y0,z0,L,W,H,M):
    #上下面
    for i in range(L):
        for j in range(W):
            mc.setBlock(x0+i,y0+H-1,z0+j,M)
            mc.setBlock(x0+i,y0,z0+j,M)
    #左右面
    for i in range(W):
        for j in range(H):
            if ((i==W/2 or i==(W/2-1)) and (j==H/2 or j==H/2-1)):  #窗户
                mc.setBlock(x0,y0+j,z0+i,20)
                mc.setBlock(x0+L-1,y0+j,z0+i,20)
            else:
                mc.setBlock(x0,y0+j,z0+i,M)
                mc.setBlock(x0+L-1,y0+j,z0+i,M)

    #前后面
    for i in range(L):
        for j in range(H):
            mc.setBlock(x0+i,y0+j,z0+W-1,M)
            if ((i==L/2 or i==(L/2-1)) and (j==1 or j==2 or j==3)):  #门
                continue
            else:
                mc.setBlock(x0+i,y0+j,z0,M)


for i in range(3):
    for j in range(3):
        for k in range(3):
            HouseBuild(pos.x+10*i,pos.y+10*j,pos.z+10*k,8,8,6,1)
