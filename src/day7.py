#!/usr/bin/python3

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.dirs = {}
        self.files = {}
        self.parent = parent

    def add_file(self, fname, fsize):
        self.files[fname] = fsize

    def add_dir(self, dir_name):
        self.dirs[dir_name] = Directory(dir_name, self)

    def __str__(self):
        if self.parent:
            return f'{self.name} - {[x.name for x in self.dirs.values()]} , {self.files}, parent={self.parent.name}'
        else:
            return f'{self.name} - {[x.name for x in self.dirs.values()]} , {self.files}'

def parse(input_lines):
    curr_dir = None
    for line in input_lines:
        if line.split()[0] == '$':
            if line.split()[1] == 'cd':
                dir_val = line.split()[2]
                if not curr_dir:
                    curr_dir = Directory(dir_val, None)
                    top_dir = curr_dir
                elif dir_val == '..':
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = curr_dir.dirs[dir_val]
            elif line.split()[1] == 'ls':
                pass
        elif line.split()[0] == 'dir':
            curr_dir.add_dir(line.split()[1])
        else:
            curr_dir.add_file(line.split()[1], int(line.split()[0]))
    return top_dir

def print_parsed(input_lines):
    top_dir = parse(input_lines)
    parsed = [top_dir]
    while parsed:
        curr_dir = parsed.pop()
        print(curr_dir)
        for d in curr_dir.dirs:
            parsed.append(curr_dir.dirs[d])

def populate_dir_sizes(current_dir: Directory, dir_sizes: dict):
    if current_dir in dir_sizes:
        return dir_sizes[current_dir]
    else:
        dir_sizes[current_dir] = sum(current_dir.files.values()) + sum([populate_dir_sizes(d, dir_sizes) for d in current_dir.dirs.values()])
        return dir_sizes[current_dir]

def problem1(input_lines):
    top_dir = parse(input_lines)
    dir_sz = {}
    populate_dir_sizes(top_dir, dir_sz)
    result = 0
    for k , v in dir_sz.items():
        if v <= 100000:
            result += v
    print(result)

def problem2(input_lines):
    top_dir = parse(input_lines)
    dir_sz = {}
    populate_dir_sizes(top_dir, dir_sz)
    total_disk_space = 70000000
    target_unused_space = 30000000
    used_space = total_disk_space - dir_sz[top_dir]
    print(min(filter(lambda e : (used_space + e) >= target_unused_space, dir_sz.values())))

if __name__ == '__main__':
    with open('input_day7.txt') as ipfile:
        input_lines = [line.strip('\n') for line in ipfile.readlines()]
    problem1(input_lines)
    problem2(input_lines)
