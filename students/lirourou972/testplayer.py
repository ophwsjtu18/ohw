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
    song_list=[]
    a='a'
    for each in k:
        tem=each.split('r')
        song_list.append(tem[1:])
    for each in song_list:
        ser.write(each.encode())
        ser.write('a'.encode())
        time.sleep(0.5)


run()


        
