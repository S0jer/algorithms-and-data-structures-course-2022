# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.


from collections import deque
from math import inf


def kingsPath(A, s, k):
    n = len(A)

    dp = [[inf for _ in range(n)] for _ in range(n)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dp[s[0]][s[1]] = A[s[0]][s[1]]
    Q = deque()
    Q.append((A[s[0]][s[1]], s))

    while len(Q) > 0:
        road, u = Q.popleft()

        for m in moves:
            x, y = u[0] + m[0], u[1] + m[1]
            if isPos(x, y, n) and dp[x][y] > A[x][y] + road:
                dp[x][y] = A[x][y] + road
                Q.append((dp[x][y], (x, y)))

    for row in dp:
        print(row)

    return dp[k[0]][k[1]]


def isPos(x, y, n):
    return (0 <= x < n and 0 <= y < n)


A = [[1, 1, 4, 5, 3, 5],
     [4, 1, 4, 2, 3, 4],
     [1, 5, 1, 1, 2, 4],
     [1, 1, 1, 2, 5, 3],
     [2, 1, 3, 5, 4, 5],
     [1, 2, 4, 4, 3, 2]]

B = [[1, 100, 0, 0],
     [99, 2, 1, 0],
     [1, 2, 1, 0],
     [1, 2, 99, 2]]

C = [[4, 0, 2, 1],
     [0, 0, 2, 1],
     [1, 1, 0, 4],
     [0, 3, 0, 1]]

n = len(A)
s, k = (0, 0), (n - 1, n - 1)

print(kingsPath(A, s, k))
