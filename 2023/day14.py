
from copy import deepcopy

def parse(l):
   return list(map(list, l))

def total_load(l):
    l.insert(0, ["#" for _ in range(len(l[0]))])
    r = 0
    for j in range(len(l[0])):
        s = []
        for i in range(len(l)):
            if l[i][j] == "#":
                s.append(0)
            elif l[i][j] == "O":
                a = len(l) - i
                s[-1] += a
        r += sum(s)
    return r

def get_positions(l):
    new_pos = {d: [[None for _ in range(len(l[0]))] for _ in range(len(l))] for d in ["no", "so", "ea", "we"]}
    for i in range(len(l)):
        k = [0]
        for j in range(len(l[i])):
            if l[i][j] != "#":
                new_pos["we"][i][j] = ([i], k)
            else:
                k = [j + 1]
    for i in range(len(l)):
        k = [len(l[i]) - 1]
        for j in range(len(l[i])-1, -1, -1):
            if l[i][j] != "#":
                new_pos["ea"][i][j] = ([i], k)
            else:
                k = [j - 1]
    for j in range(len(l[0])):
        k = [0]
        for i in range(len(l)):
            if l[i][j] != "#":
                new_pos["no"][i][j] = (k, [j])
            else:
                k = [i + 1]
    for j in range(len(l[0])):
        k = [len(l[i]) - 1]
        for i in range(len(l)-1, -1, -1):
            if l[i][j] != "#":
                new_pos["so"][i][j] = (k, [j])
            else:
                k = [i - 1]
    pos = {}
    for j in range(len(l[0])):
        for i in range(len(l)-1, -1, -1):
            if l[i][j] == "O":
                pos[len(pos) + 1] = (i, j)
    return pos, new_pos

def print_blocks(l, pos):
    s = ""
    a = [[None for _ in range(len(l[0]))] for _ in range(len(l))]
    for i in range(len(l)):
        for j in range(len(l[0])):
            found = False
            for r, (x, y) in pos.items():
                if i == x and j == y:
                    s += "O"
                    found = True
                    break
                
            if l[i][j] == "#":
                s += "#"
            elif not found:
                s += "."

            a[i][j] = s[-1]

            if found:
                continue

        s += "\n"
    return a

def move(d, pos, new_pos):
    for r, (k1, k2) in pos.items():
        npos = new_pos[d][k1][k2]
        pos[r] = (npos[0][0], npos[1][0])
        if d == "no":
            npos[0][0] += 1
        if d == "so":
            npos[0][0] -= 1
        if d == "we":
            npos[1][0] += 1
        if d == "ea":
            npos[1][0] -= 1
    return pos


def part1(l):
    l = parse(l)
    pos, new_pos = get_positions(l)
    pos = move("no", pos, new_pos)
    return total_load(print_blocks(l, pos))


def part2(l):
    l = parse(l)
    pos, new_pos = get_positions(l)
    for it in range(1000):
        for d in ["no", "we", "so", "ea"]:
            pos = move(d, pos, deepcopy(new_pos))

        print(f"{it} total load:", total_load(print_blocks(l, pos)))
