#!/usr/bin/python3

import os

def is_touching(head_coord, tail_coord):
    # H - 0,0
    # T - 0,1 | 1,0 | 0,-1 | -1,0 | -1,-1 | -1,1 | 1,1 | 1,-1 | 0,0
    head_coord_x, head_coord_y = head_coord[0], head_coord[1]
    tail_coord_x, tail_coord_y = tail_coord[0], tail_coord[1]
    if (tail_coord_x == head_coord_x or tail_coord_x == head_coord_x+1 or tail_coord_x == head_coord_x-1) and (tail_coord_y == head_coord_y or tail_coord_y == head_coord_y-1 or tail_coord_y == head_coord_y+1):
        return True
    else:
        return False

def move_tail(coords, dirn, tail_pos):
    head = coords[0]
    tail = coords[1]
    # H - 0,0
    # T - 0,1 | 1,0 | 0,-1 | -1,0
    # if tail x is equal to head x or tail y equals head y - in the same axis - move in the same direction
    if tail[0] == head[0] or tail[1] == head[1]:
        if dirn == 'U':
            tail[1] += 1
        elif dirn == 'D':
            tail[1] -= 1
        elif dirn == 'L':
            tail[0] -= 1
        elif dirn == 'R':
            tail[0] += 1
        else:
            print("Invalid direction")
    # move diagonally
    else:
        if is_touching(head, [tail[0]+1, tail[1]+1]):
            tail[0] += 1
            tail[1] += 1
        elif is_touching(head, [tail[0]-1, tail[1]+1]):
            tail[0] -= 1
            tail[1] += 1
        elif is_touching(head, [tail[0]+1, tail[1]-1]):
            tail[0] += 1
            tail[1] -= 1
        elif is_touching(head, [tail[0]-1, tail[1]-1]):
            tail[0] -= 1
            tail[1] -= 1
        else:
            print('Cannot determine diagonal movement direction')
    tail_pos.add(tuple(tail))
    return [head, tail], tail_pos


def move_and_check(direction, length, coords, tail_pos):
    while length:
        if direction == 'U':
            coords[0][1] += 1
        elif direction == 'D':
            coords[0][1] -= 1
        elif direction == 'L':
            coords[0][0] -= 1
        elif direction == 'R':
            coords[0][0] += 1
        else:
            print('invalid direction')
        length -= 1
        if not is_touching(coords[0], coords[1]):
            coords, tail_pos = move_tail(coords, direction, tail_pos)
    #print(f'H - {coords[0]} T - {coords[1]}')
    return coords, tail_pos

def move_and_check_10(direction, length, coords, tail_pos):
    while length:
        if direction == 'U':
            coords[0][1] += 1
        elif direction == 'D':
            coords[0][1] -= 1
        elif direction == 'L':
            coords[0][0] -= 1
        elif direction == 'R':
            coords[0][0] += 1
        else:
            print('invalid direction')
        length -= 1
        for i in range(0, len(coords)-1):
            if not is_touching(coords[0], coords[1]):
                coords, tail_pos = move_tail(coords, direction, tail_pos)
    #print(f'H - {coords[0]} T - {coords[1]}')
    return coords, tail_pos


def problem1(input_lines):
    start_coords = [[0,0],[0,0]]
    tail_pos = set([])
    tail_pos.add(tuple(start_coords[1]))
    for line in input_lines:
        direction = line.split(' ')[0]
        length = int(line.split(' ')[1])
        start_coords, tail_pos = move_and_check(direction, length, start_coords, tail_pos)
    #print(tail_pos)
    print(len(tail_pos))

def problem2(input_lines):
    start_coords = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    tail_pos = set([])
    tail_pos.add(tuple(start_coords[1]))
    for line in input_lines:
        direction = line.split(' ')[0]
        length = int(line.split(' ')[1])


if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    with open(aoc_input) as ipfile:
    #with open(test_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
