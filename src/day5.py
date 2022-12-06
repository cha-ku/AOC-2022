#!/usr/bin/python3

def create_initial_stack(input_lines):
    stack_values = {}
    for stack_line in input_lines:
        if not stack_line:
            break
        for i , line in enumerate(stack_line):
            for c in line:
                if not (c == ' ' or c == '[' or c == ']'):
                    if i not in stack_values:
                        stack_values[i] = []
                    stack_values[i].append(c)
    stacks = {}
    for val in stack_values.values():
        val.reverse()
        stacks[val.pop(0)] = val[1:]
    return stacks

def problem1(input_lines):
    init_stack = create_initial_stack(input_lines)
    for line in input_lines:
        if line.startswith('move'):
            line_list = line.split()
            qty_crates, mv_from, mv_to = int(line_list[1]), line_list[3], line_list[5]
            #print(f"moving {init_stack[mv_from][-qty_crates:]} from {mv_from} to {mv_to}")
            init_stack[mv_to] += reversed(init_stack[mv_from][-qty_crates:])
            del init_stack[mv_from][-qty_crates:]
    result = ''
    for key in sorted(init_stack.keys()):
        result += init_stack[key][-1]
    print(result)

def problem2(input_lines):
    init_stack = create_initial_stack(input_lines)
    for line in input_lines:
        if line.startswith('move'):
            line_list = line.split()
            qty_crates, mv_from, mv_to = int(line_list[1]), line_list[3], line_list[5]
            #print(f"moving {init_stack[mv_from][-qty_crates:]} from {mv_from} to {mv_to}")
            init_stack[mv_to] += init_stack[mv_from][-qty_crates:]
            del init_stack[mv_from][-qty_crates:]
    result = ''
    for key in sorted(init_stack.keys()):
        result += init_stack[key][-1]
    print(result)

if __name__ == '__main__':
    with open('input_day5.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
