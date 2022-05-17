# Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący
# wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym.
# Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów.


def knapsack(value, weight, maxWeight):
    n = len(value)

    dp = [[0 for _ in range(maxWeight + 1)] for _ in range(n)]

    for i in range(weight[0], maxWeight + 1):
        dp[0][i] = value[0]

    for i in range(1, n):
        for j in range(maxWeight + 1):
            dp[i][j] = dp[i - 1][j]
            if j - weight[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + value[i])

    return getSol(dp, n, maxWeight)


def getSol(dp, n, maxWeight):
    result = []
    i, j = n - 1, maxWeight

    while i > 0 and j > 0:
        while i - 1 >= 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        result.append(i)
        while j - 1 >= 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        j -= 1

    return result[::-1]


weight = [4, 5, 12, 9, 1, 13]
value = [10, 8, 4, 5, 3, 7]

maxWeight = 16

result = knapsack(value, weight, maxWeight)

print(result)
