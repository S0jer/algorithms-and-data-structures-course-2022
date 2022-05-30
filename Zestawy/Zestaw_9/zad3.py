# Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?


from collections import deque
from math import inf


# Using Dijsktra
def shortestPaths(G, s):
    n = len(G)
    dp = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    dp[s] = 0
    Q = deque()
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for i in range(n):
            if G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                parents[i] = u
                Q.append(i)

    return dp


G = [[0, 4, 4, 6, 6],
     [4, 0, 2, 0, 0],
     [4, 2, 0, 8, 0],
     [6, 0, 8, 0, 9],
     [6, 0, 0, 9, 0]]

print(shortestPaths(G, 1))

# Another approach is to use topological sort and then by it's order calculate minimal distance to every
# vertex from the one we started
