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

f = open("songs.txt",'r').read().split('\n')
songs = {}
for i in f[:-1]:
    songs[i.split(' ')[0]] = i.split(' ')[1].split(',')

def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        if action in songs:
            for i in songs[action]:
                ser.write(int(i))
                time.sleep(1)
        time.sleep(1)

run()
    
