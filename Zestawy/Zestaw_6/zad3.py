# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.


# f(i, g, d) =


def prom(A, i, L):
    n = len(A)
    dp = [[[0 for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]

    for i in range(n):
        for g in range(L + 1):
            for d in range(L + 1):
                if g + A[i] < L + 1:
                    dp[i][g + A[i]][d] = dp[i][g][d] + 1
                if d + A[i] < L + 1:
                    dp[i][g][d + A[i]] = dp[i][g][d] + 1

    for r in dp:
        for q in r:
            print(q)



L = 20
A = [10, 2, 9, 15, 3, 2, 1]

prom(A, 0, L)




