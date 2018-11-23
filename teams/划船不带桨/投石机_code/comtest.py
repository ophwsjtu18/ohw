import serial
import serial.tools.list_ports
import time

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)


for p in ports:
    print(p[1])
    if "Arduino Uno" in p[1]:
        ser = serial.Serial(port=p[0], baudrate=9600)
    else:
        print("No Arduino Device was found connected to the computer")

time.sleep(5)
'''
song = ['A', '1', '0', '0', ' ', '1', '0', '0']
cmd1 = "A 0 0 120 0 0"
# jd aarm shotting jd是底座转动的角度，aarm相当于投臂的角度，shooting大于90为释放
cmd2 = "A 90 0 120 0 0"
cmd3 = "A 150 180 20 0 0"
cmds = [cmd1, cmd2, cmd3]

count = 0


while True:
    cmd = cmds[count]
    ser.write(cmd.encode())
    print(cmd)
    time.sleep(10)
    count = count+1
    if count > 2:  # 大于等于3的时候归零
        count = 0
'''

# Only for shooting
while True:
    base_angle = input("Base angle(0 ~ 180): ")
    arm_angle = input("Arm angle(0-maximum ~ 60-minimum): ")
    shoot_cmd = "A " + base_angle + " " + arm_angle + " 120 0 0 "
    ser.write(shoot_cmd.encode())
    print(shoot_cmd)
    print("Waiting for execution......")
    time.sleep(20)






