from itertools import product


def print_mat(m):
    s = ""
    for i in range(len(m)):
        for j in range(len(m[0])):
            s += m[i][j]
        s += "\n"
    print(s)


def pad(m):
    pad_row = [["." for _ in range(len(m))]]
    m = pad_row + m + pad_row
    for j in range(len(m)):
        m[j] = ["."] + m[j] + ["."]
    return m


def solve(m, max_iter):
    m = pad(m)
    rolls = set()
    for i in range(1, len(m) - 1):
        for j in range(1, len(m[0]) - 1):
            if m[i][j] == "@":
                rolls.add((i, j))

    rolls_rm = None
    ninit = len(rolls)
    k = 0
    while rolls_rm is None or len(rolls_rm) > 0 and k < max_iter:
        rolls_rm = set()
        for i, j in rolls:
            nrolls = 0
            for ni, nj in product([-1, 0, 1], [-1, 0, 1]):
                if ni == 0 and nj == 0:
                    continue
                if (i + ni, j + nj) in rolls:
                    nrolls += 1
            if nrolls <= 3:
                rolls_rm.add((i, j))

        rolls = rolls.difference(rolls_rm)
        k += 1

    return ninit - len(rolls)


def part1(m):
    return solve(m, max_iter=1)


def part2(m):
    return solve(m, max_iter=10000000)
