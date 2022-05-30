# Zadanie 2. Proszę zaimplementować wybrany przez siebie algorytm obliczania minimalnego
# drzewa rozpinającego dla wybranej przez prowadzącego reprezentacji grafu.
from math import inf
from queue import PriorityQueue


def kruskal(G):
    n = len(G)
    E, A = [], []

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                E.append(((i, j), G[i][j]))
    E.sort(key=lambda x: x[1])

    m = len(E)
    parents = [i for i in range(m)]
    rank = [0 for _ in range(m)]

    for i in range(m):
        if find(E[i][0][0], parents) != find(E[i][0][1], parents):
            union(E[i][0][0], E[i][0][1], parents, rank)
            A.append(E[i][0])

    return A


def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)

    return parents[x]


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y:
        return

    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def prim(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    weights = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    weights[s] = 0

    Q = PriorityQueue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        visited[u] = True

        for i in range(n):
            if 0 < G[u][i] <= weights[i] and visited[i] is False:
                weights[i] = G[u][i]
                parents[i] = u
                Q.put(i)

    edges = [(parents[i], i) for i in range(1, len(parents))]

    return edges


G = [[0, 1, 5, 0, 0],
     [1, 0, 2, 7, 8],
     [5, 2, 0, 0, 3],
     [0, 7, 0, 0, 1],
     [0, 8, 3, 1, 0]]

G1 = [[0, 2, 0, 6, 0],
      [2, 0, 3, 8, 5],
      [0, 3, 0, 0, 7],
      [6, 8, 0, 0, 9],
      [0, 5, 7, 9, 0]]

print(kruskal(G1))
print(prim(G1, 0))
