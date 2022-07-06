from zad3testy import runtests
from queue import PriorityQueue

from math import inf


def paths(G, s, t):
    n = len(G)
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    edges = [[-1 for _ in range(n)] for _ in range(n)]
    dp = [inf for _ in range(n)]
    pSaved, minT = [], inf
    dp[s] = 0
    Q = PriorityQueue()
    Q.put((dp[s], s))

    while not Q.empty():
        _, u = Q.get()
        visited[u] = True

        for e in G[u]:
            if dp[e[0]] >= dp[u] + e[1] and visited[e[0]] is False:
                dp[e[0]] = dp[u] + e[1]
                parents[e[0]] = u
                Q.put((dp[e[0]], e[0]))

                if e[0] == t and dp[t] < minT and dp[t] != inf:
                    minT = dp[t]
                    pSaved = [parents[:]]
                elif e[0] == t and dp[t] == minT:
                    pSaved.append(parents[:])
    result = 0
    for p in pSaved:
        k = t
        while p[k] != -1:
            if edges[p[k]][k] == -1:
                edges[p[k]][k] = 1
                result += 1
            k = p[k]

    return result


runtests(paths)
