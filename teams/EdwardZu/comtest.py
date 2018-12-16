import serial
import serial.tools.list_ports
import time
import urllib.request as request
import mcpi.minecraft as minecraft

mc=minecraft.Minecraft.create()


def isClick():
    while True:
        events=mc.events.pollBlockHits()
        for e in events:
            if e.pos.x>134 and e.pos.x<139 and e.pos.y>79 and e.pos.y<84 and e.pos.z>25 and e.pos.z<28:
                return 1
            else:
                return 0


url = "http://172.20.10.12/num/index.html"

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)


for p in ports:
    print(p[1])
    if "Arduino Uno" in p[1]:
        ser = serial.Serial(port=p[0],baudrate=9600)
    else:
        print("No Arduino Device was found connected to the computer")


def setup():
    # 等待投石机setup
    while True:
        a = ser.readline()
        b = a.decode("utf-8")
        c = "Going to loop"
        if c in b:
            break


def target():
    # 爬一下树莓派返回网站的数据，非零即有异物
    file = request.urlopen(url)
    data = file.readline().decode("utf-8")
    print("people:"+data)
    return int(data)


song = ['A', '1', '0', '0', ' ', '1', '0', '0']
cmd1 = "A 30 0 90 0 0".split(' ')
cmd2 = "A 60 0 90 0 0".split(' ')
cmd3 = "A 90 0 100 0 0".split(' ')
cmds = [cmd1, cmd2, cmd3]
print(cmds)
count = 0

while True:

    # 若未发现生物，力度归零，不发射

    time.sleep(1)
    cmd = cmds[count]

    attack = isClick()
    if attack == 1:
        cmd[4] = "1"


    people = target()
    if people == 1:
        cmd[2] = "20"
        cmd[5] = "1"

    for i in cmd:
        print(i, end=' ')
        ser.write(i.encode())
        ser.write(" ".encode())
    print('\n')

    count = count+1
    if count > 2:  # 大于等于3的时候归零
        count = 0
    a = ser.readline().decode("utf-8")
    while not ("OVER" in a):
        print(a)
        a = ser.readline().decode("utf-8")