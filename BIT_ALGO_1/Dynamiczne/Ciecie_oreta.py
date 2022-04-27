def cut(V, n):
    m = n + 1

    dp = [0 for _ in range(m)]
    dp[0] = V[0]
    dp[1] = V[1]
    print(dp)

    for i in range(1, m):
        for j in range(i + 1):
            dp[i] = max(dp[i], dp[j] + max(dp[i - j], V[i - j]))

    print(dp)

if __name__ == '__main__':

    V = [0, 1, 2, 4, 3, 1]
    n = 5

    cut(V, n)








