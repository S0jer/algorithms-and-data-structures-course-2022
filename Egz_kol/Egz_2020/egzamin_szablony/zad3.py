from zad3testy import runtests


def fast_sort(tab, a):
    n = len(tab)
    add = max(tab) / 20
    toBucket = [add * i for i in range(21)]
    buckets = [[] for _ in range(21)]

    for i in range(n):
        idx = 0
        while tab[i] > toBucket[idx]:
            idx += 1
        buckets[idx - 1].append(tab[i])

    result = []
    for bucket in buckets:
        if len(bucket) > 1:
            sort(bucket, 0, len(bucket) - 1)
        result += bucket

    return result


def sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        sort(A, p, q - 1)
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


runtests(fast_sort)
