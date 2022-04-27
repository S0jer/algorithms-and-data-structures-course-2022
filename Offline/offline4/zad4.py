from zad4testy import runtests


# Paweł Jaśkowiec 406165

# f(i, p) = maksymalna pojemność budynków {0, i}, które na siebie nie nachodzą o cenie mniejszej niz p
# f(i, p) = max(f(i-1, b), f(i - 1, b - sortedT[i][3]) + cap[i]) dla odpowiednich warunków


def overlap(T, rec, i):
    n = len(rec)
    notOverlap = 0
    for el in rec:
        if el == -1:
            n -= 1
        elif T[el][1] > T[i][2] or T[el][2] < T[i][1]:
            notOverlap += 1

    if notOverlap == n:
        return True
    return False


def select_buildings(T, p):
    n = len(T)
    sortedT = sorted(T[::], key=lambda x: (x[1], x[2]))

    cap = [0 for _ in range(n)]

    for i in range(n):
        cap[i] = students(sortedT[i])

    dp = [[[0, []] for _ in range(p + 1)] for _ in range(n)]

    for b in range(sortedT[0][3], p + 1):
        dp[0][b][0] = cap[0]
        dp[0][b][1] = [0]

    for b in range(p + 1):
        for i in range(1, n):
            dp[i][b][0] = dp[i - 1][b][0]
            dp[i][b][1] = dp[i - 1][b][1][:]

            if b - sortedT[i][3] >= 0 and overlap(sortedT, dp[i - 1][b - sortedT[i][3]][1], i):
                newCap = dp[i - 1][b - sortedT[i][3]][0] + cap[i]
                if newCap > dp[i][b][0]:
                    dp[i][b][0] = newCap
                    dp[i][b][1] = dp[i - 1][b - sortedT[i][3]][1][:] + [i]
                if cap[i] > dp[i][b][0]:
                    dp[i][b][0] = cap[i]
                    dp[i][b][1] = [i]

    result = []
    maxC = 0

    for i in range(p + 1):
        if dp[n - 1][i][0] > maxC:
            result = dp[n - 1][i][1]
            maxC = dp[n - 1][i][0]
    # for i in range(n):
    #     for j in range(p + 1):
    #         if dp[i][j][0] > maxC:
    #             result = dp[i][j][1]
    #             maxC = dp[i][j][0]

    finalresult = []

    for el in result:
        for i in range(n):
            if sortedT[el] == T[i]:
                finalresult.append(i)

    return finalresult


def students(u):
    return abs(u[0] * (u[2] - u[1]))


runtests(select_buildings)
