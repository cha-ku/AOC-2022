#!/usr/bin/python3

import os

class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = None
        self.operation = None
        self.test = None
        self.test_true = None
        self.test_false = None
        self.count = 0

    def __str__(self):
        return f'Monkey {self.name} has items with worry levels {self.items}, will test for each item with {self.operation}, will throw to monkey {self.test_true} if test divisible by {self.test} is true or to monkey {self.test_false} if false'

    def operate_div_3(self, monkey_map):
        while self.items:
            old = self.items.pop(0)
            result = eval(self.operation)
            result = int(result/3)
            if result % int(self.test) == 0:
                monkey_map[self.test_true].items.append(result)
            else:
                monkey_map[self.test_false].items.append(result)
            self.count += 1

    def operate_no_div_3(self, monkey_map, modulo):
        while self.items:
            old = self.items.pop(0)
            result = eval(self.operation)
            if result % self.test == 0:
                monkey_map[self.test_true].items.append(result % modulo)
            else:
                monkey_map[self.test_false].items.append(result % modulo)
            self.count += 1

def construct_monkey_map(input_lines):
    chunked_actions =[input_lines[x:x+6] for x in range(0, len(input_lines), 7)]
    monkey_map = {}
    for action in chunked_actions:
        monkey_name = action[0].split(':')[0][-1]
        monkey_map[monkey_name] = Monkey(monkey_name)
        monkey_map[monkey_name].items = [int(level) for level in action[1].split(':')[1].split(',')]
        monkey_map[monkey_name].operation = action[2].split(':')[1].strip(' ').split('=')[1]
        monkey_map[monkey_name].test = int(action[3].split(':')[1].split(' ')[-1])
        monkey_map[monkey_name].test_true = action[4].split(':')[1][-1]
        monkey_map[monkey_name].test_false = action[5].split(':')[1][-1]
    return monkey_map

def problem1(input_lines):
    monkey_map = construct_monkey_map(input_lines)
    for i in range(0,20):
        for k in monkey_map:
            monkey_map[k].operate_div_3(monkey_map)
    counts = []
    for k in monkey_map:
        counts.append(monkey_map[k].count)
    print(sorted(counts)[-1] * sorted(counts)[-2])

def problem2(input_lines):
    monkey_map = construct_monkey_map(input_lines)
    modulo = 1
    for k in monkey_map:
        modulo *= monkey_map[k].test
    for i in range(10000):
        for k in monkey_map:
            monkey_map[k].operate_no_div_3(monkey_map, modulo)
    counts = []
    for k in monkey_map:
        counts.append(monkey_map[k].count)
    print(sorted(counts)[-1] * sorted(counts)[-2])

if __name__ == '__main__':
    test_input = 'test_input.txt'
    aoc_input = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    with open(aoc_input) as ipfile:
    #with open(test_input) as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
