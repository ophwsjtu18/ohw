import create_maze as create
import maze #在当前位置造一个迷宫

print('请输入方阵迷宫大小')
size = int(input()) - 2 #去掉一周的墙壁厚度2
create.route(size) #根据输入的行列随机生成一个迷宫和推荐路线
#0为墙，其余为可以行走的路线，并且'+'代表了推荐路线
maze.build_maze() #建造迷宫