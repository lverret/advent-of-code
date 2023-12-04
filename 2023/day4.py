import math
import re


def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def parse(l):
    return [(re.findall("\d+", s.split("|")[0])[1:], re.findall("\d+", s.split("|")[1])) for s in l]

def n(a, b):
    return sum(k in a for k in b)

def part1(l):
    return sum(math.floor(2**(n(a, b)-1)) for a, b in parse(l))

def part2(l):
    nn = [n(a, b) for a, b in parse(l)]
    d = [1 for _ in range(len(nn))]
    for k, l in enumerate(d):
        for _ in range(l):
            for i in range(nn[k]):
                if k + i + 1 < len(d):
                    d[k + i + 1] += 1
    return sum(d)


if __name__ == "__main__":
    lines = read_txt("day4.txt")
    print(part1(lines))
    print(part2(lines))