import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time
import requests, json
import random
class Character():
    def __init__(self):
        self.mc = minecraft.Minecraft.create()
        

    def create_character(self, character_position, head_material=2, body_material=1, arm_material=3,
    leg_material=4):
        x = character_position[0]
        y = character_position[1]
        z = character_position[2]
        
        #建造头部
        self.mc.setBlock(x,y+2,z,head_material)
        #建造身体
        for i in range(2):
            for j in range (-1,2):
                self.mc.setBlock(x+j,y+i,z,body_material)
        #建造手臂
        self.mc.setBlock(x-2,y,z,arm_material)
        self.mc.setBlock(x-2,y+1,z,arm_material)
        self.mc.setBlock(x+2,y,z,arm_material)
        self.mc.setBlock(x+2,y+1,z,arm_material)

        #建造腿
        self.mc.setBlock(x-1,y-1,z,leg_material)
        self.mc.setBlock(x-1,y-2,z,leg_material)
        self.mc.setBlock(x-1,y-3,z,leg_material)
        self.mc.setBlock(x+1,y-1,z,leg_material)
        self.mc.setBlock(x+1,y-2,z,leg_material)
        self.mc.setBlock(x+1,y-3,z,leg_material)

        time.sleep(0.5)
        #print("已建造！")

    def clear_character(self, former_position):
        self.create_character(former_position, 0, 0, 0, 0)
        #print("已消除!")

    def flash_character(self, character_position, former_position, head_material=2, body_material=1, arm_material=3,
    leg_material=4):
        self.create_character(character_position, head_material, body_material, arm_material,
    leg_material)
        self.clear_character(former_position)

    
    def walk_direction(self, character_position, target_position):
        direction = [target_position[0]-character_position[0],
        target_position[1]-character_position[1],
        target_position[2]-character_position[2]]

        #由于我的世界里面方块坐标好像只能是整数，用方向向量的方法好像不大行。。。但我也舍不得删
        ##distance = math.sqrt(direction[0]*direction[0]+direction[1]*direction[1]+
        ##direction[2]*direction[2])

        ##direction_init = [direction[i]/distance for i in range(3)]
        ##return direction_init
        return direction

    def walk(self, walk_direction, character_position, character_speed):
        if walk_direction[0] != 0:
            stepx = character_speed * walk_direction[0] / abs(walk_direction[0])
            character_position[0] += stepx

        if walk_direction[1] != 0:
            stepy = character_speed * walk_direction[1] / abs(walk_direction[1])
            character_position[1] += stepy

        if walk_direction[2] != 0:
            stepz = character_speed * walk_direction[2] / abs(walk_direction[2])
            character_position[2] += stepz
        

        return character_position


def elect(x0,y0,z0,S):
    for i in range(15):
        for j in range(2):
            for t in range(15):
                mc.setBlock(x0+i,y0+j,z0+t,S)
    for i in range(9):
        for j in range(2):
            for t in range(9):
                mc.setBlock(x0+i+3,y0+j+2,z0+t+3,S)
    for i in range(5):
        for j in range(6):
            for t in range(5):
                mc.setBlock(x0+5+i,y0+4+j,z0+5+t,S)
    for j in range(6):
        mc.setBlock(x0+6,y0+9+j,z0+6,S)
        mc.setBlock(x0+6,y0+9+j,z0+8,S)
        mc.setBlock(x0+8,y0+9+j,z0+6,S)
        mc.setBlock(x0+8,y0+9+j,z0+8,S)
    for j in range(5):
        for i in range(3):
            for t in range(3):
                mc.setBlock(x0+6+i,y0+14+j,z0+6+t,S)
    for j in range(12):
        mc.setBlock(x0+7,y0+16+j,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-20+t,y0+16+7-t,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-14+t,y0+16+t+1,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-8+t,y0+16+7-t,z0+7,S)
    for t in range(7):
        mc.setBlock(x0-2+t,y0+16+t+1,z0+7,S)
    for t in range(12):
        mc.setBlock(x0+16,y0+17+t,z0+7,S)
    for t in range(9):
        mc.setBlock(x0+16+t,y0+17,z0+7,S)

former=0
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
while True:
    r = requests.get('http://172.20.10.2:9000/')
    data = json.loads(r.content)
    number=0
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    if 'person' in data:
        number=len(data['person'])
        print(data['person'])
        print(len(data['person']))
        List=[]
        character_position=[]
        target_position=[]
        former_position=[]
        for i in range(number):
            List.append(Character())
        #character = Character()
        for i in range(number):
            character_position.append([pos.x+4*(i+1),pos.y+3,pos.z+2])
            former_position.append([pos.x+4*(i+1),pos.y+3,pos.z+2])
            target_position.append([pos.x+8+4*i,pos.y+10,pos.z+19])
        character_speed = 1
        isWalking=True
        while(character_position[0] != target_position[0]):
            for i in range(number):
                former_position[i]=character_position[i]
                walk_direction=List[i].walk_direction(character_position[i],target_position[i])
                character_position[i]=List[i].walk(walk_direction,character_position[i],character_speed)
                List[i].flash_character(character_position[i],former_position[i])
        time.sleep(0.5)
    else:
        print('No person found.')
    if(number<former):
        for i in range(former-number):
            elect(pos.x+20*(random.randint(0,3)+1),pos.y-10,pos.z+20*(random.randint(0,3)+1),41)
    former=number
    time.sleep(1)
