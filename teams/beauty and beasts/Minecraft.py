from mcpi.minecraft import Minecraft
import time
import serial
ser=None
mc=None
def connect(com=None):
    global ser
    if com==None:
        print('请输入端口号(请注意大小写):')
        com=input()
    ser=serial.Serial(com,9600)
def control(s):
    global ser
    
    if(s>0):
        ser.write('s'.encode())
        ser.write('t'.encode())
        ser.write('+'.encode())
        mc.postToChat("+")
    if(s<0):
        ser.write('s'.encode())
        ser.write('t'.encode())
        ser.write('-'.encode())
        mc.postToChat("-")
def main():
    global mc
    mc=Minecraft.create()
    connect('COM5')
    lastPos=mc.player.getTilePos()
    while True:
        time.sleep(0.5)
        pos=mc.player.getTilePos()
        control(pos.x-lastPos.x)
main()
