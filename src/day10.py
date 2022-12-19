#!/usr/bin/python3

import os

def problem1(input_lines):
    interesting_cycles = range(20, 221, 40)
    x_reg = 1
    cycles = 0
    indx = 0
    prev_addx = False
    result = 0
    val = 0
    while indx < len(input_lines):
        cycles += 1
        if cycles in interesting_cycles:
            #print(f'cycle {cycles} X register = {x_reg}')
            result += cycles * x_reg
        instruction = input_lines[indx]
        if instruction == 'noop':
            indx += 1
        else:
            if prev_addx:
                prev_addx = False
                x_reg += val
                indx += 1
            else:
                val = int(instruction.split(' ')[-1])
                prev_addx = True
    print(result)

def problem2(input_lines):
    grid = ['.'] * 240
    x_reg = 1
    cycles = 0
    indx = 0
    prev_addx = False
    val = 0
    while indx < len(input_lines):
        cycles += 1
        pos = cycles - 1
        row = pos // 40
        col = pos % 40
        if col in {x_reg-1, x_reg, x_reg+1}:
            #print(pos, {x_reg-1, x_reg, x_reg+1}, row, col)
            grid[pos] = '#'
        instruction = input_lines[indx]
        if instruction == 'noop':
            indx += 1
        else:
            if prev_addx:
                prev_addx = False
                x_reg += val
                indx += 1
            else:
                val = int(instruction.split(' ')[-1])
                prev_addx = True
    for x in range(0, len(grid), 40):
        print(''.join(grid[x:x+40]))
    #[print(_) for _ in grid_2d]
    #[print(_) for _ in grid]

if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    with open(aoc_input) as ipfile:
    #with open(test_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
