# Zadanie 5. (mnożenie macierzy) Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
# A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
# kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
# koszt mnożenia przy optymalnym doborze kolejności.

def matrixChainOrder(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(2, n):
        for j in range(1, n - i + 1):
            k = i + j - 1
            dp[j][k] = int(1e9 + 7)
            for l in range(j, k):
                cost = dp[j][l] + dp[l + 1][k] + A[j - 1] * A[l] * A[k]
                if cost < dp[j][k]:
                    dp[j][k] = cost

    return dp[1][n - 1]


A = [1, 2, 3, 4] # 18
B = [10, 20, 30] # 6000
C = [40, 20, 30, 10, 30] #26000
D = [10, 20, 30, 40, 30] #30000

print("A: ", matrixChainOrder(A))
print("B: ", matrixChainOrder(B))
print("C: ", matrixChainOrder(C))
print("D: ", matrixChainOrder(D))
