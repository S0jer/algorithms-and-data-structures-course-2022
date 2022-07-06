from zad1testy import runtests
from collections import deque

from math import inf


def best_root(L):
    n = len(L)
    rootValue = [0 for _ in range(n)]

    for i in range(n):
        rootValue[i] = max(BFS(L, i))

    rId, result = -1, inf

    for j in range(n):
        if rootValue[j] < result:
            result = rootValue[j]
            rId = j

    return rId


def BFS(G, s):
    n = len(G)
    Q = deque()
    dp = [inf for _ in range(n)]
    visited = [-1] * n

    dp[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        visited[u] = 1

        for e in G[u]:
            if visited[e] == -1:
                dp[e] = dp[u] + 1
                Q.append(e)

    return dp


runtests(best_root)
