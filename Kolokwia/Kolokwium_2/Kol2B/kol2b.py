from kol2btesty import runtests
from queue import PriorityQueue
from math import inf


# Paweł Jaśkowiec, 406165

# f(i) - min koszt dojechania do parkingu i,
# dla f[i][0] bez wykorzystania wyjątku, dla f[i][1] z wykorzystaniem wyjątku

# Algorytm polega na wyliczeniu minimalnej ceny dojazdu do i-tego parkingu dla wariantu z wykorzystaniem wyjątku
# oraz bez wykorzystania gdzie na koniec odczytujemy najlepszy wynik z obu wariantów.

# Na początku tworzymy również tablicę miejsc parkingów i ich cen oraz sortujemy rosnąco po miejscu prakingu

# Złożoność: O(n^2)


def min_cost(O, C, T, L):
    n, park = len(O), []
    for i in range(n):
        park.append((O[i], C[i]))

    park.sort(key=lambda x: x[0])

    dp = [[inf, inf] for _ in range(n + 1)]
    park = [(0, 0)] + park
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and park[i][0] - park[j][0] <= 2 * T:
            if park[i][0] - park[j][0] <= T:
                dp[i][0] = min(dp[i][0], dp[j][0] + park[i][1])
                dp[i][1] = min(dp[i][1], dp[j][1] + park[i][1])

            dp[i][1] = min(dp[i][1], dp[j][0] + park[i][1])
            j -= 1

    j = n
    result = inf
    while L - park[j][0] <= 2 * T:
        if L - park[j][0] <= T:
            result = min(result, dp[j][1])
        result = min(result, dp[j][0])
        j -= 1

    return result


def min_cost_nlog(O, C, T, L):
    n, park = len(O), []

    for i in range(n):
        park.append((O[i], C[i]))
    park.append((0, 0))
    park.append((L, 0))
    park.sort()

    n = len(park)

    dp = [[inf, inf] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    Q0 = PriorityQueue()
    Q1T = PriorityQueue()
    Q2T = PriorityQueue()

    Q0.put((0, 0))  # Moge uzyc wyjatku przegladam w odleglosci T
    Q2T.put((0, 0))  # Moge uzyc wyjatku przegladam w odleglosci 2T
    Q1T.put((0, 0))  # Nie moge uzyc wyjatku

    for i in range(1, n):
        while True:
            x = Q0.get()
            if park[i][0] - x[1] <= T:
                break
        Q0.put(x)

        while True:
            y = Q2T.get()
            if park[i][0] - y[1] <= 2 * T:
                break
        Q2T.put(y)

        while True:
            z = Q1T.get()
            if park[i][0] - z[1] <= T:
                break
        Q1T.put(z)

        dp[i][0] = x[0] + park[i][1]
        dp[i][1] = min(y[0], z[0]) + park[i][1]

        Q0.put((dp[i][0], park[i][0]))
        Q2T.put((dp[i][0], park[i][0]))
        Q1T.put((dp[i][1], park[i][0]))

    return min(dp[-1][0], dp[-1][1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost_nlog, all_tests=True)
# runtests(min_cost, all_tests=True)
