from math import inf


def autostrada(T, k):
    n = len(T)
    dp = [[inf for _ in range(n)] for _ in range(k)]
    S = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(x, n):
            S[x][y] = S[x][y - 1] + T[y]

    for i in range(n):
        dp[0][i] = S[0][i]

    for i in range(1, k):
        for j in range(n):
            if j > 0:
                dp[i][j] = min(max(S[a + 1][j], dp[i - 1][a]) for a in range(j))

    for row in dp:
        print(row)

    return dp[k - 1][n - 1]


T = [5, 10, 30, 20, 15]
k = 3

print(autostrada(T, k))
