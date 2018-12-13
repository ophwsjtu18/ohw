#这个类实现了
#1.人物的创建，可以定义人物初始的位置以及人物的头、身体、手臂和腿的材质，通过函数 create_character 实现
#2.人物的移动，可以实现从人物当前的位置到指定位置，通过函数 walk_direction（确定方向）、walk（）、flash_character 实现


import mcpi.minecraft as minecraft
import mcpi.block as block
import math

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

        print("已建造！")

    def clear_character(self, former_position):
        self.create_character(former_position, 0, 0, 0, 0)
        print("已消除!")

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


#以下是调试用的代码
character1 = Character()
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


#这一段是写在主程序里面，用来控制人前进,里面的变量应该根据实际改进
character_position = [pos.x+2,pos.y+3,pos.z+2]
target_position = [pos.x+8,pos.y+10,pos.z+19]
character_speed = 1
isWalking=True
while(character_position != target_position):
    former_position = character_position
    walk_direction = character1.walk_direction(character_position, target_position)
    #原来的代码 可能会有用
    #character_position = [int((character_position[i] + character_speed*walk_direction[i])) for i in range(3)]
    character_position = character1.walk(walk_direction, character_position, character_speed)
    character1.flash_character(character_position, former_position)


character1.create_character(character_position)
    
    

        




        

        
        


