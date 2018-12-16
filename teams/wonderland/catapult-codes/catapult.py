import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)
ser = None

for p in ports:
    print(p[1])
    if "Arduino" in p[1]:
        ser = serial.Serial(port=p[0])

if ser == None:
    print("No Arduino Device was found connected to the computer")
    exit(0)

time.sleep(3)
ser.write(b'B50')
time.sleep(3)
ser.write(b'1')
time.sleep(3)
ser.write(b'2')
time.sleep(3)
ser.write(b'0')