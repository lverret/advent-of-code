def check_invalid1(id):
    if len(id) % 2 == 1:
        return False
    else:
        sep = len(id) // 2
        first_half, second_half = id[:sep], id[sep:]
        if first_half == second_half:
            return True
        else:
            return False


def check_invalid2(id):
    i = (id + id).find(id, 1, -1)
    return False if i == -1 else True


def loop(s, check_func):
    r = 0
    for ids in s.split(","):
        first_id, last_id = ids.split("-")
        for id in range(int(first_id), int(last_id) + 1):
            r += id if check_func(str(id)) else 0
    return r


def part1(s):
    return loop(s, check_invalid1)


def part2(s):
    return loop(s, check_invalid2)
