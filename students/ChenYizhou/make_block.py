import mcpi.minecraft as minecraft
import mcpi.block as block

def build_house(mc,x,y,z,w,h):

    for i in range(w):
        # floor and ceiling
        for j in range(w):
            mc.setBlock(x+i, y, z+j, block.COBBLESTONE.id)
            mc.setBlock(x+i, y+h, z+j, block.GRASS.id)
        # walls
        for k in range(h):
            mc.setBlock(x+i,y+k,z,89)
            mc.setBlock(x+i,y+k,z+w-1,89)
            mc.setBlock(x,y+k,z+i,89)
            mc.setBlock(x+w-1,y+k,z+i,89)
    # windows
    window_length = 4
    window_margin = (int(w/2)-window_length/2, int(h/2)-window_length/2)
    for m in range(window_length):
        for n in range(window_length):
            mc.setBlock(x+window_margin[0]+m, y+window_margin[1]+n, z, block.GLASS.id)
            mc.setBlock(x+window_margin[0]+m, y+window_margin[1]+n, z+w-1, block.GLASS.id)
            mc.setBlock(x, y+window_margin[1]+n, z+window_margin[0]+m, block.GLASS.id)
    # door
    door_length = 3
    door_height = 4
    for a in range(door_height):
        for b in range(door_length):
            mc.setBlock(x+w-1, y+1+a, z+int(w/2)+b, 0)

def main():
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    # mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)
    build_house(mc,pos.x,pos.y,pos.z,10,10)

if __name__ == '__main__':
    main()
