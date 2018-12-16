from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
from urllib import request

mc=Minecraft.create()

while True:
        pos=mc.player.getTilePos()
        response = request.urlopen('http://192.168.199.213/cmd.html')
        page = response.read()
        page = page.decode('utf-8')
        pos=mc.player.getTilePos()
        print(page)
        time.sleep(1)
        if(page=='forward'):
            if(mc.getBlock(pos.x,pos.y,pos.z+1)==0):
                print("move forward")
                mc.postToChat("move forward")
                mc.player.setTilePos(pos.x,pos.y,pos.z+1)
        if(page=='back'):
            print("move backward")
            mc.postToChat("move backward")
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
        if(page=='left'):
            if(mc.getBlock(pos.x+1,pos.y,pos.z)==0):
                print("move left")
                mc.postToChat("move left")
                mc.player.setTilePos(pos.x+1,pos.y,pos.z)
        if(page=='right'):
            if(mc.getBlock(pos.x-1,pos.y,pos.z)==0):
                print("move right")
                mc.postToChat("move right")
                mc.player.setTilePos(pos.x-1,pos.y,pos.z)
