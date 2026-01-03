import numpy as np

from collections import deque
from copy import deepcopy
from scipy.optimize import linprog

MAP = {"#": True, ".": False}


def parse(machine):
    machine = machine.split()
    target = machine.pop(0)
    target = [MAP[t] for t in target if t in MAP]
    joltage = [int(m) for m in machine.pop(-1)[1:-1].split(",")]
    buttons = [tuple(map(int, m[1:-1].split(","))) for m in machine]
    return target, buttons, joltage


def apply(node, button):
    new_node = deepcopy(node)
    for switch in button:
        new_node[switch] = not node[switch]
    return new_node


def count(node, button):
    new_node = deepcopy(node)
    for switch in button:
        new_node[switch] += 1
    return new_node


def is_valid(node, target):
    return all(node[k] <= target[k] for k in range(len(node)))


def bfs(neighbors, start, target):
    visited = []
    queue = deque([start])
    levels = deque([0])
    while (level := levels.popleft()) is not None and (
        node := queue.popleft()
    ) != target:
        if node not in visited:
            visited.append(node)
            for neighbor in neighbors:
                if (new_node := apply(node, neighbor)) not in visited:
                    queue.append(new_node)
                    levels.append(level + 1)
    return level


def bfs2(neighbors, start, target):
    visited = []
    queue = deque([start])
    levels = deque([0])
    k = 0
    while (level := levels.popleft()) is not None and (
        node := queue.popleft()
    ) != target:
        k += 1
        if node not in visited:
            visited.append(node)
            for neighbor in neighbors:
                if (new_node := count(node, neighbor)) not in visited and is_valid(
                    new_node, target
                ):
                    queue.append(new_node)
                    levels.append(level + 1)
    return level


def part1(l):
    npresses = 0
    for machine in l:
        target, buttons, _ = parse(machine)
        npresses += bfs(buttons, [False] * len(target), target)
    return npresses


def part2(l):
    npresses = 0
    for machine in l:
        _, buttons, joltage = parse(machine)
        A = np.zeros((len(joltage), len(buttons)), dtype=int)
        for j, ii in enumerate(buttons):
            for i in ii:
                A[i, j] = 1
        b = np.array([joltage]).T[:, 0]
        c = np.ones(A.shape[1])
        x = linprog(c=c, A_eq=A, b_eq=b, integrality=1)["x"]
        assert np.all(A.dot(x) - b == 0)
        npresses += np.round(x).astype(int).sum()
    return npresses
