# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na
# losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).


def tenNumbers(A, k):
    n = len(A)
    lNumbers = []
    uNumbers = []
    normalNumbers = []

    for i in range(n):
        if 0 <= A[i] <= k:
            normalNumbers.append(A[i])
        elif A[i] < 0:
            lNumbers.append(A[i])
        else:
            uNumbers.append(A[i])

    quicksort(normalNumbers, 0, len(normalNumbers) - 1)
    quicksort(lNumbers, 0, len(lNumbers) - 1)
    quicksort(uNumbers, 0, len(uNumbers) - 1)

    result = lNumbers + normalNumbers + uNumbers

    return result


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


A = [3, 1234, -432, 2, 5, 100, -450, 1, 8, 9, 10, -10, 12]
k = 10

print(tenNumbers(A, k))
