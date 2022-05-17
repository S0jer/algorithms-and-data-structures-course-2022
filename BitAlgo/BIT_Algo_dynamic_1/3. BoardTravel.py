# Zadanie 3
# Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia). Mamy znaleźć minimalny koszt potrzebny do
# dostania się z pozycji [0][0] do [M-1][N-1]  Zakładamy, że:
# 1. Możemy poruszać się tylko w bok i w dół
# 2. Wszystkie koszty są dodatnie
from math import inf


def board(A):
    n, m = len(A), len(A[0])
    dp = [[inf for _ in range(m)] for _ in range(n)]
    dp[0][0] = A[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + A[i][j])
            elif i > 0 and j == 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j], dp[i][j - 1] + A[i][j])

    for row in dp:
        print(row)
    return dp[n - 1][m - 1]


T = [[1, 4, 5, 76, 3],
     [1, 4, 5, 76, 3],
     [1, 4, 5, 76, 3],
     [1, 4, 5, 76, 3],
     [1, 4, 5, 5, 3],
     [1, 4, 5, 76, 3]]

print(board(T))
