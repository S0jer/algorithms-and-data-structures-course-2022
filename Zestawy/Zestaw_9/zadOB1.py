# Zadanie 1. Proszę zaimplementować algorytm Dijkstry (dla wybranej przez prowadzącego reprezentacji grafu).

from queue import PriorityQueue
from collections import deque
from math import inf


def dijkstra(G, s):
    n = len(G)
    dp = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    Q = deque()  # Q1 = PriorityQueue()
    Q.append(s)  # Q1.put(s)
    dp[s] = 0

    while len(Q) > 0:  # while not Q1.empty():
        u = Q.popleft()  # Q.get()

        for i in range(n):
            if G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                parents[i] = u
                Q.append(i)

    return dp, parents


def dijkstraSquare(G, s):
    n = len(G)

    dp = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    dp[s] = 0

    for i in range(n):

        u = minDist(dp, visited)
        visited[u] = True

        for j in range(n):
            if dp[j] > dp[u] + G[u][j] and G[u][j] > 0 and visited[j] is False:
                dp[j] = dp[u] + G[u][j]
                parents[j] = u

    return dp, parents


def minDist(dp, visited):
    minW, minIdx, n = inf, 0, len(dp)

    for i in range(n):
        if dp[i] < minW and visited[i] is False:
            minW = dp[i]
            minIdx = i

    return minIdx


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

print(dijkstra(G, 3))
print(dijkstraSquare(G, 3))
