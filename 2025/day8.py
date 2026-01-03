import numpy as np

from collections import defaultdict
from copy import deepcopy


def get_matrices(l):
    mat = []
    for s in l:
        mat.append([int(ss) for ss in s.split(",")])
    mat = np.array(mat)
    dist = np.linalg.norm(mat[None] - mat[:, None], axis=-1)
    dist[dist == 0] = np.inf
    return mat, dist


def dfs(graph, node, connected):
    for neigh in graph[node]:
        if neigh not in connected:
            connected.add(neigh)
            dfs(graph, neigh, connected)


def find_circuits(graph, n):
    circuits = []
    for node in graph:
        connected = set()
        dfs(graph, node, connected)
        if connected not in circuits:
            circuits.append(connected)
    for node in range(n):
        if all(node not in s for s in circuits):
            circuits.append({node})
    return circuits


def connect_closest(dist_mat, niter):
    dist_mat_copy = deepcopy(dist_mat)
    graph = defaultdict(list)
    for _ in range(niter):
        idx = np.unravel_index(np.argmin(dist_mat_copy), dist_mat_copy.shape)
        i, j = idx
        dist_mat_copy[i, j] = np.inf
        dist_mat_copy[j, i] = np.inf
        graph[i].append(j)
        graph[j].append(i)
    last = (i, j)
    return graph, last


def part1(l):
    _, dist = get_matrices(l)
    n = len(dist)
    graph, _ = connect_closest(dist, niter=1000)
    circuits = find_circuits(graph, n)
    largest = sorted(circuits, key=len, reverse=True)[:3]
    return np.prod(list(map(len, largest)))


def part2(l):
    mat, dist = get_matrices(l)
    n = len(dist)
    # find correct iter by binary search
    minrange, maxrange = (1000, 6000)
    while maxrange - minrange > 1:
        niter = (maxrange + minrange) // 2
        graph, _ = connect_closest(dist, niter=niter)
        circuits = find_circuits(graph, n)
        if len(circuits) > 1:
            minrange = niter
        else:
            maxrange = niter
    # get last edge that connect everything
    graph, (i, j) = connect_closest(dist, niter=minrange)
    circuits = find_circuits(graph, n)
    if len(circuits) > 1:
        graph, (i, j) = connect_closest(dist, niter=maxrange)
        circuits = find_circuits(graph, n)
    return mat[i][0] * mat[j][0]
