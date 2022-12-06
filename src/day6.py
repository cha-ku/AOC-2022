#!/usr/bin/python3

def is_chunk_unique(chunk):
    return len(set(chunk)) == len(chunk)

def problem1(input_lines):
    inputline = input_lines[0]
    start_indx = 0
    processed = 4
    for end_indx in range(4, len(inputline)):
        chunk = inputline[start_indx:end_indx]
        if is_chunk_unique(chunk):
            break
        else:
            start_indx += 1
            processed += 1
    print(processed)

def problem2(input_lines):
    inputline = input_lines[0]
    start_indx = 0
    processed = 14
    for end_indx in range(14, len(inputline)):
        chunk = inputline[start_indx:end_indx]
        if is_chunk_unique(chunk):
            break
        else:
            start_indx += 1
            processed += 1
    print(processed)

if __name__ == '__main__':
    with open('input_day6.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
