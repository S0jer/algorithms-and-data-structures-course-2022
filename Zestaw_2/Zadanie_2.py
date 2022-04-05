# Zadanie 2. Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
# liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].
from random import randint


def mergesortInversions(T):
    global counter
    if len(T) > 1:
        half = len(T) // 2
        Left = T[:half]
        Right = T[half:]
        mergesortInversions(Left)
        mergesortInversions(Right)

        i, j, idx = 0, 0, 0

        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                T[idx] = Left[i]
                i += 1
            else:
                T[idx] = Right[j]
                counter += half - i
                j += 1
            idx += 1

        while j < len(Right):
            T[idx] = Right[j]
            idx += 1
            j += 1
        while i < len(Left):
            T[idx] = Left[i]
            idx += 1
            i += 1

    return T


def inversion(T):
    x = 0
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i] > T[j]:
                x += 1
    return x


if __name__ == '__main__':
    counter = 0
    T = [randint(1, 100) for i in range(40)]

    print(T)
    x = inversion(T)
    mergesortInversions(T)
    print(T)
    print(x, counter)
