from egzP2atesty import runtests


def zdjecie(T, m, k):
    n = len(T)
    sortedT = T[:]

    quicksort(sortedT, 0, n - 1)

    idx, indexes, borders = 0, [], []

    for j in range(m):
        borders.append(idx)
        indexes.append(idx)
        idx += k
        k += 1
    borders.append(n)
    p = 0

    while p < n:
        for j in range(m - 1, -1, -1):
            if indexes[j] < borders[j + 1]:
                T[p] = sortedT[indexes[j]]
                indexes[j] += 1
                p += 1

    return None


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1

    return T


def partition(A, p, r):
    x = A[r][1]
    i = p - 1

    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


runtests(zdjecie, all_tests=False)
