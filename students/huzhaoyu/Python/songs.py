import serial
import serial.tools.list_ports
import time
import csv

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

f = open("12345.csv",'r')
songs = list(csv.reader(f))
songs_dictory={}
song_num = 0 
for song in songs:
    songs_dictory[song[0]]=song_num
    song_num = song_num + 1
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

def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        input_name = input()
        for voise in songs[songs_dictory[input_name]]:
            ser.write(voise.encode())
            ser.write('a'.encode())
            time.sleep(0.25)

run()
