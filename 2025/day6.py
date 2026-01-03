def apply_op(a, b, op):
    if op == "*":
        return a * b
    else:
        return a + b


def part1(l):
    ops = l[-1].split()
    res = [1 if ops[k] == "*" else 0 for k in range(len(l[0].split()))]
    for s in l[:-1]:
        s = list(map(int, s.split()))
        for i in range(len(s)):
            res[i] = apply_op(res[i], s[i], ops[i])
    return sum(res)


def part2(l):
    ops = l[-1].split()
    res = [1 if ops[k] == "*" else 0 for k in range(len(l[0].split()))]
    k = len(ops) - 1
    for j in range(len(l[0]) - 1, -1, -1):
        n = ""
        for i in range(len(l) - 1):
            n += l[i][j]
        if n.strip() != "":
            res[k] = apply_op(res[k], int(n), ops[k])
        else:
            k -= 1
    return sum(res)
