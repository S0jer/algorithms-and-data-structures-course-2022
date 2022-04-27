# Zadanie 4. (najdłuższy podciąg rosnący) Proszę rozwiązać dwa następujące zadania:
# 1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
# najdłuższego rosnącego podciągu?
# 2. Na wykładzie podaliśmy algorytm działający w czasie O(n2). Proszę podać algorytm o złożoności O(nlog n)

def LongestIncreasingSubstring(A):
    n = len(A)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[j - 1] > A[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return max(F)


def fasterLis(A):
    n, idx = len(A), 0

    dp = [0 for _ in range(n + 1)]
    dp[0] = A[0]
    idx += 1

    for i in range(1, n):
        if A[i] < dp[0]:
            dp[0] = A[i]
        elif A[i] > dp[idx - 1]:
            dp[idx] = A[i]
            idx += 1
        else:
            dp[ceilIndex(dp, -1, idx - 1, A[i])] = A[i]

    return idx


def ceilIndex(A, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


A = [4, 2, 4, 8, 7, 5]
print(LongestIncreasingSubstring(A))
print(lis(A))
print(fasterLis(A))
