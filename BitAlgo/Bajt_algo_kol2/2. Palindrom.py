def palindrom(A):
    n = len(A)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n and A[i] == A[i + 1]:
            dp[i][i + 1] = 1

    maxPal = -1
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] == A[j] and i + 1 <= j - 1:
                dp[i][j] = dp[i + 1][j - 1]
            if dp[i][j] == 1 and j + 1 - i > maxPal:
                maxPal = j + 1 - i

    for row in dp:
        print(row)

    return maxPal


A = 'aacaccabcc'

print(palindrom(A))
