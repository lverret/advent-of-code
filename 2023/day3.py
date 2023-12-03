import math

def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def parse(l):
    digits, symbols = [], []
    digit = ["", set()]
    for i in range(len(l)):
        for j in range(len(l[i])):
            c = l[i][j]
            if c.isdigit():
                digit[0] += c
                digit[1].update([(i+k, j+l) for k in range(-1, 2) for l in range(-1, 2)])
            elif c != ".":
                symbols.append((c, (i, j)))
            if (not c.isdigit() or j == len(l[i])) and digit[0]:
                digits.append((int(digit[0]), digit[1]))
                digit = ["", set()]
    return digits, symbols

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