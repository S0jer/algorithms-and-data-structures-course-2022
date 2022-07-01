# Dany jest graf ważony  G, oraz drzewo rozpinające T zawierające wierzchołek s.
# Podaj algorytm, który sprawdzi, czy T jest drzewem najkrótszych ścieżek od wierzchołka s.


# Dla krawędzi nie należących do T sprawdzamy czy wystąpi relaksacja, jeśli tak to zwracamy False
from math import inf
from queue import PriorityQueue


def spanningTree(G, T, s):
    n = len(G)
    edges = []
    dp = dijkstra(T, s)
    for i in range(n):
        for j in range(n):
            if G[i][j] > 0 and T[i][j] == 0:
                edges.append(((i, j), G[i][j]))

    for e in edges:
        i = e[0][0]
        j = e[0][1]
        cost = e[1]
        if dp[i] > dp[j] + cost or dp[j] > dp[i] + cost:
            return False

    return True


def dijkstra(T, s):
    n = len(T)
    dp = [inf for _ in range(n)]
    Q = PriorityQueue()

    dp[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if T[u][i] > 0 and dp[i] > dp[u] + T[u][i]:
                dp[i] = dp[u] + T[u][i]
                Q.put(i)

    return dp
