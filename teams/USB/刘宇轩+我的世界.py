# Adventure 5: testLED.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program tests that you can flash an LED connected to your computer.
# This works on Raspberry Pi, PC and Mac.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports# use this for Raspberry Pi
#import anyio.GPIO as GPIO  # use this for Arduino on PC/Mac
import time
ports = list(serial.tools.list_ports.comports())

for port in ports:
    if‘Arduino’ in port[1]
        ser = serial.Serial(port = port[0], baudrate = 9600)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for i in range(10):
  mc.setBlock(pos.x + i, pos.y, pos.z, block.STONE.id)
counter = 0
while 1:
  pos_new = mc.player.getTilePos()
  if pos_new.z > pos.z and counter >= 0:
    for i in range(10):
      mc.setBlock(pos.x + i, pos.y, pos.z, block.TORCH.id)
    time.sleep(0.1)
    ser.dtr = False
    time.sleep(0.1)

    ser.write(b'L')
    counter = -1

  if pos_new.z < pos.z and counter <= 0:
    for i in range(10):
      mc.setBlock(pos.x + i, pos.y, pos.z, block.SNOW.id)

    time.sleep(0.1)
    ser.dtr = False
    time.sleep(0.1)

    ser.write(b'R')
    counter = 1


      
