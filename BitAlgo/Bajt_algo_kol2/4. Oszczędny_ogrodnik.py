from collections import deque


def ogrodnik(T, D, Z, l):
    n, m = len(T[0]), len(T)
    Visited = [[-1 for _ in range(n)] for _ in range(m)]
    Cost = []
    for idx in D:
        Cost.append(BFS(T, Visited, 0, idx))
    n = len(Z)
    dp = [[0 for _ in range(l + 1)] for _ in range(n)]

    for c in range(Cost[0], l + 1):
        dp[0][c] = Z[0]

    for i in range(1, n):
        for j in range(1, l + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= Cost[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - Cost[i]] + Z[i])

    print(get_solution(dp, Cost, Z, n - 1, l))
    return dp[n - 1][l]


def BFS(G, Visited, x0, y0):
    n, m = len(G[0]), len(G)

    result = 0
    Q = deque()
    Q.append((x0, y0))
    moves = [(1, 0), (0, 1), (0, -1)]

    while len(Q) > 0:
        x, y = Q.popleft()
        result += G[x][y]

        for move in moves:
            newX, newY = x + move[0], y + move[1]
            if isPossible(n, m, newX, newY) and G[newX][newY] != 0 and Visited[newX][newY] == -1:
                Visited[newX][newY] = 1
                Q.append((newX, newY))

    return result


def isPossible(n, m, x, y):
    return (0 <= x < m and 0 <= y < n)


def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    return get_solution(F, W, P, i - 1, w)


D = [4, 9, 12, 16]
Z = [13, 11, 15, 4]
l = 32
T = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0, 0, 6, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 0, 0, 2, 2, 2, 0, 2, 4, 2, 0],
     [0, 0, 0, 1, 2, 0, 0, 1, 4, 6, 0, 2, 1, 3, 0, 0, 3, 1, 0, 0]]

print(ogrodnik(T, D, Z, l))
