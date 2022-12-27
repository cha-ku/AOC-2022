#!/usr/bin/python3

import os
import sys

def problem1(input_lines):
    pass

def problem2(input_lines):
    pass

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
