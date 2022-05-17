from kol2btesty import runtests
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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
