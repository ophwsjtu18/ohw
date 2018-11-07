from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time


def saysong(choice):
    choice = str(choice)
    ser=serial.Serial(port='COM4')
    time.sleep(2)
    f = open("tenyear.csv","r")
    data = f.read()
    data_line = data.split("\n")
    data_dir = {}

    for line in data_line:
        line = line.split(',')
        data_dir[line[0]] = line[1:len(line)+1]

    print(data_dir)
    #choice = input("song name:")
    s = 'q'
    datas = data_dir[choice]
    print(datas)
    for num in datas:
        ser.write(num.encode())
        ser.write(s.encode())
        time.sleep(0.25)


print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

mc=Minecraft.create()

stayed_time=0
choice = 0

while True:
    choice = choice + 1
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=45 y=23 z=109 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==45 and pos.y==23 and pos.z==109:
        stayed_time=stayed_time+1
        if stayed_time>=4:
            stayed_time=0
            mc.player.setTilePos(45,30,109)
            saysong(choice%3)
            
    else:
        stayed_time=0
