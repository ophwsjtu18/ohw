import serial
import serial.tools.list_ports
from urllib import request
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1] or "Uno" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM3')
#Arduino/Genuino Uno
#wait 2 seconds for arduino board restart
time.sleep(2)
while(True):
	f = request.urlopen("http://192.168.137.229/data.html")
	data = f.read()
	data = data.decode('utf-8')
	data = data.split('\n')
	angle = int(50*float(data[0]))
	print("x: "+str(float(data[0])))
	print("y: "+str(float(data[1])))

	action = "A "+str(angle)+" "+"60"
	ser.write(action.encode())

	time.sleep(5)
