import re
import math


def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def part1(l):
    d = {"red": 12, "green": 13, "blue": 14}
    return sum((k + 1) * all(map(lambda x: int(x[0]) <= d[x[1]], map(str.split, re.findall("|".join("\d{1,2} "f"{x}" for x in d), s)))) for k, s in enumerate(l))

def part2(l):
    return sum(math.prod(map(lambda x: max([int(k) for k in x if k]), zip(*re.findall("|".join("(\d{1,2} "f"(?={x}))" for x in ["red", "green", "blue"]), s)))) for s in l)


if __name__ == "__main__":
    lines = read_txt("day2.txt")
    print(part1(lines))
    print(part2(lines))