from queue import PriorityQueue
from math import inf


def islands(G, s, t):
    n = len(G)
    dp = [inf for _ in range(n)]
    Q = PriorityQueue()

    dp[s] = 0
    Q.put((dp[s], s, 0))

    while not Q.empty():
        _, u, lastT = Q.get()

        for i in range(n):
            if G[u][i] > 0 and G[u][i] != lastT and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                Q.put((dp[i], i, G[u][i]))

    return dp[t]


G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]

print(islands(G, 5, 2))
