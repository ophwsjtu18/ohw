import serial
import serial.tools.list_ports
import time
import csv

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "USB-SERIAL" or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)
p = open("songs.csv",'r').read()
song=[]
g=p.split('\n')
for i in g:
    song.append(i.split(','))
def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        for i in song:
            for a in i:
                ser.write(a.encode())
                ser.write('a'.encode())
                time.sleep(0.125)
    ser.close()

run()
