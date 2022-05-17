from math import inf


def ksuma(T, k):
    n = len(T)
    dp = [number for number in T]
    dp[0] = T[0]

    for i in range(n):
        if i - k >= 0:
            dp[i] = min(T[i] + dp[j] for j in range(i - k, i))

    minKsum = inf
    for j in range(n - k, n):
        minKsum = min(minKsum, dp[j])

    return minKsum


T = [1, 2, 3, 4, 6, 15, 8, 7]
k = 4

print(ksuma(T, k))
