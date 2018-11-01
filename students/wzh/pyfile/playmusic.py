import serial
import serial.tools.list_ports
import time
import csv

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

f=open("song.csv",'r')
songs=list(csv.reader(f))
song_dictionary={}
i=0
for song in songs:
    song_dictionary[song[0]]=song[1:]
    i+=1
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
        name=input()
        for voice in song_dictionary[name]:
            ser.write(voice.encode())
            ser.write("a".encode())
            time.sleep(0.1)

run()
