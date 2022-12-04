#!/usr/bin/python3

def get_priority(c):
    if c.islower():
        char_priority = (ord(c) - ord('a')) + 1
    else:
        char_priority = (ord(c) - ord('A')) + 27
    return char_priority

def get_priority_line(line):
    cpmnt1 = set(line[:int(len(line)/2)])
    cpmnt2 = set(line[int(len(line)/2):])
    line_priority = 0
    for c in cpmnt1.intersection(cpmnt2):
        line_priority = line_priority + get_priority(c)
    return line_priority

def problem1(list_lines):
    priority = 0
    for line in list_lines:
        # print(f'{line} : {intx}')
        priority = priority + get_priority_line(line)
    return priority

def get_common_item(list_items):
    return set(list_items[0]).intersection(set(list_items[1]).intersection(list_items[2]))

def problem2(input_lines):
    global_priority = 0
    for i in range(0, len(input_lines), 3):
        grp_three = input_lines[i:i+3]
        for c in get_common_item(grp_three):
            global_priority = global_priority + get_priority(c)
    return global_priority

if __name__ == '__main__':
    with open('input_day3.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    print(problem1(input_lines))
    print(problem2(input_lines))
