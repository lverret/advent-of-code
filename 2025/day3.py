def argmax(values):
    def argmax_func(pairs):
        return max(pairs, key=lambda x: x[1])[0]

    return argmax_func(enumerate(values))


def max_bat(s, n):
    """
    max_bat(s, n) = max(concat(max_bat(s, n-1), k) for k in s)
    """
    if n == 1:
        ind = argmax(s)
        return [ind], s[ind]
    ind, _ = max_bat(s, n - 1)
    ind_max = "".join([str(s[j]) for j in ind])
    new_s = []
    j = 0
    for i in range(len(s)):
        if j < len(ind) and i == ind[j]:
            j += 1
            new_s.append(-1)
        else:
            new_s.append(int(ind_max[:j] + str(s[i]) + ind_max[j:]))
    new_ind = argmax(new_s)
    return sorted(ind + [new_ind]), new_s[new_ind]


def loop(m, n):
    r = 0
    for row in m:
        row = list(map(int, row))
        _, rr = max_bat(row, n)
        r += rr
    return r


def part1(m):
    return loop(m, n=2)


def part2(m):
    return loop(m, n=12)
