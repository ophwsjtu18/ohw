import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
            ser=serial.Serial(port=p[0])
    else :
            print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

def media_play():
        f = open('songs.txt','r').read()
        all_songs = f.split('\n')
        songs = {}
        for a in all_songs[:-1]:
                songs[a.split(' ')[0]] = a.split(' ')[1].split(',')

        action = "empty"
        while action != 'q':
                print("welcome to hyh's player, press q to quit")
                action = input("> ")
                if action in songs:
                        for b in songs[action]:
                                print(b)
                                ser.write(b.encode())
                                time.sleep(1) 
                time.sleep(5)
                print("next")
media_play()
                                
        



       





