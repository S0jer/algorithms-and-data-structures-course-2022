# Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [ai , bi]. Dwa przedziały można
# skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
# 1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
# 2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
# 3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.


# 3 !
# f(i, j) - długosc najdłuższego przedziału kończącego się na przedziale i

# f(i, j) = min liczba przedziałów które trzeba skleić, żeby powstał przedział od i do j
# f(i, j) = min(f(i, k) + f(k, j) ( ? + 1 ? )) for k in range(i, j)\
# nie jestem pewny co do tej "+ 1"

# zlozonosc: n^3
# rozwiązanie do podpunktu 3ciego sprawdza się dla dwóch poprzednich,


from math import inf


def longestSection(T, k):
    n = len(T)
    for section in T:
        n = max(n, section[0] + 1, section[1] + 1)

    dp = [[inf] * n for _ in range(n)]

    for section in T:
        dp[section[0]][section[1]] = 1
        dp[section[1]][section[0]] = 1

    for i in range(n):
        for j in range(n):
            for z in range(i, j + 1):
                dp[i][j] = min(dp[i][j], dp[i][z] + dp[z][j])

    LS = -1
    for a in range(n):
        for b in range(n):
            if abs(a - b) > LS and 0 < dp[a][b] <= k:
                LS = abs(a - b)

    for row in dp:
        print(row)

    return LS


T = [(1, 3), (2, 7), (3, 5), (1, 2), (4, 5), (4, 8), (1, 3), (1, 4), (0, 5), (0, 1), (1, 2), (2, 3), (3, 4), (7, 8)]

print(longestSection(T, 3))
