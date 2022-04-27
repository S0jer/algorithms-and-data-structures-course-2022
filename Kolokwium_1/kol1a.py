from kol1atesty import runtests


# Paweł Jaśkowiec, 406165

# Pomysł polega na podzieleniu słów względem długości oraz drugiej litery słowa,
# oraz zliczeniu siły dla elementów podzielonych względem danych zależności

#

def g(T):
    n = len(T)
    maxL = 0
    for i in range(n):
        if len(T[i]) > maxL:
            maxL = len(T[i])

    buckets = [[] for _ in range(maxL + 1)]

    for i in range(n):
        buckets[len(T[i])].append(T[i])

    result = -1
    for bucket in buckets:
        m = len(bucket)
        if m > 0:

            bucket = sort(bucket)
            x = 1
            for i in range(m - 1):
                if bucket[i] == bucket[i + 1] or bucket[i] == bucket[i + 1][::-1]:
                    x += 1
                else:
                    x = 1
                if x > result:
                    result = x

    return result


def sort(T):
    n = len(T)
    for j in range(len(T[0]) - 1, -1, -1):
        values = [0 for _ in range(n)]
        for i in range(n):
            values[i] = ord(T[i][j])

        T = quicksort(values, T, 0, n - 1)

    return T


def partition(V, A, p, r):
    x = V[r]
    i = p - 1
    for j in range(p, r):
        if V[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            V[i], V[j] = V[j], V[i]

    A[r], A[i + 1] = A[i + 1], A[r]
    V[r], V[i + 1] = V[i + 1], V[r]

    return i + 1


def quicksort(V, A, p, l):
    while p < l:
        q = partition(V, A, p, l)
        quicksort(V, A, p, q - 1)
        p = q + 1

    return A


runtests(g, all_tests=True)
