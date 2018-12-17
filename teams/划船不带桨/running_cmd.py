from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import serial
import serial.tools.list_ports
from urllib import request


def get_cmd_info(ip="192.168.199.213"):
    response = request.urlopen("http://" + ip + "/cmd.html")
    page = response.read()
    page = page.decode('utf-8')
    print(page)
    pos_cmd = page.split(',')[0]
    raw_angle = page.split(',')[1]
    return pos_cmd, raw_angle


def maze_game(mc, period=60):
    start = time.time()
    while True:
        pos_cmd, _ = get_cmd_info()
        pos = mc.player.getTilePos()
        time.sleep(1)
        if (time.time() - start) > period:
            break
        if pos_cmd == 'forward':
            if mc.getBlock(pos.x, pos.y, pos.z + 1) == 0:
                print("move forward")
                mc.postToChat("move forward")
                mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        elif pos_cmd == 'back':
            print("move backward")
            mc.postToChat("move backward")
            mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
        elif pos_cmd == 'left':
            if mc.getBlock(pos.x + 1, pos.y, pos.z) == 0:
                print("move left")
                mc.postToChat("move left")
                mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
        elif pos_cmd == 'right':
            if mc.getBlock(pos.x - 1, pos.y, pos.z) == 0:
                print("move right")
                mc.postToChat("move right")
                mc.player.setTilePos(pos.x - 1, pos.y, pos.z)


def catapult_shoot(ser):
    _, raw_angle = get_cmd_info()
    if raw_angle > 0:
        base_angle = str(raw_angle / 6)
        arm_angle = '20'
        shoot_cmd = "A " + base_angle + " " + arm_angle + " 120 0 0 "
        ser.write(shoot_cmd.encode())
        print(shoot_cmd)
        print("Waiting for execution......")
        time.sleep(20)
    else:
        print("No people found")


def check_points_per_step(mc):
    # check get or lose points every single step.
    # change block id here!
    good_id = 35
    bad_id = 1
    normal_id = 2
    pos = mc.player.getTilePos()
    point_per_step = 0
    if mc.getBlock(pos.x, pos.y-1, pos.z) == good_id:
        point_per_step = +20
    elif mc.getBlock(pos.x, pos.y-1, pos.z) == bad_id:
        point_per_step = -10
    elif mc.getBlock(pos.x, pos.y-1, pos.z) == normal_id:
        point_per_step = 5
    return point_per_step


def running_game(mc):
    start = time.time()
    points = 0
    while True:
        pos_cmd, _ = get_cmd_info()
        pos = mc.player.getTilePos()
        points = points + check_points_per_step(mc)
        time.sleep(0.5)
        mc.postToChat("keep moving forward")
        duration = time.time() - start
        if mc.getBlock(pos.x, pos.y-1, pos.z) == block.GLASS.id:
            comments = "Finish! you have got " + str(points) + " points in " + str(duration[:5]) + " seconds. GOOD JOB!"
            print(comments)
            mc.postToChat(comments)
            break
        else:
            comments = "you have got " + str(points) + " points in " + str(duration[:5]) + " seconds."
            print(comments)
            mc.postToChat(comments)
        if mc.getBlock(pos.x, pos.y, pos.z + 1) == 0:
            mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        if pos_cmd == 'left':
            if mc.getBlock(pos.x + 1, pos.y, pos.z) == 0:
                print("move left")
                mc.postToChat("move left")
                mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
        elif pos_cmd == 'right':
            if mc.getBlock(pos.x - 1, pos.y, pos.z) == 0:
                print("move right")
                mc.postToChat("move right")
                mc.player.setTilePos(pos.x - 1, pos.y, pos.z)


def main():
    mc = Minecraft.create()
    ports = list(serial.tools.list_ports.comports())
    print(ports)
    for p in ports:
        print(p[1])
        if "Arduino Uno" in p[1]:
            ser = serial.Serial(port=p[0], baudrate=9600)
        else:
            print("No Arduino Device was found connected to the computer")
    while True:
        instruct = input("a: Game in my world  b: Shoot a stone  q: quit")
        if instruct == 'a':
            home = [55, 51, 51]
            run_pos = [91, 13, 524]
            run_button = [53, 52, 57]
            maze_pos = []
            maze_button = [57, 52, 57]

            mc.player.setTilePos(home[0], home[1], home[2])
            if mc.getBlock(run_button[0], run_button[1], run_button[2]) == 41:
                mc.player.setTilePos(run_pos[0], run_pos[2], run_pos[3])
                running_game(mc)


        elif instruct == 'b':
            catapult_shoot(ser=ser)
        elif instruct == 'q':
            break


main()
