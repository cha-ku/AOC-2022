#!/usr/bin/python3

import os
import sys
from math import inf

def problem1(input_lines):
    right = 0
    down = 0
    left = inf
    cave = []
    for line in input_lines:
        coords = [eval(l) for l in line.split(' -> ')]
        cave.append(coords)
        m = max(coords, key=lambda x : x[0])[0]
        mini = min(coords, key=lambda x : x[0])[0]
        d = max(coords, key=lambda x : x[1])[1]
        right = max(right, m)
        down = max(down, d)
        left = min(left, mini)
    blocks = []
    for rock_line in cave:
        i = 0
        while i+1 < len(rock_line):
            # vertical
            if rock_line[i][0] == rock_line[i+1][0]:
                column = rock_line[i][0]
                vstart , vend = rock_line[i][1] , rock_line[i+1][1]
                inc = 1
                if vstart > vend:
                    inc = -1
                for j in range(vstart, vend+inc, inc):
                    blocks.append((j, column))
            # horizontal
            else:
                row = rock_line[i][1]
                hstart , hend = rock_line[i][0], rock_line[i+1][0]
                inc = 1
                if hstart > hend:
                    inc = -1
                for k in range(hstart, hend+inc, inc):
                    blocks.append((row, k))
            i += 1

    start_pos = (0, 500)
    tick = 0
    outside = False
    at_rest = True
    particles = 0
    while not outside:
        tick += 1
        if at_rest:
            particles += 1
            at_rest = False
            pos = start_pos
        if pos[1] not in range(left, right+1) or pos[0] not in range(down):
            print(f'particle {particles} is at {pos} and has gone outside')
            outside = True
        else:
            if (pos[0]+1, pos[1]) not in blocks:
                pos = (pos[0]+1, pos[1])
            elif (pos[0]+1, pos[1]-1) not in blocks:
                pos = (pos[0]+1, pos[1]-1)
            elif (pos[0]+1, pos[1]+1) not in blocks:
                pos = (pos[0]+1, pos[1]+1)
            else:
                print(f'particle {particles} has come to rest at {pos}')
                at_rest = True
                blocks.append(pos)
    print(particles-1)


def problem2(input_lines):
    right = 0
    down = 0
    left = inf
    cave = []
    for line in input_lines:
        coords = [eval(l) for l in line.split(' -> ')]
        cave.append(coords)
        m = max(coords, key=lambda x : x[0])[0]
        mini = min(coords, key=lambda x : x[0])[0]
        d = max(coords, key=lambda x : x[1])[1]
        right = max(right, m)
        down = max(down, d)
        left = min(left, mini)
    blocks = set()
    for rock_line in cave:
        i = 0
        while i+1 < len(rock_line):
            # vertical
            if rock_line[i][0] == rock_line[i+1][0]:
                column = rock_line[i][0]
                vstart , vend = rock_line[i][1] , rock_line[i+1][1]
                inc = 1
                if vstart > vend:
                    inc = -1
                for j in range(vstart, vend+inc, inc):
                    blocks.add((j, column))
            # horizontal
            else:
                row = rock_line[i][1]
                hstart , hend = rock_line[i][0], rock_line[i+1][0]
                inc = 1
                if hstart > hend:
                    inc = -1
                for k in range(hstart, hend+inc, inc):
                    blocks.add((row, k))
            i += 1

    start_pos = (0, 500)
    blocked = False
    at_rest = True
    particles = 0
    while not blocked:
        if at_rest:
            particles += 1
            at_rest = False
            pos = start_pos
        if pos[0]+1 == down + 2:
            print(f'particle {particles} has come to rest on the floor at {pos}')
            at_rest = True
            blocks.add(pos)
        elif (pos[0]+1, pos[1]) not in blocks:
            pos = (pos[0]+1, pos[1])
        elif (pos[0]+1, pos[1]-1) not in blocks:
            pos = (pos[0]+1, pos[1]-1)
        elif (pos[0]+1, pos[1]+1) not in blocks:
            pos = (pos[0]+1, pos[1]+1)
        else:
            print(f'particle {particles} has come to rest at {pos}')
            at_rest = True
            blocks.add(pos)
        if pos == start_pos and at_rest:
            blocked = True
    print(particles)

if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    is_test = False
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        is_test = True
    if is_test:
        problem_input = test_input
    else:
        problem_input = aoc_input
    with open(problem_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    #problem1(input_lines)
    problem2(input_lines)
