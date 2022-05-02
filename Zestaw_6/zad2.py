# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.


def fallingBlocks(A):
    n = len(A)
    A = sorted(A, key=lambda x: x[0])
    print(A)

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])
    print(dp)
    return n - max(dp)


A = [[3, 5], [4, 10], [1, 5], [8, 8], [5, 8], [7, 8], [2, 3]]
print(fallingBlocks(A))
