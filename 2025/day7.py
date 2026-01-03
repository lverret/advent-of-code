def dfs1(m, i, j, s):
    if i == len(m):
        return
    if m[i][j] == "^":
        s.add((i, j))
        if (i, j - 2) not in s:
            dfs1(m, i, j - 1, s)
        dfs1(m, i, j + 1, s)
    else:
        dfs1(m, i + 1, j, s)


def dfs2(m, i, j, s):
    if i == len(m):
        return 1

    if m[i][j] == "^":
        if (i, j - 1) in s:
            nleft = s[(i, j - 1)]
        else:
            nleft = dfs2(m, i, j - 1, s)

        if (i, j + 1) in s:
            nright = s[(i, j + 1)]
        else:
            nright = dfs2(m, i, j + 1, s)

        s[(i, j)] = nleft + nright
    else:
        s[(i, j)] = dfs2(m, i + 1, j, s)

    return s[(i, j)]


def part1(m):
    j = m[0].index("S")
    s = set()
    dfs1(m, 0, j, s)
    return len(s)


def part2(m):
    j = m[0].index("S")
    s = {}
    dfs2(m, 0, j, s)
    return s[(0, j)]
