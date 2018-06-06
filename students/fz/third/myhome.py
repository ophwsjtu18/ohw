from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()

stayed_time=0
#clear
for x in range(40):
    for y in range(40):
        for z in range(40):
            mc.setBlock(-39+x,y,16+z,block.AIR.id)
        

cx = -14
cy = 0
cz = 42
#me

mc.player.setTilePos(-20,10,40)

#paint glassfloor and lava
for x in range(27):
    for y in range(3):
        for z in range(28):
            if x == 0 or x == 26:
                mc.setBlock(x-27,-1-y,z+28,block.LAVA_FLOWING.id)

for x in range(25):
    for y in range(3):
        for z in range(26):
            mc.setBlock(x-26,-1-y,z+29,block.GLASS.id)

for x in range(27):
    for y in range(100):
        for z in range(28):
            mc.setBlock(x-27,-3-y,z+28,block.AIR.id)


#paint flower
for x in range(17):
    for y in range(1):
        for z in range(18):
            mc.setBlock(x-22,y-1,z+33,block.GRASS.id)
            if (x + z) % 2 == 0:
                mc.setBlock(x-22,y,z+33,block.FLOWER_YELLOW.id)
            else:
                mc.setBlock(x-22,y,z+33,block.FLOWER_CYAN.id)
for x in range(11):
    for z in range(12):
        mc.setBlock(x-19,0,z+36,block.AIR.id)
        mc.setBlock(x-19,-1,z+36,block.GLASS.id)


#paint LIGHT

for x in range(11):
    for z in range(12):
        mc.setBlock(x-19,7,z+36,block.LAVA_STATIONARY.id)



#paint walls
for y in range(9):
    for z in range(10):
        mc.setBlock(-9,y,z+37,block.DIAMOND_BLOCK.id)
        mc.setBlock(-19,y,z+37,block.DIAMOND_BLOCK.id)
    for x in range(11):
        mc.setBlock(x-19,y,47,block.DIAMOND_BLOCK.id)
        mc.setBlock(x-19,y,36,block.DIAMOND_BLOCK.id)
for x in range(11):
    for z in range(12):
        mc.setBlock(x-19,9,z+36,block.DIAMOND_BLOCK.id)



#paint windows
for x in range(11):
    for z in range(12):
        mc.setBlock(x-19,6,z+36,block.GLASS_PANE.id)


        
#paint door
for y in range(3):
    for z in range(2):
        mc.setBlock(-19,y,z+40,block.DOOR_WOOD.id)
        mc.setBlock(-19,y,39,block.GOLD_BLOCK.id)
        mc.setBlock(-19,y,42,block.GOLD_BLOCK.id)
mc.setBlock(-19,3,40,block.GOLD_BLOCK.id)
mc.setBlock(-19,3,41,block.GOLD_BLOCK.id)

#paint heart
for x in range(2):
    for y in range(4):
        for z in range(-y,1+y):
            mc.setBlock(-14+x,11+y,z+40,block.LAPIS_LAZULI_BLOCK.id)
    mc.setBlock(-14+x,15,38,block.LAPIS_LAZULI_BLOCK.id)
    mc.setBlock(-14+x,15,39,block.LAPIS_LAZULI_BLOCK.id)
    mc.setBlock(-14+x,15,41,block.LAPIS_LAZULI_BLOCK.id)
    mc.setBlock(-14+x,15,42,block.LAPIS_LAZULI_BLOCK.id)

#paint FZ
for x in range(2):
    #paint F
    for y in range(7):
        mc.setBlock(-14+x,14+y,35,block.TNT.id)
    
    for z in range(4):
        mc.setBlock(-14+x,20,36+z,block.TNT.id)
    for z in range(3):
        mc.setBlock(-14+x,17,36+z,block.TNT.id)
    #paint Z
    for z in range(5):
        mc.setBlock(-14+x,20,45+z,block.TNT.id)
    for z in range(5):
        mc.setBlock(-14+x,14,45+z,block.TNT.id)
    for z in range(5):
        mc.setBlock(-14+x,15+z,45+z,block.TNT.id)
    
    

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-13 to -15 y=0 z=41 to 43 for 5s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x<=-13 and  pos.x>=-15 and pos.y==-0 and pos.z>=41 and pos.z<=43:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=10:
            mc.player.setTilePos(-20,10,40)
            stayed_time=0
    else:
        stayed_time=0
        
     
