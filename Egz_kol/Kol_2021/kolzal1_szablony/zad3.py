from zad3testy import runtests
from math import inf


def iamlate(T, V, q, l):
    T.append(l)
    V.append(0)
    n = len(T)
    dp = [[inf for _ in range(n)] for _ in range(q + 1)]
    parents = [[[] for _ in range(n)] for _ in range(q + 1)]

    for j in range(1, q + 1):
        dp[min(j, V[0])][0] = 1

    for i in range(n - 1):
        for j in range(q, -1, -1):
            if dp[j][i] != inf:
                idx = i + 1
                while idx < n and j - abs(T[idx] - T[i]) >= 0:
                    f = j - abs(T[idx] - T[i])
                    af = min(f + V[idx], q)

                    if dp[f][idx] > dp[j][i]:
                        dp[f][idx] = dp[j][i]
                        parents[f][idx] = parents[j][i] + [i]

                    if dp[af][idx] > dp[j][i] + 1:
                        dp[af][idx] = dp[j][i] + 1
                        parents[af][idx] = parents[j][i] + [i]

                    idx += 1

    result = inf
    xId = 0
    for j in range(q + 1):
        if dp[j][n - 1] < result:
            result = dp[j][n - 1]
            xId = j

    return parents[xId][n - 1]


runtests(iamlate)
