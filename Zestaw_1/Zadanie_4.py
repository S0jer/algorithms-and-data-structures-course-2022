# Zadanie 4. (min/max) Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
# oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań

from random import randint


def minMax(A):
    n = len(A)

    maxId, minID = 0, 0
    for i in range(0, n, 2):
        if i + 1 < n and A[i] >= A[i + 1]:
            if A[i] >= A[maxId]:
                maxId = i
            if A[minID] >= A[i + 1]:
                minID = i + 1
        elif i + 1 < n and A[i + 1] >= A[i]:
            if A[i + 1] >= A[maxId]:
                maxId = i + 1
            if A[minID] >= A[i]:
                minID = i
        elif i + 1 >= n:
            if A[i] >= A[maxId]:
                maxId = i
            if A[minID] >= A[i]:
                minID = i

    print(min(A), A[minID])
    print(max(A), A[maxId])


A = [randint(-500, 500) for _ in range(100)]

minMax(A)
