import re
import math


def parse(l):
    return [list(map(int, re.findall("-?\d+\.?\d*", x))) for x in l]

def ext(l, f):
    l = parse(l)
    comb = [[(-1) ** k * math.comb(n, k) for k in range(0, n+1)] for n in range(len(l[0])+1)]
    r = 0
    for t in l:
        for i in range(len(t)):
            n = len(comb[i])
            if all(sum(comb[i][k] * t[j+n-(k+1)] for k in range(n)) == 0 for j in range(len(t) - n + 1)):
                break
        r += f(comb, i, n, t)
    return r

def part1(l):
    def f(comb, i, n, t):
        return - sum(comb[i][k] * t[len(t) - k] for k in range(1, n))
    return ext(l, f)

def part2(l):
    def f(comb, i, n, t):
        return - sum(comb[i][n-k-1] * t[k-1] for k in range(1, n)) * comb[i][-1]
    return ext(l, f)