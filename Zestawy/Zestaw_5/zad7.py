# Zadanie 7. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
# kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa:
# dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)


def coins(M, x):
    dp = [_ for _ in range(x + 1)]
    dp[0] = 0

    for i in range(x + 1):
        for m in M:
            if i >= m:
                dp[i] = min(dp[i], dp[i - m] + 1)

    print(dp)
    return dp[x]


M = [1, 5, 8]
x = 15

print(coins(M, x))
