import re
import math


def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def parse(l):
    return list(map(int, re.findall("\d+", l[0]))), list(map(int, re.findall("\d+", l[1])))

def part1(l):
    t, d = parse(l)
    return math.prod(sum(1 for k in range(t[i]) if k * (t[i] - k) > d[i]) for i in range(len(t)))

def part2(l):
    t, d = parse(l)
    t, d = int("".join(map(str, t))), int("".join(map(str, d)))
    return sum(1 for k in range(t) if k * (t - k) > d)


if __name__ == "__main__":
    lines = read_txt("day6.txt")
    print(part1(lines))
    print(part2(lines))