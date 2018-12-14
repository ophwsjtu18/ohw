import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import csv

num_rows = int(input("Rows: "))  # number of rows
num_cols = int(input("Columns: "))  # number of columns

# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
M = np.zeros((num_rows, num_cols, 5), dtype=np.uint8)

# The array image is going to be the output image to display
image = np.zeros((num_rows*10, num_cols*10), dtype=np.uint8)

# Set starting row and column
r = 0
c = 0
history = [(r, c)]  # The history is the stack of visited locations

# Trace a path though the cells of the maze and open walls along the path.
# We do this with a while loop, repeating the loop until there is no history,
# which would mean we backtracked to the initial start.
while history:
    M[r, c, 4] = 1  # designate this location as visited
    # check if the adjacent cells are valid for moving to
    check = []
    if c > 0 and M[r, c-1, 4] == 0:
        check.append('L')
    #对于当前位置M[r, c, 4]即(r-1, c-1)，如果他左边的一列的点的状态为0，（not visited）
    #则在检查check[]中添加左侧可以进行搜寻的信息'L'
    #下面的同理
    if r > 0 and M[r-1, c, 4] == 0:
        check.append('U')
    #原点设置为左上方
    if c < num_cols-1 and M[r, c+1, 4] == 0:
        check.append('R')
    if r < num_rows-1 and M[r+1, c, 4] == 0:
        check.append('D')
    #print(check)

    if len(check):  # If there is a valid cell to move to.
        #check不为空，则证明还有地方没有被走到
        # Mark the walls between cells as open if we move
        history.append([r, c])
        #储存走过的点的位置坐标
        move_direction = random.choice(check)
        #从还未走到的位置（check中保存）中任选一个作为下次行进的位置
        #后来因为初始点在左上，所以基本上都是往右下走
        if move_direction == 'L':
            M[r, c, 0] = 1 #记录轨迹，我从M[r, c, 0]的位置向左走了，0代表单位数第一位
            c = c-1 #相应的作为左边的点，就向右可以走，记录在此点可以向右的信息
            M[r, c, 2] = 1
            #剩余同理
        if move_direction == 'U':
            M[r, c, 1] = 1
            r = r-1
            M[r, c, 3] = 1
        if move_direction == 'R':
            M[r, c, 2] = 1
            c = c+1
            #加以减一来进行循环中的遍历
            M[r, c, 0] = 1
        if move_direction == 'D':
            M[r, c, 3] = 1
            r = r+1
            M[r, c, 1] = 1
    else:  # If there are no valid cells to move to.
        # retrace one step back in history if no move is possible
        r, c = history.pop()
        #如果前后左右都不能走，那就把这个点删掉，回退到上一步，继续进行四个方向的选择（防止死胡同）


# Open the walls at the start and finish
M[0, 0, 0] = 1 #原点在左上角，所以左上角不能向左走，设为初始点
M[num_rows-1, num_cols-1, 2] = 1 #右下角同理不能向右。设为结束点

# Generate the image for display
def show_maze():
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            cell_data = M[row, col] 
            #先行row 后列col
            #与正常的print输出顺序相同
            #print(cell_data)
            for i in range(10*row+2, 10*row+8):
                image[i, range(10*col+2, 10*col+8)] = 255
                #除了出入口的边界都画为黑的
            if cell_data[0] == 1:
                image[range(10*row+2, 10*row+8), 10*col] = 255
                image[range(10*row+2, 10*row+8), 10*col+1] = 255
            if cell_data[1] == 1:
                image[10*row, range(10*col+2, 10*col+8)] = 255
                image[10*row+1, range(10*col+2, 10*col+8)] = 255
            if cell_data[2] == 1:
                image[range(10*row+2, 10*row+8), 10*col+9] = 255
                image[range(10*row+2, 10*row+8), 10*col+8] = 255
            if cell_data[3] == 1:
                image[10*row+9, range(10*col+2, 10*col+8)] = 255
                image[10*row+8, range(10*col+2, 10*col+8)] = 255
    # Display the image
    plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
    plt.show()

#print(check)

'''
print(M)

with open('maze.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(M)
'''
show_maze()