from collections import defaultdict



def split(l):
    m, n = [], []
    for s in l:
        if len(s.rstrip()) == 0:
            m.append(n)
            n = []
        else:
            n.append(s)
    m.append(n)
    return m

def parse(l):
    h, v = defaultdict(list), defaultdict(list)
    tl = list(map("".join, map(list, zip(*l))))
    he = [0, -1], [1, -1], [l[0], l[-1]]
    ve = [0, -1], [1, -1], [tl[0], tl[-1]]
    for i, s in enumerate(l):
        h[s].append(i)
    for j, s in enumerate(tl):
        v[s].append(j)
    return he, {k: v for k,v in h.items() if len(v) > 1}, ve, {k: v for k,v in v.items() if len(v) > 1}

def check(x, a, b, d):
    r = True
    while not (d == 1 and a > b or d == -1 and b > a):
        if a == b or all(a not in xx or b not in xx for xx in x.values()):
            r = False
            break
        a += d
        b -= d
    return r

def get_numbers(s):
    he, h, ve, v = parse(s)
    t = []
    for xe, x, coeff in zip([ve, he], [v, h], [1, 100]):
        for idx, d, e in zip(*xe):
            if e in x:
                a = x[e]
                for y in a:
                    if y != a[idx]:
                        if check(x, a[idx], y, d):
                            t.append((a[idx] + d * abs((a[idx] - y) // 2)) * coeff)
    return t

def part1(l):
    l = split(l)
    return sum(get_numbers(s)[0] for s in l)

def part2(l):
    switch = {"#": ".", ".": "#"}
    l = split(l)
    r = 0
    for s in l:
        found = False
        o = get_numbers(s)
        for i in range(len(s)):
            for j in range(len(s[0])):
                s[i] = s[i][0:j] + switch[s[i][j]] + s[i][j+1:]
                t = get_numbers(s)
                s[i] = s[i][0:j] + switch[s[i][j]] + s[i][j+1:]
                if len(t) > 0 and t != o:
                    assert len(t) == 1 or len(t) == 2
                    r += t[0] if t[0] != o[0] or len(t) == 1 else t[1]
                    found = True
                    break
            if found:
                break
    return r

