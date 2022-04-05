# Zadanie 3. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x.
# Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.


def searchSum(A, x):
    n, i, j = len(A), 0, 0

    while i < n and j < n:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] > x:
            i += 1
        elif A[i] + A[j] < x:
            j += 1

    return -1


A = [1, 3, 4, 8, 11, 14, 15, 16, 21]

idx = searchSum(A, 5)
print(idx)
