#!/usr/bin/python3
import copy

def problem1(input_lines):
    int_input_lines = []
    for line in input_lines:
        int_input_lines.append([int(x) for x in line])
    length = len(input_lines)
    width = len(input_lines[0])
    already_visible = [[0]*width for _ in range(length)]

    #mark edges as visible
    for i in range(len(already_visible)):
        if i == 0 or i == len(already_visible)-1:
            already_visible[i] = [1]*width
        else:
            already_visible[i][0] = 1
            already_visible[i][-1] = 1

    #left view
    for i in range(len(int_input_lines)):
        left_max = int_input_lines[i][0]
        for j in range(1, len(int_input_lines[i])):
            if int_input_lines[i][j] > left_max:
                left_max = int_input_lines[i][j]
                already_visible[i][j] = 1

    #right view
    for i in range(len(int_input_lines)):
        right_max = int_input_lines[i][-1]
        for j in range(-2, -len(int_input_lines[i]), -1):
            if int_input_lines[i][j] > right_max:
                right_max = int_input_lines[i][j]
                already_visible[i][j] = 1

    #top view
    for i in range(len(int_input_lines[0])):
        top_max = int_input_lines[0][i]
        for j in range(1, len(int_input_lines)):
            if int_input_lines[j][i] > top_max:
                top_max = int_input_lines[j][i]
                already_visible[j][i] = 1

    #bottom view
    for i in range(len(int_input_lines[0])):
        bottom_max = int_input_lines[-1][i]
        for j in range(-2, -len(int_input_lines), -1):
            if int_input_lines[j][i] > bottom_max:
                bottom_max = int_input_lines[j][i]
                already_visible[j][i] = 1

    #[print(_) for _ in already_visible]
    #print('\n')
    #[print(_) for _ in int_input_lines]
    #print('\n')
    print(sum([sum(row) for row in already_visible]))

def problem2(input_lines):
    trees = []
    for line in input_lines:
        trees.append([int(x) for x in line])

    #mark edge scenic score as 0
    scenic_score = [[0]*len(trees[0]) for _ in range(len(trees))]

    left_ss  = copy.deepcopy(scenic_score)
    right_ss = copy.deepcopy(scenic_score)
    top_ss   = copy.deepcopy(scenic_score)
    down_ss  = copy.deepcopy(scenic_score)

    #left scenic score
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees[i])-1):
            is_taller = True
            elem = trees[i][j]
            for k in range(j+1, len(trees[0])):
                if is_taller:
                    if trees[i][k] < elem:
                        right_ss[i][j] += 1
                    else:
                        right_ss[i][j] += 1
                        is_taller = False

    #right scenic score
    for i in range(1, len(trees)-1):
        for j in range(-2, -len(trees[i]), -1):
            is_taller = True
            elem = trees[i][j]
            for k in range(j-1, -len(trees[i])-1, -1):
                if is_taller:
                    if trees[i][k] < elem:
                        left_ss[i][j] += 1
                    else:
                        left_ss[i][j] += 1
                        is_taller = False

    #down scenic score
    for i in range(1, len(trees[0])-1):
        for j in range(1, len(trees)-1):
            is_taller = True
            elem = trees[j][i]
            for k in range(j+1, len(trees)):
                if is_taller:
                    if trees[k][i] < elem:
                        down_ss[j][i] += 1
                    else:
                        down_ss[j][i] += 1
                        is_taller = False

    #top scenic score
    for i in range(1, len(trees[0])-1):
        for j in range(-2, -len(trees), -1):
            is_taller = True
            elem = trees[j][i]
            for k in range(j-1, -len(trees[i])-1, -1):
                if is_taller:
                    if trees[k][i] < elem:
                        top_ss[j][i] += 1
                    else:
                        top_ss[j][i] += 1
                        is_taller = False

    #[print(x) for x in trees]
    #print('right-')
    #[print(z) for z in right_ss]
    #print('left-')
    #[print(z) for z in left_ss]
    #print('down-')
    #[print(z) for z in down_ss]
    #print('up-')
    #[print(z) for z in top_ss]
    max_score = 0
    for i in range(len(scenic_score)):
        for j in range(len(scenic_score[i])):
            max_score = max(max_score, right_ss[i][j] * left_ss[i][j] * top_ss[i][j] * down_ss[i][j])
    print(max_score)

if __name__ == '__main__':
    with open('input_day8.txt') as ipfile:
    #with open('test_input.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
