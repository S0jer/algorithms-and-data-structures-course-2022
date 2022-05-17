# Edit distance DP problem
from math import inf


def napraw(s, t):
    m, n = len(s), len(t)

    dp = [[inf for _ in range(m)] for _ in range(n)]

    if t[0] != s[0]:
        dp[0][0] = 1

    for i in range(1, m):
        if t[0] != s[i]:
            dp[0][i] = dp[0][i - 1] + 1
        else:
            dp[0][i] = i

    for j in range(1, n):
        if s[0] != t[j]:
            dp[j][0] = dp[j - 1][0] + 1
        else:
            dp[j][0] = j

    for a in range(1, n):
        for b in range(1, m):
            if t[a] == s[b]:
                dp[a][b] = dp[a - 1][b - 1]
            else:
                dp[a][b] = min(dp[a - 1][b - 1], dp[a - 1][b], dp[a][b - 1]) + 1

    for row in dp:
        print(row)

    return dp[n - 1][m - 1]


s = "swidry"
t = "kawiory"

print(napraw(s, t))
