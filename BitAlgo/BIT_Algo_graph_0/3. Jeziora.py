# Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd.
# Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.
# - Policz, ile jezior jest w tablicy
# - Policz, ile komórek zawiera największe jezioro


from queue import Queue


def lakes(lake):
    n = len(lake)
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and lake[i][j] == "W":
                Q = Queue()
                cnt = 0
                Q.put((i, j))

                while not Q.empty():
                    x, y = Q.get()
                    visited[x][y] = 1
                    cnt += 1
                    for m in moves:
                        X = x + m[0]
                        Y = y + m[1]
                        if isPossible(X, Y, n) and visited[X][Y] == -1 and lake[X][Y] == "W":
                            visited[X][Y] = 1
                            Q.put((X, Y))

                dp.append(cnt)

    return len(dp), max(dp)


def isPossible(X, Y, n):
    return 0 <= X < n and 0 <= Y < n


L = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

print(lakes(L))
