DIR = {"SO": (1, 0), "NO": (-1, 0), "WE": (0, -1), "EA": (0, 1)}
MOVE = lambda l, i, j, x: ((i + DIR[x][0], j + DIR[x][1]), l[i + DIR[x][0]][j + DIR[x][1]], INV(x))
PIPES = {
    "|": {"SO": "NO", "NO": "SO"}, 
    "-": {"WE": "EA", "EA": "WE"},
    "L": {"EA": "NO", "NO": "EA"}, 
    "J": {"WE": "NO", "NO": "WE"},
    "7": {"WE": "SO", "SO": "WE"},
    "F": {"EA": "SO", "SO": "EA"},
    ".": {},
}
def INV(x):
    if x == "SO":
        return "NO"
    elif x == "NO":
        return "SO"
    elif x == "EA":
        return "WE"
    elif x == "WE":
        return "EA"

def loop(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            yield (i, j)

def parse(l):
    l = list(map(list, l))
    l.append(["." for _ in range(len(l[0]))])
    l.insert(0, ["." for _ in range(len(l[0]))])
    for i in range(len(l)):
        l[i].append(".")
        l[i].insert(0, ".")
    return l
            
def find_cand(l):
    cand = []
    for i, j in loop(l):
        if l[i][j] == "S":
            for p, inout in PIPES.items():
                if p != "." and all(INV(out) in PIPES[MOVE(l, i, j, out)[1]] for out in inout.values()):
                    cand.append(p)
            return (i, j), cand

def propagate(l, pos, c):
    out = list(PIPES[c].values())
    pos1, c1, invout1 = MOVE(l, *pos, out[0])
    pos2, c2, invout2 = MOVE(l, *pos, out[1])
    pos_loop = set([pos, pos1, pos2])
    n = 1
    while pos1 != pos2:
        pos1, c1, invout1 = MOVE(l, *pos1, PIPES[c1][invout1])
        pos2, c2, invout2 = MOVE(l, *pos2, PIPES[c2][invout2])
        pos_loop.update([pos1, pos2])
        n += 1
    return n, pos_loop

def is_inside(l, i, j, pos_loop):
    n_cross = sum(out == "NO" for k in range(j, len(l[0])) for out in PIPES[l[i][k]].values() if (i, k) in pos_loop)
    return n_cross % 2 == 1

def count_inside(l, pos_loop):
    return sum(is_inside(l, i, j, pos_loop) for i, j in loop(l) if (i, j) not in pos_loop)

def part1(l):
    l = parse(l)
    (i, j), cand = find_cand(l)
    n, _ = propagate(l, (i, j), cand[0])
    return n

def part2(l):
    l = parse(l)
    (i, j), cand = find_cand(l)
    l[i][j] = cand[0]
    _, pos_loop = propagate(l, (i, j), cand[0])
    return count_inside(l, pos_loop)
    
    
