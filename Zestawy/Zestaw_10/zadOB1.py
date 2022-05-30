# Zadanie 1. (malejące krawędzie, c.d.) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach
# o malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).

from math import inf
from queue import PriorityQueue


def descendingEdges(G, s, k):
    n = len(G)
    Q = PriorityQueue()
    dp = [inf for _ in range(n)]
    dp[s] = 0
    Q.put((inf, s))

    while not Q.empty():
        lastEdge, u = Q.get()

        for i in range(n):
            if lastEdge > G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                Q.put((G[u][i], i))

    return dp[k]


G = [[0, 2, 0, 0, 0, 4, 0, 0, 2, 0],
     [2, 0, 0, 9, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 5, 0, 0, 0, 0, 0, 3],
     [0, 9, 5, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 3, 0, 0],
     [4, 0, 0, 0, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
     [0, 0, 0, 0, 3, 0, 2, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
     [0, 0, 3, 0, 0, 0, 0, 0, 2, 0]]

print(descendingEdges(G, 3, 7))
print(descendingEdges(G, 3, 8))
