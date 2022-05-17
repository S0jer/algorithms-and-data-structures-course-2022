#
# Nie jest to moje rozwiązanie, skopiowane od osoby tłumaczącej rozwiązanie.
# It's not my solution, copied from the guy that explained how to solve it.
#


def f(T, dp, i, l1, l2):
    if i > len(T) - 1:
        return 0
    if dp[i][l1][l2] != -1:
        return dp[i][l1][l2]

    if T[i] > l1 and T[i] > l2:
        dp[i][l1][l2] = 0
        return 0

    if T[i] > l1:
        dp[i][l1][l2] = f(T, dp, i + 1, l1, l2 - T[i]) + 1
    elif T[i] > l2:
        dp[i][l1][l2] = f(T, dp, i + 1, l1 - T[i], l2) + 1

    else:
        w1 = f(T, dp, i + 1, l1 - T[i], l2)
        w2 = f(T, dp, i + 1, l1, l2 - T[i])
        dp[i][l1][l2] = max(w1, w2) + 1

    return dp[i][l1][l2]


def prom(T, l1, l2):
    n = len(T)
    dp = [[[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)] for _ in range(n)]
    w = f(T, dp, 0, l1, l2)

    i = 0
    l1 = l1
    l2 = l2
    sol = []
    sol2 = []

    while i < n and (l1 >= T[i] or l2 >= T[i]):
        if T[i] > l1:
            w1 = 0
            w2 = 1
        elif T[i] > l2:
            w1 = 1
            w2 = 0
        else:
            w1 = f(T, dp, i + 1, l1 - T[i], l2)
            w2 = f(T, dp, i + 1, l1, l2 - T[i])

        if w1 > w2:
            sol.append(i)
            l1 = l1 - T[i]
        else:
            sol2.append(i)
            l2 = l2 - T[i]
        i += 1

    if w - 1 in sol:
        return sol
    else:
        return sol2
