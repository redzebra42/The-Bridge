import sys
import math
import copy


m = 2 # the amount of motorbikes to control
v = 1  # the minimum amount of motorbikes that must survive
l0 = '...0......'  # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
l1 = '...00.....'
l2 = '...0..0...'
l3 = '...0......'

bridge = []
for str_line in [l0, l1, l2, l3]:
    line = []
    for char in str_line:
        if char == '.':
            line.append(0)
        elif char == '0':
            line.append(1)
        else:
            raise RuntimeError
    bridge.append(line)

def can_up(moto_list):
    for moto in moto_list:
        if moto[x] == 0:
            return False
    return True

def can_down(moto_list):
    for moto in moto_list:
        if moto[x] == 3:
            return False
    return True

def dies(moto, speed, action):
    x, y = moto['x'], moto['y']
    if action == 'SPEED':
        return 1 in bridge[moto[y]][x+1:x+speed+2]
    elif action == 'SLOW':
        return 1 in bridge[moto[y]][x+1:x+speed]
    elif action == 'JUMP':
        return 1 == bridge[moto[y]][x+speed]
    elif action == 'WAIT':
        return 1 in bridge[moto[y]][x+1:x+speed+1]
    elif action == 'UP':  #assuming the moto can go up
        return (1 in bridge[moto[y]][x+1:x+speed] or 1 in bridge[moto[y+1]][x+1:x+speed+1])
    elif action == 'DOWN':  #assuming the moto can go down
        return (1 in bridge[moto[y]][x+1:x+speed] or 1 in bridge[moto[y-1]][x+1:x+speed+1])
    else:
        raise RuntimeError

def nb_tiles_before_hole(moto):
    '''returns the number of tile before the next hole, and the size of the next hole'''
    x = 0
    while bridge[moto['y']][moto['x']+x] == 0:
        x += 1
    x2 = 0
    while bridge[moto['y']][moto['x']+x+x2] == 1:
        x2 += 1
    return x, x2

# game loop
while True:
    m_list = []  # list of the motorbikes
    s = int(input())  # the motorbikes' speed
    for i in range(m):
        # a: indicates whether the motorbike is activated "1" or detroyed "0"
        x, y, a = [int(j) for j in input().split()]
        m_list.append({'x': x, 'y': y, 'a': a})


    # A single line containing one of 6 keywords: SPEED, SLOW, JUMP, WAIT, UP, DOWN.