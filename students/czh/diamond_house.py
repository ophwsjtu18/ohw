from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0

#x=-9 y=0 z=89




for y in range(66):
    for z in range(44):
        for x in range(88):
            mc.setBlock(-x+20,y,z+77,block.AIR.id)#清空一下地面其他东西




for y in range(19):
    for z in range(10):
        mc.setBlock(-9,y,z+87,block.DIAMOND_BLOCK.id)
        mc.setBlock(-19,y,z+87,block.DIAMOND_BLOCK.id)
    for x in range(11):
        mc.setBlock(x-19,y,97,block.DIAMOND_BLOCK.id)
        mc.setBlock(x-19,y,87,block.DIAMOND_BLOCK.id)#钻石外壳
for y in range(2):
    for z in range(18):
        mc.setBlock(-7,y,z+83,block.FENCE.id)
        mc.setBlock(-22,y,z+83,block.FENCE.id)
    for x in range(15):
        mc.setBlock(x-22,y,100,block.FENCE.id)
        mc.setBlock(x-22,y,83,block.FENCE.id)#篱笆



for x in range(11):
    for z in range(15):
        m=z
        if m<=7:
            mc.setBlock(x-19,m+18,z+85,block.STONE_BRICK.id)
        else:
            mc.setBlock(x-19,22-m+8,z+85,block.STONE_BRICK.id)#房顶1
for x in range(10):
    for z in range(13):
        m=z
        if m<=6:
            mc.setBlock(x-19,m+17,z+86,block.DIAMOND_BLOCK.id)
        else:
            mc.setBlock(x-19,22-m+7,z+86,block.DIAMOND_BLOCK.id)#房顶2




for y in range(2):
    for x in range(4):
        mc.setBlock(x-15,4+y,97,block.GLASS_PANE.id)
        mc.setBlock(x-15,4+y,87,block.GLASS_PANE.id)#窗户
      


for y in range(5):
    for z in range(3):
            mc.setBlock(-9,y,91+z,block.AIR.id)
            mc.setBlock(-7,y,91+z,block.AIR.id)#门


for x in range(11):
    for z in range(11):
        mc.setBlock(x-19,-1,z+87,block.WOOD_PLANKS.id)#地板
for x in range(1,10):
    for z in range(1,10):
        mc.setBlock(x-19,0,z+87,block.AIR.id)#空气1（地面）
for x in range(11):
    for z in range(11):
        mc.setBlock(x-19,7,z+87,block.WOOD.id)#天花板1     
for x in range(11):
    for z in range(11):
        mc.setBlock(x-19,14,z+87,block.WOOD.id)#天花板2

mc.setBlock(-18,7,88,block.AIR.id)
mc.setBlock(-18,7,89,block.AIR.id)
for x in range(2):
    mc.setBlock(x-17,7,89,block.AIR.id)
    mc.setBlock(x-17,7,88,block.AIR.id)#空气2（楼梯）
for z in range(9):
    mc.setBlock(-18,6,88+z,block.TORCH.id)
    mc.setBlock(-10,6,88+z,block.TORCH.id)
    mc.setBlock(-10,13,88+z,block.TORCH.id)
    mc.setBlock(-18,12,88+z,block.TORCH.id)#火把
for z in range(7):
    mc.setBlock(-18,17,95-z,block.TORCH.id)
    mc.setBlock(-10,17,95-z,block.TORCH.id)



for x in range(4):
    for z in range(2):
        mc.setBlock(-x-16,0,z+95,block.BEDROCK.id)
mc.setBlock(-18,0,94,block.CRAFTING_TABLE.id)#桌子
for y in range(4):
    for z in range(3):
        mc.setBlock(-18,y,93-z,block.BOOKSHELF.id)#书架
for x in range(7):
    mc.setBlock(-x-12,x,89,block.WOOD.id)
    mc.setBlock(-x-12,x,88,block.WOOD.id)#梯子1
for z in range(7):
    mc.setBlock(-18,z+8,z+91,block.WOOD.id)
    mc.setBlock(-17,z+8,z+91,block.WOOD.id)#梯子2
for x in range(2):
    mc.setBlock(-x-17,14,96,block.AIR.id)
    mc.setBlock(-x-17,14,95,block.AIR.id)
    mc.setBlock(-x-17,14,94,block.AIR.id)#空气2（楼梯）
for y in range(4):
    for x in range(7):
        mc.setBlock(x-17,8+y,97,block.GLASS_PANE.id)
        mc.setBlock(x-17,8+y,87,block.GLASS_PANE.id)#窗户
for z in range(3):
    for y in range(4):
        mc.setBlock(-10,8+y,88+z,block.BOOKSHELF.id)#书架
for z in range(3):
        mc.setBlock(-10,8,91+z,block.CRAFTING_TABLE.id)#桌子
for z in range(2):
    for y in range(4):
        mc.setBlock(-10,8+y,94+z,block.CHEST.id)#柜子



while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-9 y=0 z=89 for 15s to find the diamond")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x<=-6 and  pos.x>=-12 and pos.y==-0 and pos.z>=89 and pos.z<=94:
        mc.postToChat("welcome")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.setBlock(-9,0,99,block.DIAMOND_BLOCK.id)
            stayed_time=0
    else:
        stayed_time=0
        
     
