# Zadanie 5
# Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich
# binarnych (0/1) string'ów o długości n bez jedynek obok siebie.

# f(i) - ilość prawidłowych ciągów o długości i


def binaryS(n):
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = 2, 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 100

print(binaryS(n))
