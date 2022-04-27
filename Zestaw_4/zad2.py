# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A.
# Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A,
# które sumują się do zadanej wartości T.


def substringOfSum(A, T):
    n = len(A)

    dp = [[1] + [0 for _ in range(T)] for _ in range(n)]

    if A[0] <= T:
        dp[0][A[0]] = 1

    for i in range(1, n):
        for j in range(1, T + 1):
            dp[i][j] = dp[i - 1][j]
            if j - A[i] >= 0 and dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j - A[i]]

    if dp[n - 1][T] == 1:
        return True
    return False


A = [5, 6, 7, 3, 3, 8, 13]
T = 21

print(substringOfSum(A, T))
