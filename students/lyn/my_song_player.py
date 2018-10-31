import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)
def song_player():
    song = open('songs.csv', 'r')
    songs = song.read().split('\n')
    song_lst = [song.split(',') for each_song in songs]
    print(song_lst)
    for each_song in song_lst:
        print(song_lst.index(seach_ong))
        for temp in each_song:
            ser.write(temp.encode())
            time.sleep(1)
        time.sleep(5)
        print('next song')


song_player()
