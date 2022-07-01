# Dana jest tablica zawierająca n liczb z zakresu [0...n^2-1]. Napisz algorytm, który posortuje taką tablicę w czasie O(n).


from random import randint


def bNumbers(A, k):
    n = len(A)
    for i in range(n):
        A[i] = (A[i] // k, A[i] % k)

    rSort(A, 1, k)
    rSort(A, 0, k)

    for i in range(n):
        A[i] = A[i][0] * k + A[i][1]

    return A


def rSort(A, idx, k):
    n = len(A)

    buckets = [[] for _ in range(k)]

    for i in range(n):
        buckets[A[i][idx]].append(A[i])

    j = 0
    for bucket in buckets:
        for el in bucket:
            A[j] = el
            j += 1


T = [randint(100, 899) for _ in range(20)]
R = T[::]
R.sort()

k = 30

result = bNumbers(T, k)
print("W", result)
print("R", R)

for j in range(len(R)):
    if result[j] != R[j]:
        print("False")
        break
