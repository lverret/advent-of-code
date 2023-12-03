import math
import re

def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def parse(l):
    d, s = [], []
    for k in range(len(l)):
        for n in re.finditer("\d+|[^.]", l[k]):
            c = n.group()
            if c.isdecimal():
                d.append([int(c), [(i, j) for i in [k-1, k, k+1] for j in range(n.start()-1, n.end()+1)]])
            else:
                s.append([c, (k, n.start())])
    return d, s

def part1(l):
    d, s = parse(l)
    return sum(k for k, a in d for _, p in s if p in a)

def part2(l):
    d, s = parse(l)
    return sum(math.prod(c) for c in [[k for k, a in d if p in a] for x, p in s if x == "*"] if len(c) == 2)


if __name__ == "__main__":
    lines = read_txt("day3.txt")
    print(part1(lines))
    print(part2(lines))