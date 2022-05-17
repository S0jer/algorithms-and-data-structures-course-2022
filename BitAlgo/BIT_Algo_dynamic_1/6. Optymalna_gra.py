# Zadanie 6
# Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy i
# dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie,
# jaką maksymalną sumę możemy uzbierać?


def optimalGame(board):
    n = len(board)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    pref = [i for i in board]

    for i in range(n):
        dp[i][i] = board[i]
        if i > 0:
            pref[i] += pref[i - 1]

    for l in range(2, n):
        for i in range(n - l):
            dp[i][i + l] = pref[i + l] - pref[i]
            dp[i][i + l] -= min(dp[i + 1][i + l], dp[i][i + l - 1])

    return dp[0][n - 1]


A = [2, 2, 4, 2, 5, 4, 5, 1, 1, 2]
B = [1, 4, 5, 6, 7, 3, 1]

print(optimalGame(A))
print(optimalGame(B))
