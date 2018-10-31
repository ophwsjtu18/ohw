from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
import time
import csv

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

f=open("song.csv",'r')
songs=list(csv.reader(f))
song_dictionary={}
i=0
for song in songs:
    song_dictionary[song[0]]=song[1:]
    i+=1
for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        for voice in song_dictionary["aaa"]:
            ser.write(voice.encode())
            print(voice)
            ser.write("a".encode())
            time.sleep(0.1)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
            run()
    else:
        stayed_time=0
        


