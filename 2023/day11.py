def loop(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            yield i, j

def expand(l, rate):
    l = list(map(list, l))
    d = [
        [rate-1 if all(l[i][k] != "#" for k in range(len(l[0]))) or 
                   all(l[k][j] != "#" for k in range(len(l))) 
                else 0
        for j in range(len(l[0]))] 
        for i in range(len(l))
    ]
    di = [[0 for _ in range(len(l[0]))] for _ in range(len(l))]
    dj = [[0 for _ in range(len(l[0]))] for _ in range(len(l))]
    for i, j in loop(d):
        if i != 0:
            di[i][j] += di[i-1][j] + d[i-1][j]
        if j != 0:
            dj[i][j] += dj[i][j-1] + d[i][j-1]
    return l, di, dj

def n_sp(l, rate):
    l, di, dj = expand(l, rate)
    g = set((i + di[i][j], j + dj[i][j]) for i, j in loop(l) if l[i][j] == "#")
    r = int(sum(abs(p[0] - q[0]) + abs(p[1] - q[1]) for p in g for q in g if q != p) / 2)
    return r

def part1(l):
    return n_sp(l, rate=2)

def part2(l):
    return n_sp(l, rate=1000000)