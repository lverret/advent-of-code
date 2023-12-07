import re
import math


def parse(l):
    return list(map(int, re.findall("\d+", l[0]))), list(map(int, re.findall("\d+", l[1])))

def part1(l):
    t, d = parse(l)
    return math.prod(sum(1 for k in range(t[i]) if k * (t[i] - k) > d[i]) for i in range(len(t)))

def part2(l):
    t, d = map(lambda x: int("".join(map(str, x))), parse(l))
    return sum(1 for k in range(t) if k * (t - k) > d)
