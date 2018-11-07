import serial
import serial.tools.list_ports
import time
from mcpi.minecraft import Minecraft

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)

for p in ports:
    print(p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser = serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")

# ser=serial.Serial(port='COM4')
# ser=serial.Serial(port='/dev/ttymodem542')
# wait 2 seconds for arduino board restart
time.sleep(2)

music = [
    [1, 1, 5, 5, 6, 6, 5],
    [1, 2, 3, 1, 1, 2, 3, 1, 3, 4, 5, 5, 3, 4, 5, 5],
    [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
]

mc = Minecraft.create()

stayed_time = 0

count = 0

while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()
    mc.postToChat("please goto home for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if -11 <= pos.x <= -9 and -1 <= pos.z <= 1:
        mc.postToChat("welcome home")
        stayed_time = stayed_time+1
        if stayed_time >= 3:
            mc.player.setTilePos(pos.x, pos.y+10, pos.z)
            stayed_time = 0
            for note in music[count % 3]:
                ser.write((str(note) + 'a').encode())
                time.sleep(0.25)
                ser.write(('0a').encode())
                time.sleep(0.1)
            count += 1

    else:
        stayed_time = 0
        mc.postToChat("%s, %s, %s" % (pos.x, pos.y, pos.z))
