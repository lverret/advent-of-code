import re

def parse(l):
    return l[0].split(",")

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

def part1(l):
    return sum(hash(s) for s in parse(l))

def part2(l):
    boxes = [{} for _ in range(256)]
    for s in parse(l):
        lab, fl = re.findall("(.*)[-=](\d*)", s)[0]
        ibox = hash(lab)
        if fl:
            boxes[ibox][lab] = int(fl)
        else:
            if lab in boxes[ibox]:
                del boxes[ibox][lab]
    return sum([(i + 1) * (j + 1) * fl for i, box in enumerate(boxes) for j, fl in enumerate(box.values())])