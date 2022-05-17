# Zadanie 6. (wyszukiwanie binarne) Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną
# niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A. Jeśli tak, to
# zwraca najmniejszy indeks, pod którym x występuje.


def binarySearch(A, i, j, x):
    idx = (j + i) // 2

    if j >= i:
        if A[idx] == x:
            return idx
        elif A[idx] > x:
            return binarySearch(A, i, idx - 1, x)
        elif A[idx] < x:
            return binarySearch(A, idx + 1, j, x)
    else:
        return -1


A = [1, 3, 4, 8, 11, 14, 15, 16, 21]

idx = binarySearch(A, 0, len(A) - 1, 123)
print(idx)
