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
def run():
    f = open('songs.csv', 'r')
    songs = f.read().split('\n')
    song_lst = [song.split(',') for song in songs]
    #song_dict = [song[0]:song[1:] for song in song_lst]
    print(song_lst)
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        for song in song_lst:
            if action == song[0]:
                for i in song:
                    i = i + 'a'
                    ser.write(i.encode())
                    time.sleep(0.25)

run()
