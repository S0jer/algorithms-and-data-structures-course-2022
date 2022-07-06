from kol1btesty import runtests


def f(T):
    n, mm, nMax = len(T), 97, -1
    base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    for i in range(n):
        if len(T[i]) > nMax:
            nMax = len(T[i])
    nMax += 1

    buckets = [[] for _ in range(nMax)]

    for j in range(n):
        v = [0 for _ in range(26)]
        idx = len(T[j])
        for c in T[j]:
            v[ord(c) - mm] += 1

        c = 0
        for k in range(26):
            if v[k] > 0:
                c += base[k] ** v[k]

        buckets[idx].append(c)

    result = -1
    for bucket in buckets:
        m = len(bucket)
        quickSort(bucket, 0, m - 1)

        cnt = 1
        for j in range(1, m):
            if bucket[j - 1] == bucket[j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt

    return result


def quickSort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickSort(T, p, q - 1)
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


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(f, all_tests=True)
