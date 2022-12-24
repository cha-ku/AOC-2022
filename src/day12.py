#!/usr/bin/python3

import os
import sys
from collections import deque

def generate_2d_grid(input_lines):
    return [[ord(d) - ord('a') + 1 for d in line] for line in input_lines]

def bfs(q, grid):
    visited = set()
    while q:
        (r, c), distance = q.popleft()
        if (r, c) not in visited:
            visited.add((r , c))
            if grid[r][c] == 27:
                return distance
            for row, col in [(-1,0),(1,0),(0,-1),(0,1)]: #down, up, left, right
                new_row = r + row
                new_col = c + col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] <= grid[r][c] + 1:
                    q.append(((new_row , new_col), distance+1))


def problem1(input_lines):
    Q = deque()
    grid_2d = generate_2d_grid(input_lines)
    for col in range(len(input_lines[0])):
        for row in range(len(input_lines)):
            if input_lines[row][col] == 'S':
                Q.append(((row, col), 0))
                grid_2d[row][col] = 1
            if input_lines[row][col] == 'E':
                grid_2d[row][col] = 27
    #[print(_) for _ in grid_2d]
    print(bfs(Q, grid_2d))


def problem2(input_lines):
    Q = deque()
    grid_2d = generate_2d_grid(input_lines)
    for col in range(len(input_lines[0])):
        for row in range(len(input_lines)):
            if input_lines[row][col] == 'S' or input_lines[row][col] == 'a':
                Q.append(((row, col), 0))
                grid_2d[row][col] = 1
            if input_lines[row][col] == 'E':
                grid_2d[row][col] = 27
    #[print(_) for _ in grid_2d]
    print(bfs(Q, grid_2d))

if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    is_test = False
    if len(sys.argv) == 2 and sys.argv[1] == 't':
        is_test = True
    if is_test:
        problem_input = test_input
    else:
        problem_input = aoc_input
    with open(problem_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)