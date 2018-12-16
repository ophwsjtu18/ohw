from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
from urllib import request


mc=Minecraft.create()
ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    print(p[1])
    if "Arduino Uno" in p[1]:
        ser = serial.Serial(port=p[0], baudrate=9600)
    else:
        print("No Arduino Device was found connected to the computer")

while True:
    instruct = input("a: controlled by camera.  b: shoot a stone")
    if instruct == 'a':
        start = time.time()
        while True:
            pos=mc.player.getTilePos()
            response = request.urlopen('http://192.168.199.213/cmd.html')
            page = response.read()
            page = page.decode('utf-8')
            pos=mc.player.getTilePos()
            print(page)
            pos_cmd = page.split(',')[0]
            time.sleep(1)
            if (time.time()-start) > 60:
                break
            if(pos_cmd=='forward'):
                if(mc.getBlock(pos.x,pos.y,pos.z+1)==0):
                    print("move forward")
                    mc.postToChat("move forward")
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            elif(pos_cmd=='back'):
                print("move backward")
                mc.postToChat("move backward")
                mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            elif(pos_cmd=='left'):
                if(mc.getBlock(pos.x+1,pos.y,pos.z)==0):
                    print("move left")
                    mc.postToChat("move left")
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            elif(pos_cmd=='right'):
                if(mc.getBlock(pos.x-1,pos.y,pos.z)==0):
                    print("move right")
                    mc.postToChat("move right")
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
    elif instruct == 'b':
        response = request.urlopen('http://192.168.199.213/cmd.html')
        page = response.read()
        page = page.decode('utf-8')
        raw_angle = page.split(',')[1]
        base_angle = str(float(raw_angle)/6)
        arm_angle = '20'
        shoot_cmd = "A " + base_angle + " " + arm_angle + " 120 0 0 "
        ser.write(shoot_cmd.encode())
        print(shoot_cmd)
        print("Waiting for execution......")
        time.sleep(20)
