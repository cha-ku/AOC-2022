#!/usr/bin/python3

import os
import sys

def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1 
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            cmp = compare(left[i], right[i])
            if cmp == -1:
                return -1 
            if cmp == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return -1
        elif i == len(right) and i < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    else:
        return compare([left], right)


def problem1(input_lines):
    result = 0
    for group, i in enumerate(range(0, len(input_lines), 3)):
        left = eval(input_lines[i])
        right = eval(input_lines[i+1])
        if compare(left, right) == -1:
            #print(f'group {group}: {left}, {right}')
            result += group + 1 
    print(result)

def problem2(input_lines):
    output = []
    for i in range(0, len(input_lines), 3):
        left = eval(input_lines[i])
        right = eval(input_lines[i+1])
        output.append(left)
        output.append(right)
    output.append([[2]])
    output.append([[6]])
    from functools import cmp_to_key
    sorted_packets = sorted(output, key=cmp_to_key(lambda left, right: compare(left, right)))
    result = 1
    for i, packet in enumerate(sorted_packets):
        if packet == [[2]] or packet == [[6]]:
            result *= i+1
    print(result)


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
    problem1(input_lines)
    problem2(input_lines)