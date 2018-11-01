from mcpi.minecraft import Minecraft
import time
import my_song_player

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
home_position = [20,30,40]
mc.player.setTilePos(home_position[0],home_position[1],home_position[2])
while True:

    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=20 y=30 z=40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    if pos.x==home_position[0] and pos.y==home_position[1] and pos.z==home_position[2]:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time==15:
            mc.player.setTilePos(home_position[0],home_position[1]+15,home_position[2])
            time.sleep(5)
            ser = my_song_player.test_com()
            my_song_player.song_player(ser)
            mc.player.setTilePos(home_position[0],home_position[1]-15,home_position[2])
        if stayed_time>=30:
            mc.player.setTilePos(home_position[0],home_position[1],home_position[2])
            stayed_time=0
    else:
        stayed_time=0
