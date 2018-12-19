from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import serial
import serial.tools.list_ports
from urllib import request

def build_maze():
    mc = Minecraft.create()
    pos = mc.player.getTilePos()

    GAP = block.AIR.id
    WALL = block.GOLD_BLOCK.id
    FLOOR = block.GRASS.id

    origin_x = 92
    origin_y = 4
    origin_z = 839

    z = origin_z

    f = open('maze.csv', 'r')
    for line in f.readlines():
        data = line.split(',')
        #print(data)
        x = origin_x
        for cell in data:
            #print(cell)
            if cell == " " or cell == '+':
                b = GAP
            else:
                b = WALL
            for i in range(2):
                for j in range(2):
                    mc.setBlock(x + i, origin_y, z + j, b)
                    mc.setBlock(x + i, origin_y + 1, z + j, b)
                    mc.setBlock(x + i, origin_y - 1, z + j, FLOOR)

            x = x + 2
        z = z + 2

def get_cmd_info(ip="192.168.43.162"):
    response = request.urlopen("http://" + ip + "/cmd.html")
    page = response.read()
    page = page.decode('utf-8')
    print(page)
    pos_cmd = page.split(',')[0]
    raw_angle = page.split(',')[1]
    return pos_cmd, raw_angle


def maze_game(mc, period=60):
    print("GameStart")
    start = time.time()
    while True:
        pos_cmd, _ = get_cmd_info()
        pos = mc.player.getTilePos()
        time.sleep(1)
        if mc.getBlock(pos.x, pos.y-1, pos.z) == block.GLASS.id:
            for i in range(100):
                mc.postToChat("ntql")
            break
        if (time.time() - start) > period:
            mc.postToChat("Time is up")
            break
        if pos_cmd == 'forward':
            if mc.getBlock(pos.x, pos.y, pos.z + 1) == 0:
                print("move forward")
                mc.postToChat("move forward")
                mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
        elif pos_cmd == 'back':
            if mc.getBlock(pos.x, pos.y, pos.z - 1) == 0:
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
    if float(raw_angle) > 0:
        base_angle = str(150-float(raw_angle) / 3)
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
    bad_id = 41
    normal_id = 42
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
        time.sleep(0.8)
        mc.postToChat("keep moving forward")
        duration = time.time() - start
        if mc.getBlock(pos.x, pos.y-1, pos.z) == block.GLASS.id:
            comments = "Finish! you have got " + str(points) + " points in " + str(duration)[:5] + " seconds. GOOD JOB!"
            print(comments)
            mc.postToChat(comments)
            break
        else:
            comments = "you have got " + str(points) + " points in " + str(duration)[:5] + " seconds."
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
            home = [55, 52, 51]
            run_pos = [91, 13, 524]
            run_button = [53, 52, 57]
            maze_pos = [95, 6, 838]
            maze_button = [57, 52, 57]

            mc.player.setTilePos(home[0], home[1], home[2])
            while True:
                if mc.getBlock(run_button[0], run_button[1], run_button[2]) == 41:
                    mc.player.setTilePos(run_pos[0], run_pos[1], run_pos[2])
                    running_game(mc)
                    break
                if mc.getBlock(maze_button[0], maze_button[1], maze_button[2]) == 41:
                    mc.player.setTilePos(maze_pos[0], maze_pos[1], maze_pos[2])
                    maze_game(mc,120)
                    break


        elif instruct == 'b':
            catapult_shoot(ser=ser)
        elif instruct == 'q':
            break


main()
