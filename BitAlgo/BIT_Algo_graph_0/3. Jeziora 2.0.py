# c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0]
# do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
# d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce


from queue import PriorityQueue
from math import inf


def lakes2(L, s):
    n = len(L)
    Q = PriorityQueue()
    dp = [[inf for _ in range(n)] for _ in range(n)]
    moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    dp[s[0]][s[1]] = 0
    Q.put((dp[s[0]][s[1]], s[0], s[1]))

    while not Q.empty():
        _, x, y = Q.get()

        for m in moves:
            X = x + m[0]
            Y = y + m[1]

            if isPossible(X, Y, n) and dp[X][Y] > dp[x][y] + 1 and L[X][Y] == "L":
                dp[X][Y] = dp[x][y] + 1
                Q.put((dp[X][Y], X, Y))

    return dp[n - 1][n - 1]


def isPossible(x, y, n):
    return 0 <= x < n and 0 <= y < n


L = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

print(lakes2(L, (0, 0)))
