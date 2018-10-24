
song=[['1','1','5','5','6','6','5'],['4','4','3','3','2','2','1']]
import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "USB" in p[1]:
	    ser=serial.Serial("COM9")
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)

def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        for i in song[int (action)]:
            ser.write(i.encode())
            time.sleep(2)
    ser.close()

run()
