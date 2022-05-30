# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką 1
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.


from collections import deque
from math import inf


def zeroOneEdges(G, s, t):
    n = len(G)
    Q = deque()
    distance = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]

    distance[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for i in range(n):
            if G[u][i] >= 0 and distance[i] > distance[u] + G[u][i]:
                parents[i] = u
                distance[i] = distance[u] + G[u][i]
                Q.append(i)

    return distance[t], getRoad(parents, s, t)


def getRoad(parents, s, t):
    result = [t]

    while t != s:
        t = parents[t]
        result.append(t)

    return result[::-1]


G = [[-1, 0, 1, 1, -1, -1, -1, -1, -1],
     [0, -1, -1, -1, -1, -1, -1, -1, -1],
     [1, -1, -1, 1, -1, 0, 0, 1, -1],
     [1, -1, 1, -1, 0, -1, -1, -1, -1],
     [-1, -1, -1, 0, -1, 0, -1, -1, -1],
     [-1, -1, 0, -1, 0, -1, 1, -1, 1],
     [-1, -1, 1, -1, -1, 1, -1, -1, -1],
     [-1, -1, 1, -1, -1, -1, -1, -1, 0],
     [-1, -1, -1, -1, -1, 0, -1, 0, 0]]

s = 3
t = 7

print(zeroOneEdges(G, s, t))
