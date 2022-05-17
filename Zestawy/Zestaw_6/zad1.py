# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci,
# jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f - maksymalny zysk scinając do i-tego drzewa
# dp[i] = max(dp[i - 2] + A[i], dp[i - 1])

def blackForest(A):
    n = len(A)
    dp = [-1 for _ in range(n)]
    dp[0], dp[1] = A[0], A[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i])
    print(dp)

    return max(dp)


A = [1, 2, 8, 4, 3, 7, 1, 9, 2, 1, 3]
B = [5, 2, 4, 8, 11, 3, 1, 1]
resultA = blackForest(A)
print(resultA)
resultB = blackForest(B)
print(resultB)
