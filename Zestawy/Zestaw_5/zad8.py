# Zadanie 8. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie

from math import inf


def boardTravel(A):
    n, m = len(A), len(A[0])
    dp = [[inf for _ in range(m)] for _ in range(n)]
    dp[0][0] = A[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j - 1] + A[i][j]
            elif j == 0 and i > 0:
                dp[i][j] = dp[i - 1][j] + A[i][j]
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j], dp[i][j - 1] + A[i][j])

    return dp[n - 1][m - 1]


A = [[1, 1, 5],
     [1, 2, 0],
     [1, 2, 0],
     [1, 10, 5]]

boardTravel(A)
