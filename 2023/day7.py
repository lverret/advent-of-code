def read_txt(filename):
    return [line.rstrip('\n') for line in open(filename, 'r')]

def res(l, p, d):
    def score(s, p, d):
        t = {(1, 1): 0, (2, 1): 1, (2, 2): 2, (3, 1): 3, (3, 2): 4, (4, 1): 5, (5, 0): 6}
        p = "".join([format(t[p(s, d)], '#06b')[2:]] + [format(d[c], '#06b')[2:] for c in s[0]])
        return int(p, 2)
    l = list(map(str.split, l))
    l.sort(key=lambda x: score(x, p, d))
    return sum([int(s[1]) * (i + 1) for i, s in enumerate(l)])

def part1(l):
    def p(s, d):
        m2, m1 = sorted([s[0].count(c) for c in d])[-2:]
        return m1, m2
    d = dict(zip(["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"], range(13)))
    return res(l, p, d)

def part2(l):
    def p(s, d):
        m2, m1 = sorted([s[0].count(c) for c in d if c != "J"])[-2:]
        return m1 + s[0].count("J"), m2
    d = dict(zip(["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"], range(13)))
    return res(l, p, d)


if __name__ == "__main__":
    lines = read_txt("day7.txt")
    print(part1(lines))
    print(part2(lines))