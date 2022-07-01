# Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, w którym z nim należy
# wybudować dom, tak aby suma euklidesowych odległości od tego punktu do wszystkich pozostałych była minimalna.
# Należy zwrócić również tę sumę. Algorytm powinien być jak najszybszy.


# Gdy długość tablicy jest nieparzysta: znajdujemy medianę (QuickSelect / magiczne piątki)
# Gdy jest parzysta, to znajdujemy dwa środkowe elementy i liczymy ich odległość do każdego punktu

# Ja sortuje i szukam odległości punktów kazdy z kazdym liniowo zwracam najmniejszy

from math import inf


def buildHouse(A):
    n = len(A)
    quickSort(A, 0, n - 1)
    
    diffList = [0 for _ in range(n)]
    diff = 0
    for i in range(1, n):
        diff += (A[i] - A[i - 1]) * i
        diffList[i] += diff
    diffList[0] = diffList[n - 1]
    diff = 0

    for j in range(n - 1, 0, -1):
        diff += (A[j] - A[j - 1]) * (n - j)
        diffList[j] += diff

    result, minDist = -1, inf
    for k in range(n):
        if diffList[k] < minDist:
            minDist = diffList[k]
            result = k

    return result


def quickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        p = q + 1


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


A = [30, 10, 1, 5, 3]

print(buildHouse(A))
