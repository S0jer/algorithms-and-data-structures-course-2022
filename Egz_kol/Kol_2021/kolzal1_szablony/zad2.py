from zad2testy import runtests
from queue import PriorityQueue

from math import inf


def breaking(G):
    n = len(G)
    arct, bridges = DFSB(G)

    indexes = PriorityQueue()
    for i in range(n):
        if arct[i] == 1:
            indexes.put((-1 * bridges[i], i))

    if indexes.empty():
        return None

    max, u = indexes.get()
    rIdx, result = -1, 0
    max *= -1

    while True:
        visited = [-1 for _ in range(n)]
        cnt = 0
        GG = G[::]

        for i in range(n):
            GG[i][u] = 0
            GG[u][i] = 0

        for j in range(n):
            if visited[j] == -1:
                DFS(GG, j, visited)
                cnt += 1
        if cnt > result:
            result = cnt
            rIdx = u

        if indexes.empty():
            break

        toCheck, u = indexes.get()
        toCheck *= -1
        if toCheck < max:
            break

    if result == 1:
        return None

    return rIdx


def DFS(G, u, visited):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if G[u][i] > 0 and visited[i] == -1:
            DFS(G, i, visited)


def DFSB(G):
    n = len(G)
    visited = [-1 for _ in range(n)]
    d = [inf for _ in range(n)]
    low = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    arct = [-1 for _ in range(n)]
    bridges = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == -1:
            DFSBridge(G, i, visited, d, 1, low, parents, arct)

    for i in range(n):
        if low[i] == d[i] and parents[i] != -1:
            bridges[parents[i]] += 1
            bridges[i] += 1

    return arct, bridges


def DFSBridge(G, u, visited, d, dNum, low, parents, arct):
    n = len(G)
    visited[u], d[u], low[u] = 1, dNum, dNum
    child = 0

    for i in range(n):
        if visited[i] == 1 and G[u][i] == 1 and i != parents[u]:
            low[u] = min(d[u], d[i])

        if G[u][i] > 0 and visited[i] == -1:
            child += 1
            parents[i] = u
            DFSBridge(G, i, visited, d, dNum + 1, low, parents, arct)

            if parents[u] == -1 and child > 1:
                arct[u] = 1
            if parents[u] != -1 and low[i] >= d[u]:
                arct[u] = True

    for i in range(n):
        if visited[i] == 1 and G[u][i] == 1 and i != parents[u]:
            low[u] = min(low[u], low[i])


runtests(breaking)
