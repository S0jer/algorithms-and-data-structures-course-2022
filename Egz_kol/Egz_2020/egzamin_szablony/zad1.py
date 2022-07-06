from zad1testy import runtests
from queue import PriorityQueue
from math import inf


def islands(G, A, B):
    n = len(G)
    Q = PriorityQueue()
    dp = [inf for _ in range(n)]

    dp[A] = 0
    Q.put((dp[A], A, -1))

    while not Q.empty():
        _, u, lastT = Q.get()

        for i in range(n):
            if G[u][i] > 0 and G[u][i] != lastT and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                Q.put((dp[i], i, G[u][i]))

    if dp[B] == inf:
        return None
    return dp[B]


runtests(islands)
