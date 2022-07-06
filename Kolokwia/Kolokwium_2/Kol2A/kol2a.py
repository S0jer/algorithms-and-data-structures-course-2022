from kol2atesty import runtests

from math import inf


# f(i, J/M) - minimalna ilośc odwiedzonych punktow kontrolnych przez Mariana dla punktu zmiany i gdzie do danego punktu
# przyjezdza J lub M, rozrozniamy dla danych dwoch przypadkow

# dp[i][0] = min(dp[i - 1][1], dp[i - 2][1], dp[i - 3][1])
# dp[i][1] = min(dp[i - 1][0] + (switch[i][1] - switch[i - 1][1]),
#                dp[i - 2][0] + (switch[i][1] - switch[i - 2][1]),
#                dp[i - 3][0] + (switch[i][1] - switch[i - 3][1]))


def drivers(P, B):
    P.append((B, True))
    n = len(P)

    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)

    P = sorted(P, key=lambda x: x[0])

    switch = [(0, 0), (0, 0), (0, 0)]
    controls = 0
    for i in range(n):
        if P[i][1] is True:
            switch.append((P[i][2], controls))
        else:
            controls += 1

    n = len(switch)
    dp = [[inf, inf] for _ in range(n)]
    road = [[[], []] for _ in range(n)]
    dp[0] = [inf, 0]
    dp[1] = [inf, 0]
    dp[2] = [inf, 0]
    #         J   M

    for i in range(3, n):
        for j in range(i - 3, i):
            if dp[i][0] > dp[j][1]:
                dp[i][0] = dp[j][1]
                road[i][0] = road[j][1] + [switch[i][0]]

            if dp[i][1] > (dp[j][0] + (switch[i][1] - switch[j][1])):
                dp[i][1] = dp[j][0] + (switch[i][1] - switch[j][1])
                road[i][1] = road[j][0] + [switch[i][0]]

    if dp[n - 1][0] > dp[n - 1][1]:
        result = road[n - 1][1]
    else:
        result = road[n - 1][0]
    result.pop(-1)
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=True)
