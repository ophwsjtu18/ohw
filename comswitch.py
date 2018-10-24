<<<<<<< HEAD
import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)


while True:
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        print("got ON")
    if 'OFF' in rs:
        print("got OFF")
=======
import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)


while True:
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        print("got ON")
    if 'OFF' in rs:
        print("got OFF")
    
    
    
    
>>>>>>> 3e6eb28e676e97109cb3503df70bae1fe4f8e75b
