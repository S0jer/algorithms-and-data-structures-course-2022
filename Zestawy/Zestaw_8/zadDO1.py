# Zadanie 1. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.


from collections import deque


def shipCaptain(M, T, s, k):
    n, m = len(M), len(M[0])
    dp = [[False for _ in range(m)] for _ in range(n)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    Q = deque()
    Q.append(s)

    while len(Q) > 0:
        x, y = Q.popleft()
        dp[x][y] = True

        for move in moves:
            nextX, nextY = x + move[0], y + move[1]
            if isPos(nextX, nextY, n, m) and dp[nextX][nextY] is False and M[nextX][nextY] >= T:
                Q.append((nextX, nextY))

    return dp[k[0]][k[1]]


def isPos(x, y, n, m):
    return (0 <= x < n and 0 <= y < m)


M = [[3, 1, 4, 5, 3, 5],
     [4, 1, 4, 2, 3, 4],
     [3, 5, 3, 1, 2, 4],
     [1, 1, 1, 2, 5, 3],
     [2, 1, 3, 5, 4, 5],
     [1, 2, 4, 4, 3, 2],
     [1, 2, 4, 4, 3, 3]]

n = len(M)
m = len(M[0])
T, s, k = 3, (0, 0), (n - 1, m - 1)
print(shipCaptain(M, T, s, k))
