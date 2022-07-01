# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n.
# Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.

# Sortujemy mniejsza tablicę i dla każdego elementu z większej sprawdzamy binary-searchem czy jest w większej


from random import randint


def twoTables(A, B):
    if len(A) > len(B):
        smallTable = B
        bigTable = A
        m, n = len(B), len(A)
    else:
        smallTable = A
        bigTable = B
        m, n = len(A), len(B)

    quickSort(smallTable, 0, m - 1)

    for i in range(n):
        if binarySearch(smallTable, 0, m - 1, bigTable[i]) is not None:
            return False

    return True


def binarySearch(A, i, j, x):
    if i > j:
        return None
    half = (i + j) // 2

    if A[half] == x:
        val = binarySearch(A, i, half - 1, x)
        if val is None:
            return half
        return val

    if A[half] > x:
        return binarySearch(A, i, half - 1, x)
    else:
        return binarySearch(A, half + 1, j, x)


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


A = [randint(5, 20) for _ in range(20)]
B = [4, 2, 6, 8, 10]

print(twoTables(A, B))
