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
    f=open('song.txt','r')
    g=f.read()
    k=g.split('\n')
    song_list={}
    for each in k:
        tem=each.split(',')
        song_list[tem[0]]=tem
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        print(action)
        if action in song_list:
            rym=song_list[action][1:]
            for a in rym:
                ser.write(a.encode())
                ser.write('a'.encode())
                time.sleep(0.5)


run()
