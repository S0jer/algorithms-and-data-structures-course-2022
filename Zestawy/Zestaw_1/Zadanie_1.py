# Zadanie 1. Proszę zaimplementować jeden ze standardowych algorytmów sortowania tablicy działający w
# czasie O(n2) (np. sortowanie bąbelkowe, sortowanie przez wstawianie, sortowanie przez wybieranie).

from random import randint


def bubbleSort(A):
    n = len(A)

    while True:
        check = True
        for i in range(1, n):
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                check = False

        if check:
            break

    return A


def selectionSort(A):
    n, idx = len(A), 0
    while idx < n:
        idx_min = idx
        for i in range(idx, n):
            if A[idx_min] > A[i]:
                idx_min = i

        A[idx_min], A[idx] = A[idx], A[idx_min]

        idx += 1

    return A


def insertionSort(A):
    n, idx = len(A), 0

    for i in range(1, n):
        u = A[i]
        j = i - 1
        while j >= 0 and A[j] > u:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = u

    return A


A = [randint(1, 100) for _ in range(10)]

insertionSort(A)
selectionSort(A)
bubbleSort(A)
