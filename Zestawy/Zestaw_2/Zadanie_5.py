# Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.

from math import inf


def lider(A):
    n = len(A)
    maxId = -inf
    minId = inf

    for i in range(n):
        if A[i] > maxId:
            maxId = A[i]
        if A[i] < minId:
            minId = A[i]

    if minId >= 0:
        m = maxId + 1
        minus = 0
    else:
        minus = -1 * minId
        m = minus + maxId + 1

    tmp = 0
    indexes = [-1 for _ in range(m)]

    for j in range(n):
        if indexes[A[j] + minus] == -1:
            indexes[A[j] + minus] = tmp
            tmp += 1

    numbersCounter = [0 for _ in range(n)]

    for k in range(n):
        numbersCounter[indexes[A[k] + minus]] += 1

    for num in numbersCounter:
        if num > (n / 2):
            return True
    return False


T = [5, -22, 2, 2, 5, 5, 3]
print(lider(T))
