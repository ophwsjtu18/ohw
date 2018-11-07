from mcpi.minecraft import Minecraft
import time
import my_song_player

#initialize the global variables and constant parameters

home_position = [86,22,111]


def fly_sing_loop(mc):
    count_fly = 0
    stayed_time = 0
    song_dict = my_song_player.get_songs()
    ser = my_song_player.test_com()
    # endless loop
    while True:
        print("stay_time"+str(stayed_time))
        time.sleep(0.5)
        pos=mc.player.getTilePos()
        mc.postToChat("please go to home x=86 y=22 z=111 for 15s to fly")
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

        if pos.x==home_position[0] and pos.y==home_position[1] and pos.z==home_position[2]:
            mc.postToChat("welcome home")
            stayed_time = stayed_time + 1
            if stayed_time==16:
                # fly above
                mc.player.setTilePos(home_position[0],home_position[1]+30,home_position[2])
                stayed_time = 0
                # play a song
                song_name, song_content = list(song_dict.items())[count_fly%3]
                my_song_player.play_single_song(ser, song_name, song_content)
                count_fly = count_fly + 1
                # get back to home from the sky
                mc.player.setTilePos(home_position[0],home_position[1],home_position[2])
        else:
            stayed_time=0


def main():
    mc=Minecraft.create()
    # set the start position at home
    mc.player.setTilePos(home_position[0],home_position[1],home_position[2])
    fly_sing_loop(mc)

if __name__ == '__main__':
    main()