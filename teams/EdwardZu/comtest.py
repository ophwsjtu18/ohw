import serial
import serial.tools.list_ports
import time

#def recv(serial):
#   while True:
#        data = serial.read_all()
#        if data == '':
#            continue
#        else:
#            break
#        time.sleep(0.02)
#    return data


print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)


for p in ports:
    print(p[1])
    if "Arduino Uno" in p[1]:
        ser = serial.Serial(port=p[0],baudrate=9600)
    else:
        print("No Arduino Device was found connected to the computer")

while True:
    a = ser.readline()
    b = a.decode("utf-8")
    c = "Going to loop"
   # print(type(b), type(c))
    if  c in b:
        break

song = ['A', '1', '0', '0', ' ', '1', '0', '0']
cmd1 = "A 30 20 90 0 0".split(' ')
cmd2 = "A 60 20 90 0 0".split(' ')
cmd3 = "A 90 20 100 0 0".split(' ')
cmds = [cmd1, cmd2, cmd3]
print(cmds)
count = 0

while True:
    cmd = cmds[count]
    for i in cmd:
        print(i, end=' ')
        ser.write(i.encode())
        ser.write(" ".encode())
    print ('\n')

    count = count+1
    if count > 2:  # 大于等于3的时候归零
       count = 0
    a = ser.readline().decode("utf-8")
    while not ("OVER" in a):
        print(a)
        a = ser.readline().decode("utf-8")