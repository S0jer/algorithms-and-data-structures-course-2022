from zad1testy import runtests
from math import inf


def zbigniew(A):
    n = len(A)
    dp = [[[0, inf] for _ in range(1)] for _ in range(n)]
    dp[0].append([A[0], 0])


    for i in range(n):
        for z in range(len(dp[i])):
            for j in range(i + 1, min(i + dp[i][z][0] + 1, n)):
                k = j - i
                if dp[j][0][1] > dp[i][z][1] + 1:
                    dp[j][0][1] = dp[i][z][1] + 1
                    dp[j][0][0] = dp[i][z][0] - k + A[j]
                elif dp[i][z][0] - k + A[j] > dp[j][0][0] and j != n - 1:
                    dp[j].append([dp[i][z][0] - k + A[j], dp[i][z][1] + 1])

    if dp[n - 1][0][1] == inf:
        return -1

    return dp[n - 1][0][1]




runtests(zbigniew)
