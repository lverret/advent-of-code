import math
import re


def parse(l):
    d = [[int(n.group()), [(i, j) for i in [k-1, k, k+1] for j in range(n.start()-1, n.end()+1)]] for k in range(len(l)) for n in re.finditer("\d+", l[k])]
    s = [[n.group(), (k, n.start())] for k in range(len(l)) for n in re.finditer("[^\d.]", l[k])]
    return d, s

def part1(l):
    d, s = parse(l)
    return sum(k for k, a in d for _, p in s if p in a)

def part2(l):
    d, s = parse(l)
    return sum(math.prod(c) for c in [[k for k, a in d if p in a] for x, p in s if x == "*"] if len(c) == 2)
