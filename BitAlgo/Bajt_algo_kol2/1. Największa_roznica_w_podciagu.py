

def roznica(A):
    n = len(A)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if A[j - 1] == 0:
                dp[i][j] = dp[i][j - 1] + 1
            elif A[j - 1] == 1:
                dp[i][j] = dp[i][j - 1] - 1

    result, indexes = -10, (-1, -1)

    for a in range(n + 1):
        for b in range(a, n + 1):
            if dp[a][b] > result:
                result = dp[a][b]
                indexes = (a - 1, b - 1)

    return result, indexes


A = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]

print(roznica(A))
