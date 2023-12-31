import re


def part1(l):
    return sum((lambda x: int(x[0]+x[-1]))(re.findall("\d", s)) for s in l)

def part2(l):
    d = {"zer": "o0", "on": "e1", "tw": "o2", "thre": "e3", "fou": "r4", "fiv": "e5", "si": "x6", "seve": "n7", "eigh": "t8", "nin": "e9"}
    return part1([re.compile("|".join(f"{x}(?={d[x][0]})" for x in d)).sub(lambda x: d[x.group()][1], s) for s in l])
