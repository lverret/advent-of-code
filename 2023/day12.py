
def generate_blocks(g):
    return ["#" * int(x) + "." for x in g.split(",")], sum([int(x) + 1 for x in g.split(",")])

def get_hash(blocks, s):
    return "".join(blocks)+ "," +s

def narr(blocks, s, remspace, intres):
    if len(blocks) == 0 or s == "": # no blocks left or end of string
        return 1 if "#" not in s and len(blocks) == 0 else 0
    na, j, b = 0, 0, blocks[0]
    while s[j-1] != "#" and j <= len(s) - len(b): # while don't see a # and not end of string
        match = all(b[i] == s[j+i] for i in range(len(b)) if s[j+i] != "?")
        if match and len(s) >= remspace:
            hash = get_hash(blocks[1:], s[j+len(b):])
            if hash not in intres:
                intres[hash] = narr(blocks[1:], s[j+len(b):], remspace - len(b), intres) # place block
            na += intres[hash]
        j += 1
    return na

def count_arr(l, k):
    r = []
    l = list(map(str.split, l))
    for s, g in l:
        intres = {}
        s, g = "?".join([s] * k) + ".", ",".join([g] * k)
        blocks, remspace = generate_blocks(g)
        t = narr(blocks, s, remspace, intres)
        r.append(t)
    return r

def part1(l):
    return sum(count_arr(l, k=1))
  
def part2(l):
    return sum(count_arr(l, k=5))


