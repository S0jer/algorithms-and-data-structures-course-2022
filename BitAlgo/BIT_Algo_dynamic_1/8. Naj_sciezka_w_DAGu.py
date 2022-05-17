# Zadanie 8
# Znajdź długość najdłuższej ścieżki prostej w acyklicznym grafie skierowanym (DAGu).

from math import inf


def longestPathInDag(G):
    n = len(G)
    dist = [-inf for _ in range(n)]
    d = tplS(G)

    dist[d[-1]] = 0

    while len(d) > 0:
        u = d[-1]
        del d[-1]

        if dist[u] != -inf:
            for i in G[u]:
                if dist[i] < dist[u] + 1:
                    dist[i] = dist[u] + 1

    print(dist)
    return max(dist)


def tplS(G):
    n = len(G)
    v = [-1 for _ in range(n)]
    delete = []

    i = 0
    while i != n:
        delete, v = visitTpk(G, i, v, delete)
        while i != n and v[i] != -1:
            i += 1

    return delete


def visitTpk(G, u, v, delete):
    v[u] = 1

    for i in G[u]:
        if v[i] != 1:
            visitTpk(G, i, v, delete)

    delete.append(u)

    return delete, v


graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]

print(longestPathInDag(graph))
