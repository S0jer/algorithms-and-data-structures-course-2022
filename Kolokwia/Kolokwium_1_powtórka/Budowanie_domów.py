def choosePlace(A):
    n = len(A)
    quicksort(A, 0, len(A) - 1)
    if n % 2 == 1:
        pass
    else:
        pass


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


def quicksort(A, p, l):
    while p < l:
        q = partition(A, p, l)
        quicksort(A, p, q - 1)
        p = q + 1

    return A


def binarySearch(T, i, j, x):
    if i > j:
        return None
    half = (i + j) // 2

    if T[half] == x:
        result = binarySearch(T, i, half - 1, x)
        if result == None:
            return half
        return result
    if T[half] > x:
        return binarySearch(T, i, half - 1, x)
    else:
        return binarySearch(T, half + 1, j, x)





if __name__ == '__main__':
    A = []
