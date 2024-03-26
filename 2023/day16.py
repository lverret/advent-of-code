MVIDX = {"r": (0, 1), "l": (0, -1), "u": (-1, 0), "d": (1, 0)}

def parse(l):
    return list(map(list, l))

def cast_beam(dir, pos, l, e, f):
    i, j = pos

    if 0 <= i < len(l) and 0 <= j < len(l[i]):
        e[i][j] = True
        if dir in f[i][j]:
            return
        else:
            f[i][j].add(dir)

    i += MVIDX[dir][0]
    j += MVIDX[dir][1]

    while 0 <= i < len(l) and 0 <= j < len(l[i]) and l[i][j] == ".":
        e[i][j] = True
        i += MVIDX[dir][0]
        j += MVIDX[dir][1]

    if not (0 <= i < len(l) and 0 <= j < len(l[i])):
        return
    
    if l[i][j] == "|": 
        if dir in ["l", "r"]:
            cast_beam("u", (i, j), l, e, f)
            cast_beam("d", (i, j), l, e, f)
        else:
            cast_beam(dir, (i, j), l, e, f)
    elif l[i][j] == "-":
        if dir in ["u", "d"]:
            cast_beam("l", (i, j), l, e, f)
            cast_beam("r", (i, j), l, e, f)
        else:
            cast_beam(dir, (i, j), l, e, f)
    elif l[i][j] == "/":
        if dir == "r":
            cast_beam("u", (i, j), l, e, f)
        if dir == "l":
            cast_beam("d", (i, j), l, e, f)
        if dir == "u":
            cast_beam("r", (i, j), l, e, f)
        if dir == "d":
            cast_beam("l", (i, j), l, e, f)
    elif l[i][j] == "\\":
        if dir == "r":
            cast_beam("d", (i, j), l, e, f)
        if dir == "l":
            cast_beam("u", (i, j), l, e, f)
        if dir == "u":
            cast_beam("l", (i, j), l, e, f)
        if dir == "d":
            cast_beam("r", (i, j), l, e, f)
    
def count_energized(dir, pos, l):
    e = [[False for _ in range(len(l[0]))] for _ in range(len(l))]
    f = [[set() for _ in range(len(l[0]))] for _ in range(len(l))]
    cast_beam(dir, pos, l, e, f)
    return sum(sum(x) for x in e)

def part1(l):
    l = parse(l)
    return count_energized("r", (0, -1), l)

def part2(l):
    l = parse(l)
    maxi = 0
    for i in range(len(l)):
        maxi = max(maxi, count_energized("r", (i, -1), l))
        maxi = max(maxi, count_energized("l", (i, len(l)), l))
    for j in range(len(l[0])):
        maxi = max(maxi, count_energized("d", (-1, j), l))
        maxi = max(maxi, count_energized("u", (len(l[0]), j), l))
    return maxi

