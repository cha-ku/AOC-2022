#!/usr/bin/python3

import os
import sys
import re
from math import inf
from collections import namedtuple


def problem1(input_lines, y_):
    Point = namedtuple("Point", "x y")
    pattern = re.compile(
        'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    sensors = []
    beacons = set()
    intervals = []
    for line in input_lines:
        m = pattern.match(line)
        sensor = Point(int(m.group(1)), int(m.group(2)))
        beacon = Point(int(m.group(3)), int(m.group(4)))
        beacons.add((beacon.x, beacon.y))
        manhattan = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        sensors.append((sensor, manhattan))
        # if y_ is within manhattan distance of sensor.y
        if abs(sensor.y - y_) <= manhattan:
            vertical_dist_to_target_row = abs(sensor.y - y_)
            half_interval = manhattan - vertical_dist_to_target_row
            start_x, end_x = min(sensor.x - half_interval, sensor.x + half_interval),\
                max(sensor.x - half_interval, sensor.x + half_interval)
            intervals.append([start_x, end_x])
    intervals.sort()
    collapsed = []
    collapsed.append(intervals[0])
    for interval in intervals[1:]:
        if collapsed[-1][0] <= interval[0] <= collapsed[-1][1]:
            collapsed[-1][1] = max(collapsed[-1][1], interval[1])
        else:
            collapsed.append(interval)
    print(collapsed[-1][-1] - collapsed[0][0])


def problem2(input_lines):
    Point = namedtuple("Point", "x y")
    pattern = re.compile(
        'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    sensors = []
    beacons = set()
    for line in input_lines:
        m = pattern.match(line)
        sensor = Point(int(m.group(1)), int(m.group(2)))
        beacon = Point(int(m.group(3)), int(m.group(4)))
        beacons.add((beacon.x, beacon.y))
        manhattan = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        sensors.append((sensor, manhattan))
    positive_lines = []
    negative_lines = []
    for sensor, manh in sensors:
        positive_lines.extend(
            [sensor.x - sensor.y - manh, sensor.x - sensor.y + manh])
        negative_lines.extend(
            [sensor.x + sensor.y - manh, sensor.x + sensor.y + manh])
    assert (len(positive_lines) == len(negative_lines) == 2*len(sensors))
    pos, neg = None, None
    for i in range(2 * len(sensors)):
        for j in range(i+1, 2*len(sensors)):
            if abs(positive_lines[i] - positive_lines[j]) == 2:
                pos = min(positive_lines[i], positive_lines[j]) + 1
            if abs(negative_lines[i] - negative_lines[j]) == 2:
                neg = min(negative_lines[i], negative_lines[j]) + 1
    x, y = (pos + neg) // 2, (neg - pos) // 2
    print(x * 4000000 + y)


if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + \
        os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    is_test = False
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        is_test = True
    if is_test:
        problem_input = test_input
        y_ = 10
    else:
        problem_input = aoc_input
        y_ = 2000000
    with open(problem_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines, y_)
    problem2(input_lines)
