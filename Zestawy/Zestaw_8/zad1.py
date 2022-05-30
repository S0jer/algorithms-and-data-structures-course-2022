# Zadanie 1. (DFS/BFS) Proszę zaimplementować następujące algorytmy:
# 1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).
# 2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania

from collections import deque


def BFSColors(G):
    n = len(G)
    visited = [-1 for _ in range(n)]
    colors = [0 for _ in range(n)]
    Q = deque()

    visited[0] = 1
    colors[0] = 1
    check = True
    Q.append(0)

    while len(Q) > 0:
        u = Q.popleft()

        for i in range(n):
            if G[u][i] == 1 and visited[i] != 1:
                visited[i] = 1
                if colors[i] == 0:
                    colors[i] = colors[u] * (-1)
                elif colors[i] == colors[u]:
                    check = False
                Q.append(i)
            elif G[u][i] == 1 and colors[i] == colors[u]:
                check = False

    return check


def DFSColors(G, visited, u, check, colors):
    n = len(G)
    visited[u] = 1

    if colors[u] == 0:
        colors[u] = 1

    for i in range(n):
        if visited[i] != 1 and G[u][i] == 1:
            visited[i] = 1
            if colors[i] == 0:
                colors[i] = colors[u] * (-1)
            elif colors[i] == colors[u]:
                check = False
            DFSColors(G, visited, i, check, colors)

        elif G[u][i] == 1 and colors[i] == colors[u]:
            check = False

    return check


G = [[0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]

graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]]

G1 = [[0, 1, 1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 0]]

vG = [-1 for _ in range(len(G))]
vg = [-1 for _ in range(len(graph))]

print(BFSColors(graph))
print(BFSColors(G))
print()
print(DFSColors(graph, vg, 0, True, [0 for _ in range(len(graph))]))
print(DFSColors(G, vG, 0, True, [0 for _ in range(len(G))]))


def spójneSkladowe(G):
    n = len(G)
    c = [0 for _ in range(n)]
    visited = [-1 for _ in range(n)]
    cCnt = 1
    for i in range(n):
        if visited[i] == -1:
            visited, c = BFS(G, i, c, visited, cCnt)
            cCnt += 1

    return c


def BFS(G, u, c, visited, cCnt):
    n = len(G)
    c[u] = cCnt
    Q = deque()
    Q.append(u)

    while len(Q) > 0:
        u = Q.popleft()
        visited[u] = 1

        for i in range(n):
            if G[u][i] == 1 and visited[i] != 1:
                c[i] = cCnt
                Q.append(i)

    return visited, c


def spójneSkladoweDFS(G):
    n = len(G)
    c = [0 for _ in range(n)]
    visited = [-1 for _ in range(n)]
    cCnt = 1

    for i in range(n):
        if visited[i] == -1:
            visited, c = DFS(G, visited, i, c, cCnt)
            cCnt += 1

    return c


def DFS(G, visited, u, c, cCnt):
    n = len(G)
    visited[u] = 1
    c[u] = cCnt

    for i in range(n):
        if visited[i] != 1 and G[u][i] == 1:
            DFS(G, visited, i, c, cCnt)

    return visited, c


print("\n")
print(spójneSkladowe(G1))
print()
print(spójneSkladoweDFS(G1))
