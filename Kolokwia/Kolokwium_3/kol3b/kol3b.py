from math import inf

from kol3btesty import runtests
from queue import PriorityQueue


def airports(G, A, s, t):
    n = len(G)
    for i in range(n):
        G[i] += [(n, A[i])]
    A.append(0)
    G.append([])

    for j in range(n + 1):
        G[n].append((j, A[j]))

    dp = [inf for _ in range(n + 1)]
    Q = PriorityQueue()

    dp[s] = 0
    Q.put((dp[s], s))

    while not Q.empty():
        _, u = Q.get()
        for i, l in G[u]:
            if dp[i] > dp[u] + l:
                dp[i] = dp[u] + l
                Q.put((dp[i], i))

    return dp[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
