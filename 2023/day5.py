import sys
import re


def parse(l):
    l = list(map(lambda x: [int(k) for k in x], map(lambda x: re.findall("\d+", x), "\n".join(l).split("map"))))
    return l[0], l[1:]

def lookup(r, m):
    for i in range(1, len(m), 3):
        start, end, cut = m[i], m[i] + m[i+1], m[i] - m[i-1]
        if start <= r[0] < end and start <= r[-1] < end:
            return [range(r[0] - cut, r[-1] - cut + 1)]
        elif start <= r[0] < end and not start <= r[-1] < end:
            return [
                *lookup(range(r[0], end), m), 
                *lookup(range(end, r[-1] + 1), m)
            ]
        elif start <= r[-1] < end:
            return [
                *lookup(range(r[0], start), m), 
                *lookup(range(start, r[-1] + 1), m)
            ]
    return [r]

def find_min(seeds, maps):
    mini = sys.maxsize
    for s in seeds:
        for m in maps:
            s = [j for r in s for j in lookup(r, m)]
        mini = min(mini, *[k[0] for k in s])
    return mini

def part1(l):
    seeds, maps = parse(l)
    seeds = [[range(s, s + 2)] for s in seeds]
    return find_min(seeds, maps)

def part2(l):
    seeds, maps = parse(l)
    seeds = [[range(seeds[i], seeds[i] + seeds[i+1])] for i in range(0, len(seeds), 2)]
    return find_min(seeds, maps)
