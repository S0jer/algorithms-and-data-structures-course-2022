# Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
# do wskazanego wierzchołka.

from math import inf
from collections import deque


def dijkstra(graph, s, e):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    distance[s] = 0

    Q = deque()
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for i in range(n):
            if distance[u] + graph[u][i] < distance[i] and graph[u][i] > 0:
                distance[i] = graph[u][i] + distance[u]
                parents[i] = u
                Q.append(i)

    result = getRoad(parents, e)

    return result


def getRoad(parents, e):
    add = parents[e]
    result = []
    while add != -1:
        result.append(add)
        add = parents[add]

    return result[::-1]


G = [[0, 1, 5, 0, 0],
     [1, 0, 2, 7, 8],
     [5, 2, 0, 0, 3],
     [0, 7, 0, 0, 1],
     [0, 8, 3, 1, 0]]

G_ns = [[0, 1, 5, 0, 0],
        [1, 0, 2, 7, 8],
        [5, 2, 0, 0, 3],
        [0, 7, 0, 0, 1],
        [0, 8, 3, 1, 0]]

print(dijkstra(G, 0, 3))
