# rectangle maze
import random
import math
import copy
# show the maze or the path


def show_maze(maze):
    for i in maze:
        for j in i:
            if j == '0':  # wall
                print('\033[36m', j, sep='', end='\033[0m')
            elif j == 'O':  # [ entrance & exit ]& path
                print('\033[33m', j, sep='', end='\033[0m')
            elif j == 'X':  # footprint
                print('\033[31m', j, sep='', end='\033[0m')
            else:
                print(j, end='')
        print()
# build a maze which the size of maze is [ n * 10n ]


def build_maze(n):
    maze = []
    # wall
    w = '0'
    # entrance & exit
    e = 'O'
    # outer wall
    for i in range(n+2):
        if i == 0:
            maze.append([e]+[w]*(n*10+1))
        elif i == n+1:
            maze.append([w]*(n*10+1)+[e])
        else:
            maze.append([w]+[' ']*n*10+[w])
    # random inner wall
    for i in range(1, n+1):
        atan = math.atan(n)
        balance = math.floor(atan**(atan**(atan+0.5)+0.5))*n
        if i == 1:
            for j in range(balance):
                maze[i][random.randint(2, n*10-1)] = w
        elif i == n:
            for j in range(balance):
                maze[i][random.randint(1, n*10-2)] = w
        else:
            for j in range(balance):
                maze[i][random.randint(1, n*10-1)] = w
    show_maze(maze)
    return maze
# route optimization


def optimize(path):
    # anterior step, next step, posterior step
    anterior = 0
    while anterior < len(path):
        x, y = path[anterior]
        next_step = [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]
        for posterior in range(len(path)-1, anterior+1, -1):
            if path[posterior] in next_step:
                del path[anterior+1:posterior]
                break
        anterior += 1
# find the exit of the maze


def route(maze, n, option=0):
    if option == 0:
        # right down up left
        steps = ((0, 1), (1, 0), (-1, 0), (0, -1))
    elif option == 1:
        # right up down left
        steps = ((0, 1), (-1, 0), (1, 0), (0, -1))
    else:
        # left up down right
        steps = ((0, -1), (-1, 0), (1, 0), (0, 1))
    # the way out of maze
    path = [(1, 1)]
    # never again
    footprint = []
    # entrance
    x = y = 1
    while x != n or y != n*10:
        # horizontal vertical
        for h, v in steps:
            if maze[x+h][y+v] == ' ' and (x+h, y+v) not in footprint:
                path.append((x+h, y+v))
                footprint.append((x+h, y+v))
                break
        else:
            if path:
                path.pop()
            else:
                # There is no escape. show the maze and footprint
                for x, y in footprint:
                    maze[x][y] = 'X'
                show_maze(maze)
                break
        # location
        if path:
            x, y = path[-1]
    else:
        # show the maze, footprint and path
        for x, y in footprint:
            maze[x][y] = 'X'
        # optimize the path of maze
        optimize(path)
        for x, y in path:
            maze[x][y] = 'O'
        show_maze(maze)


# play
while True:
    n = input('the size of maze: ')
    if n.isdigit() and n != '0':
        n = int(n)
        maze0 = build_maze(n)
        maze1 = copy.deepcopy(maze0)
        maze2 = copy.deepcopy(maze0)
        input('Press any key to continue.')
        route(maze0, n)
        input('Press any key to continue.')
        route(maze1, n, 1)
        input('Press any key to continue.')
        route(maze2, n, 2)
    else:
        n = 19
        maze0 = build_maze(n)
        maze1 = copy.deepcopy(maze0)
        maze2 = copy.deepcopy(maze0)
        input('Press any key to continue.')
        route(maze0, n)
        input('Press any key to continue.')
        route(maze1, n, 1)
        input('Press any key to continue.')
        route(maze2, n, 2)

