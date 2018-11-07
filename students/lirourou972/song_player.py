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

def run():
    f=open('song.csv','r')
    g=f.read().split('\n')
    song_list={}
    for each in g:
        tem=each.split(',')
        song_list[tem[0]]=song_list[1:]
    print(song_list)
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        if action in song_list:
            for each in song_list[action]:
                ser.write(each.encode())
                time.sleep(0.5)
        print("next song:")

run()
