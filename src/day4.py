#!/usr/bin/python3

def check_if_subset(range1, range2):
    if range1[0] in range2 and range1[-1] in range2:
        return True
    if range2[0] in range1 and range2[-1] in range1:
        return True
    return False

def get_overlapping_intervals(range1, range2):
    start_overlap = max(range1[0], range2[0])
    end_overlap = min(range1[1], range2[1])
    return start_overlap <= end_overlap

def problem1(input_lines):
    overlapped = 0
    for line in input_lines:
        sections = line.split(',')
        fst = [int(e) for e in sections[0].split('-')]
        fst[1] = fst[1] + 1
        snd = [int(e) for e in sections[1].split('-')]
        snd[1] = snd[1] + 1
        if check_if_subset(range(fst[0], fst[1]), range(snd[0], snd[1])):
            #print(fst, snd)
            overlapped += 1
    return overlapped

def problem2(input_lines):
    intervals_overlap = 0
    for line in input_lines:
        sections = line.split(',')
        fst = [int(e) for e in sections[0].split('-')]
        snd = [int(e) for e in sections[1].split('-')]
        if get_overlapping_intervals(fst, snd):
            intervals_overlap += 1
    return intervals_overlap


if __name__ == '__main__':
    with open('input_day4.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    with open('test_input.txt') as ipfile:
        test_input_lines = [line.strip('\n') for line in ipfile.readlines()]
    print(problem1(input_lines))
    print(problem2(input_lines))
