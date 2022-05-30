# Zadanie 4. (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.

from collections import deque
from math import inf


def decreasingEdges(G, s, e):
    n = len(G)
    canTravel = False

    Q = deque()
    Q.append((inf, s))

    while len(Q) > 0:
        pathVal, u = Q.popleft()

        if u == e:
            canTravel = True

        for i in range(n):
            if pathVal > G[u][i] and G[u][i] > 0:
                Q.append((G[u][i], i))

    return canTravel


def decreasingEdgesDFS(G, s, e, visited, found, pathVal):
    n = len(G)
    visited[s] = 1

    for i in range(n):
        if pathVal > G[s][i] > 0 and visited[i] == -1:
            decreasingEdgesDFS(G, i, e, visited, found, G[s][i])

    if visited[e] == 1:
        return True
    return False


G = [[0, 3, 1, 2, 0, 0],
     [3, 0, 0, 0, 2, 0],
     [1, 0, 0, 2, 0, 0],
     [2, 0, 2, 0, 0, 1],
     [0, 2, 0, 0, 0, 2],
     [0, 0, 0, 1, 2, 0]]

print(decreasingEdges(G, 4, 0))
print(decreasingEdgesDFS(G, 4, 0, [-1 for _ in range(len(G))], False, inf))
print()
print(decreasingEdges(G, 0, 4))
print(decreasingEdgesDFS(G, 0, 4, [-1 for _ in range(len(G))], False, inf))
