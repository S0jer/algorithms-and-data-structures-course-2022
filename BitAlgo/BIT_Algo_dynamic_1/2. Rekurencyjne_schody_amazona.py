# Zadanie 2: Rekurencyjne schody Amazona Dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1.
# Początkowo stoimy na pozycji 0, wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.
# Przykład A = {1,3,2,1,0} Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
# Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.


def amazonStairs(A):
    n = len(A)
    dp = [0 for _ in range(n)]
    dp[n - 1] = 1

    for i in range(n - 2, -1, -1):
        for j in range(i, min(i + A[i] + 1, n)):
            dp[i] += dp[j]

    return dp[0]


def amazonStairsBU(A):
    n = len(A)
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for i in range(n):
        for j in range(i + 1, min(i + A[i] + 1, n)):
            dp[j] += dp[i]

    return dp[n - 1]


B = [2, 1, 3, 2, 1, 0]
A = [1, 3, 2, 1, 0]

print(amazonStairs(A))
print(amazonStairsBU(B))
