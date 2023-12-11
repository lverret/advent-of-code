import re
import math


def parse(l):
    g = list(l[0])
    a = {n: {"L": l, "R": r} for s in l[2:] for n, l, r in re.findall("(.*) = \((.*), (.*)\)", s)}
    return g, a

def search(a, g, n, c):
    i, j = 0, 0
    while c(n) or i == 0:
        n = a[n][g[j]]
        i += 1
        j = (j + 1) % len(g)
    return i

def part1(l):
    g, a = parse(l)
    return search(a, g, "AAA", lambda x: x != "ZZZ")

def part2(l):
    g, a = parse(l)
    return math.lcm(*[search(a, g, n, lambda x: x[-1] != "Z") for n in a if n[-1] == "A"])