# Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo ścieżką między v i u,
# ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych ścieżek w sensie liczby krawędzi
# wśród najkrótszych ścieżek w sensie wagowym). Podaj algorytm, który dla danego wierzchołka startowego s
# znajdzie superfajne ścieżki do pozostałych wierzchołków.


from queue import PriorityQueue

from math import inf


# Dijkstra uwzględniający liczbę odwiedzonych wierzchołków gdy długość trasy równa

def extraCoolPaths(G, s):
    n = len(G)
    dp = [inf for _ in range(n)]
    dpLength = [inf for _ in range(n)]
    dp[s] = 0

    Q = PriorityQueue()
    Q.put((dp[s], s))

    while not Q.empty():
        _, u = Q.get()

        for i in range(n):
            if G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                dpLength[i] = dpLength[u] + 1
                Q.put((dp[i], i))
            elif G[u][i] > 0 and dp[i] == dp[u] + G[u][i] and dpLength[i] > dpLength[u] + 1:
                dpLength[i] = dpLength[u] + 1

    return dp


G = [[0, 4, 4, 6, 6, 0, 0, 0, 0, 0],
     [4, 0, 2, 0, 0, 0, 0, 0, 0, 0],
     [4, 2, 0, 8, 0, 0, 0, 2, 4, 0],
     [6, 0, 8, 0, 9, 2, 0, 0, 0, 0],
     [6, 0, 0, 9, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 5, 2, 0, 0],
     [0, 0, 0, 0, 0, 5, 0, 0, 3, 2],
     [0, 0, 2, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 4, 0, 0, 0, 3, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]]

print(extraCoolPaths(G, 3))
