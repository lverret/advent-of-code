from bisect import bisect_left
from copy import deepcopy


def part1(l):
    i = l.index("")
    ranges = [list(map(int, r.split("-"))) for r in l[:i]]
    ingrs = list(map(int, l[i + 1 :]))
    nfresh = 0
    for ingr in ingrs:
        fresh = False
        for range in ranges:
            if range[0] <= ingr <= range[1]:
                fresh = True
                break
        if fresh:
            nfresh += 1
    return nfresh


def part2(l):
    i = l.index("")
    ranges = [list(map(int, r.split("-"))) for r in l[:i]]
    new_ranges = []

    for range_ in ranges:
        sincl = bisect_left(new_ranges, range_[0])
        eincl = bisect_left(new_ranges, range_[1])

        if sincl == eincl and sincl % 2 == 0 and eincl % 2 == 0:
            new_ranges.insert(sincl, range_[1])
            new_ranges.insert(sincl, range_[0])
        elif sincl % 2 == 1 and eincl % 2 == 0:
            del new_ranges[sincl:eincl]
            new_ranges.insert(sincl, range_[1])
        elif sincl % 2 == 0 and eincl % 2 == 1:
            del new_ranges[sincl:eincl]
            new_ranges.insert(sincl, range_[0])
        elif sincl % 2 == 1 and eincl % 2 == 1:
            del new_ranges[sincl:eincl]
        else:
            del new_ranges[sincl:eincl]
            new_ranges.insert(sincl, range_[1])
            new_ranges.insert(sincl, range_[0])

        ok = False
        while not ok:
            new_ranges_clean = deepcopy(new_ranges)
            for i in range(1, len(new_ranges) - 1, 2):
                if new_ranges[i] == new_ranges[i + 1]:
                    del new_ranges_clean[i : i + 2]
            new_ranges = new_ranges_clean
            ok = all(
                new_ranges[i] != new_ranges[i + 1]
                for i in range(1, len(new_ranges) - 1, 2)
            )

    return sum(
        new_ranges[i + 1] - new_ranges[i] + 1 for i in range(0, len(new_ranges), 2)
    )
