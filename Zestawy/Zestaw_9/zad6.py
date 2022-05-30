# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach 1
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
# zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim poprawny).

from math import inf
from queue import PriorityQueue


def twoDrivers(G, s, k):
    dp1, road1 = dijkstry(G, s, k, 1)
    dp2, road2 = dijkstry(G, s, k, -1)

    # print(dp1)
    # print(road1)
    # print()
    # print(dp2)
    # print(road2)

    if dp1[k] > dp2[k]:
        return dp2[k], road2
    else:
        return dp1[k], road1


def dijkstry(G, s, k, state):
    n = len(G)
    dp = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    Q = PriorityQueue()
    visited[s] = True
    dp[s] = 0
    Q.put((0, s, state, [s]))

    while not Q.empty():
        _, u, stan, road = Q.get()
        visited[u] = True

        for i in range(n):
            if G[u][i] > 0 and stan == 1 and dp[i] > dp[u] + G[u][i] and visited[i] is False:
                dp[i] = dp[u] + G[u][i]
                parents[i] = u
                Q.put((dp[i], i, -1 * stan, road + [i]))
            elif G[u][i] > 0 and stan == -1 and dp[i] > dp[u] and visited[i] is False:
                dp[i] = dp[u]
                parents[i] = u
                Q.put((dp[i], i, -1 * stan, road + [i]))

        if u == k:
            return dp, road

    return dp, parents


G1 = [[-1, 4, 3, 3, -1],
      [4, -1, 7, -1, -1],
      [3, 7, -1, 4, 2],
      [3, -1, 4, -1, 5],
      [-1, -1, 2, 5, -1]]
# 0  1   2   3   4   5   6   7  8
G2 = [[-1, 2, -1, -1, -1, -1, -1, -1, 5],
      [-1, -1, 1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, 3, -1, -1, 1, -1, -1],
      [-1, -1, -1, -1, 1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, 4, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, 1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, 1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, 4, -1]]

G3 = [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3, 0, 0, 0, 0, 0],
      [0, 0, 0, 3, 0, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 2, 0, 4, 0, 0, 0],
      [0, 0, 0, 0, 0, 4, 0, 3, 0, 0],
      [0, 0, 0, 0, 0, 0, 3, 0, 3, 0],
      [0, 0, 0, 0, 0, 0, 0, 3, 0, 2],
      [0, 0, 0, 0, 0, 0, 0, 0, 2, 0]]

print(twoDrivers(G2, 0, 6))
