# Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
# długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2))


def longestCommonSubstring(A, B):
    n, m = len(A), len(B)
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                print(i, j)
                dp[i][j] = 0
            elif A[j - 1] == B[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for row in dp:
        print(row)

    return dp[m][n]


A = [4, 2, 4, 8, 7, 5]
B = A.copy()
B.sort()
B.append(11)
B.append(13)
print(A)
print(B)

print(longestCommonSubstring(A, B))
