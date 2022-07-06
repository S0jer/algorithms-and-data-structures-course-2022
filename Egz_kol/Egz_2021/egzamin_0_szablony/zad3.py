from queue import PriorityQueue, Queue

from zad3testy import runtests
from math import inf


def jumper(G, s, w):
    # result = dijkstra_M(G, s, w)
    result = dijkstra(G, s, w)
    return result


def dijkstra(G, s, k):
    n = len(G)
    Q = Queue()
    dp = [[inf, inf] for _ in range(n)]

    dp[s] = [0, 0]
    Q.put((s, 0, inf, -1))

    while not Q.empty():
        u, boots, last, lastID = Q.get()

        for i in range(n):
            if G[u][i] > 0:
                if boots == 0 and dp[i][0] > dp[u][0] + G[u][i]:
                    dp[i][0] = dp[u][0] + G[u][i]
                    Q.put((i, 2, G[u][i], u))
                    Q.put((i, 0, -1, -1))

                elif boots == 1 and dp[i][0] > min(dp[u][1], dp[u][0]) + G[u][i]:
                    dp[i][0] = min(dp[u][1], dp[u][0]) + G[u][i]
                    Q.put((i, 0, -1, -1))

                elif boots == 2 and dp[i][1] > dp[lastID][0] + max(last, G[u][i]):
                    dp[i][1] = dp[lastID][0] + max(last, G[u][i])
                    Q.put((i, 1, -1, -1))

    return min(dp[k][0], dp[k][1])


def dijkstra_M(G, s, w):
    n = len(G)

    dp = [[inf, inf] for _ in range(n)]
    visited = [False] * n

    dp[s][0], dp[s][1] = 0, 0

    for i in range(n):

        u = min_distance(dp, visited)
        visited[u] = True

        for j in range(n):
            if dp[j][0] > dp[u][0] + G[u][j] and G[u][j] != 0 and visited[j] is False:
                dp[j][0] = dp[u][0] + G[u][j]
                for z in range(n):

                    if dp[z][1] > dp[u][0] + max(G[j][z], G[u][j]) and G[j][z] != 0 and visited[z] is False:
                        dp[z][1] = dp[u][0] + max(G[j][z], G[u][j])

            if dp[j][0] > dp[u][1] + G[u][j] and G[u][j] != 0 and visited[j] is False:
                dp[j][0] = dp[u][1] + G[u][j]

    return min(dp[w][0], dp[w][1])


def min_distance(dp, visited):
    min_w, min_idx, n = inf, 0, len(dp)

    for i in range(n):
        if dp[i][0] < min_w and visited[i] is False:
            min_w = dp[i][0]
            min_idx = i
        if dp[i][1] < min_w and visited[i] is False:
            min_w = dp[i][1]
            min_idx = i

    return min_idx


runtests(jumper)
