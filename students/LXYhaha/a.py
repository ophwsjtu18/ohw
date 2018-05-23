from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

mc=Minecraft.create()

pos0=mc.player.getTilePos()

mc.postToChat("move left to turn left, move right to turn right'\n'jump to fire")

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
#ser=serial.Serial(port='COM4')

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    

    if pos.x<pos0.x:
        angle = abs(pos.x - pos0.x)*5
        mc.postToChat("at left and turn angle is")
        mc.postToChat(angle)
        ser.write('41'.encode())

    if pos.x>pos0.x:
        angle = abs(pos.x - pos0.x)*5
        mc.postToChat("at right and turn angle is")
        mc.postToChat(angle)

    if pos.y>pos0.y:
        mc.postToChat("fire")
    



