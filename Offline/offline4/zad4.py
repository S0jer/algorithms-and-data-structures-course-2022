from zad4testy import runtests


# Paweł Jaśkowiec 406165

# f(i, p) = max liczba studentów, które moga mieszkać w budynkach od 0 do i,
# które na siebie nie nachodzą i kosztują <= p

# f(i, p) = max(f(i - 1, p), students(i) + f(prev(i), p - cost(i)))


def select_buildings(T, p):
    n = len(T)
    for a in range(n):
        T[a] = (a, T[a][0], T[a][1], T[a][2], T[a][3])
    T = sorted(T, key=lambda x: x[3])
    StudentsCap = [students(u) for u in T]
    PreviousBuilding = [-1 for _ in range(n)]
    dp = [[0 for _ in range(p + 1)] for _ in range(n)]
    result = []

    for i in range(n):
        for t in range(i - 1, -1, -1):
            if T[i][2] > T[t][3]:
                PreviousBuilding[i] = t
                break

    for i in range(n):
        for t in range(p + 1):
            dp[i][t] = max(dp[i - 1][t], dp[i][t])
            if t - T[i][4] >= 0 and PreviousBuilding[i] == -1:
                dp[i][t] = max(dp[i][t], StudentsCap[i])
            elif t - T[i][4] >= 0 and PreviousBuilding[i] != -1:
                dp[i][t] = max(dp[i][t], StudentsCap[i] + dp[PreviousBuilding[i]][t - T[i][4]])

    getResult(dp, StudentsCap, PreviousBuilding, T, result, n - 1, p)

    return result


def getResult(dp, StudentsCap, PreviousBuilding, T, result, i, p):
    if i == -1:
        return result.sort()
    if i == 0:
        if p >= T[0][4]:
            result += [T[0][0]]
            return result.sort()
    if dp[i - 1][p] == dp[i][p]:
        return getResult(dp, StudentsCap, PreviousBuilding, T, result, i - 1, p)
    result += [T[i][0]]

    return getResult(dp, StudentsCap, PreviousBuilding, T, result, PreviousBuilding[i], p - T[i][4])


def students(u):
    return abs(u[1] * (u[3] - u[2]))


runtests(select_buildings)
