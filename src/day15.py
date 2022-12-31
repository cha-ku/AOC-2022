#!/usr/bin/python3

import os
import sys
import re
from math import inf
from collections import namedtuple


def problem1(input_lines, y_):
    Beacon = namedtuple("Beacon", "x y")
    Sensor = namedtuple("Sensor", "x y")
    pattern = re.compile(
        'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    sensors = []
    beacons = set()
    min_x = inf
    max_x = -inf
    ranges = set()
    for line in input_lines:
        m = pattern.match(line)
        sensor = Sensor(int(m.group(1)), int(m.group(2)))
        beacon = Beacon(int(m.group(3)), int(m.group(4)))
        beacons.add((beacon.x, beacon.y))
        manhattan = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        min_x = min(sensor.x - manhattan, min_x)
        max_x = max(sensor.x + manhattan, max_x)
        sensors.append((sensor, manhattan))
    print(min_x, max_x)
    covered = set()
    for x_ in range(min_x, max_x + 1):
        for (s, m) in sensors:
            if m >= (abs(s.x - x_) + abs(s.y - y_)) and (x_, y_) not in beacons:
                covered.add((x_, y_))
    print(len(covered))


def problem2(input_lines):
    pass


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
