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
    f = open('music.csv','r')
    music = f.read().split('\n')
    dic = {}
    dic['liangzhilaohu'] = music[0]
    dic['twinkle star'] = music[1]
    dic['huanlesong'] = music[2]
    while(True):
        instruction = input('>')
        music_line = dic[instruction].split(',')
        for action in music_line:
            ser.write((action+'a').encode())
            time.sleep(0.25)

run()
