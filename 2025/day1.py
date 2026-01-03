def part1(l):
    p = 50
    tmap = {"R": 1, "L": -1}
    count = 0
    for rot in l:
        turn, num = tmap[rot[0]], int(rot[1:])
        p = (p + turn * num) % 100
        if p == 0:
            count += 1
    return count


def part2(l):
    p1 = 50 + 1000000000
    tmap = {"R": 1, "L": -1}
    count = 0
    for rot in l:
        turn, num = tmap[rot[0]], int(rot[1:])
        p2 = p1 + turn * (num + 0.1)

        box1 = p1 // 100
        box2 = p2 // 100

        if p1 % 100 == 0:
            box1_list = [box1, box1 - 1]
        else:
            box1_list = [box1]

        incr = int(min([abs(box - box2) for box in box1_list]))
        count += incr

        p1 = round(p2)

    return count
