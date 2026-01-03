from collections import defaultdict
from tqdm import trange


def get_hv(tiles):
    htiles = defaultdict(list)
    for k in range(1, len(tiles), 2):
        xi = tiles[k][0]
        if k + 1 == len(tiles):
            xj = tiles[0][0]
        else:
            xj = tiles[k + 1][0]
        yi = tiles[k][1]
        if xi != xj:
            htiles[yi].append((min(xj, xi), max(xi, xj)))
    vtiles = defaultdict(list)
    for k in range(0, len(tiles), 2):
        yi = tiles[k][1]
        if k + 1 == len(tiles):
            yj = tiles[0][1]
        else:
            yj = tiles[k + 1][1]
        xi = tiles[k][0]
        if yi != yj:
            vtiles[xi].append((min(yj, yi), max(yi, yj)))

    htiles = {k: htiles[k] for k in sorted(htiles)}
    vtiles = {k: vtiles[k] for k in sorted(vtiles)}
    return htiles, vtiles


def is_inside(x, y, htiles, vtiles):
    ninters = [0, 0, 0, 0]
    for row in htiles:
        for s, e in htiles[row]:
            if row <= y and s <= x <= e:
                ninters[0] += 1
            if row >= y and s <= x <= e:
                ninters[1] += 1
    for col in vtiles:
        for s, e in vtiles[col]:
            if col <= x and s <= y <= e:
                ninters[2] += 1
            if col >= x and s <= y <= e:
                ninters[3] += 1
    return all(n != 0 for n in ninters)


def part1(lines):
    tiles = [list(map(int, s.split(","))) for s in lines]
    max_area = -1
    for k in range(len(tiles)):
        ui, uj = tiles[k]
        for l in range(k + 1, len(tiles)):
            vi, vj = tiles[l]
            xmin = min(vi, ui)
            xmax = max(vi, ui)
            ymin = min(vj, uj)
            ymax = max(vj, uj)
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area > max_area:
                max_area = area
    return max_area


def part2(lines):
    tiles = [list(map(int, s.split(","))) for s in lines]
    is_inside_mem = {}
    htiles, vtiles = get_hv(tiles)
    max_area = -1
    for k in trange(len(tiles)):
        ui, uj = tiles[k]
        for l in trange(k + 1, len(tiles), leave=False):
            vi, vj = tiles[l]
            xmin = min(vi, ui)
            xmax = max(vi, ui)
            ymin = min(vj, uj)
            ymax = max(vj, uj)
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area > max_area:
                box_is_inside = True
                for xx in range(xmin, xmax):
                    if (xx, ymin) not in is_inside_mem:
                        is_inside_mem[(xx, ymin)] = is_inside(xx, ymin, htiles, vtiles)
                    if not is_inside_mem[(xx, ymin)]:
                        box_is_inside = False
                        break

                    if (xx, ymax) not in is_inside_mem:
                        is_inside_mem[(xx, ymax)] = is_inside(xx, ymax, htiles, vtiles)
                    if not is_inside_mem[(xx, ymax)]:
                        box_is_inside = False
                        break

                if box_is_inside:
                    for yy in range(ymin, ymax):
                        if (xmin, yy) not in is_inside_mem:
                            is_inside_mem[(xmin, yy)] = is_inside(
                                xmin, yy, htiles, vtiles
                            )
                        if not is_inside_mem[(xmin, yy)]:
                            box_is_inside = False
                            break

                        if (xmax, yy) not in is_inside_mem:
                            is_inside_mem[(xmax, yy)] = is_inside(
                                xmax, yy, htiles, vtiles
                            )
                        if not is_inside_mem[(xmax, yy)]:
                            box_is_inside = False
                            break

                if box_is_inside:
                    max_area = area
    return max_area
