from mcpi.minecraft import Minecraft
import mcpi.block as block
#pos.x,pos.y,pos.z
def roof(x0,y0,z0,L,W,H,M):
    p=open("roof.csv",'r').read().split('\n')
    a=-1
    for i in p:
        a=a+1
        b=-1
        for j in i:
            b=b+1
            if j=='1':
                mc.setBlock (x0+1+b,y0+H,z0+a,M)
    return
def house(x0,y0,z0,L,W,H,M1,Mroof):
    for a in range(L):
        for j in range(W):
            for k in range(H):
                mc.setBlock (x0+1+a,y0+j,z0+k,M1)
    for a in range(L-2):
        for j in range(W-2):
            for k in range(H-2):
                mc.setBlock (x0+2+a,y0+1+j,z0+1+k,0)
    mc.setBlock (x0+1,y0+1,z0+W/2,0)
    mc.setBlock (x0+1,y0+2,z0+W/2,0)
    mc.setBlock (x0,y0,z0+W/2,M1)
    mc.setBlock (x0,y0+2,z0+W/2+1,50)
    mc.setBlock (x0,y0+2,z0+W/2-1,50)
    mc.setBlock (x0+L-1,y0+H-2,z0+W-2,50)
    mc.setBlock (x0+L-1,y0+H-2,z0+1,50)
    mc.setBlock (x0+L-1,y0+1,z0+1,26)
    mc.setBlock (x0+L-1,y0+1,z0+2,26)
    roof(x0,y0,z0,L,W,H,Mroof)
    for a in range(2):
        for j in range(2):
            mc.setBlock (x0+L/2+a,y0+H-4+j,z0+W-1,20)
    return
def clear(L):
    pos=mc.player.getTilePos()
    for a in range(-L,L+1):
        for b in range(-L,L+1):
            for c in range(-L,L+1):
                mc.setBlock (pos.x+a,pos.y+b,pos.z+c,0)
    return
def manyhouse(x0,y0,z0,L,W,H,M,n):
    for a in range(0,2*n*L,2*L):
        for j in range(0,2*n*L,2*L):
            for k in range(0,2*n*L,2*L):
                house(x0+a,y0+j,z0+k,L,W,H,M)
    return

mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
    clear(50)
