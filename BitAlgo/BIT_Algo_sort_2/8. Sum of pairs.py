# Dana jest tablica A oraz liczba k. Znaleźć liczbę różnych par elementów z tablicy A o różnicy równej k.
#
# Przykład: Dla tablicy [7,11,3,7,3,9,5] oraz k = 4 odpowiedź to 3

# Sortujemy tablicę rosnąco, usuwając duplikaty
# Dla każdego elementu A[i] szukamy binarnie elementu A[i] + k. Jeśli znaleźliśmy, to zwiększamy counter o 1.


def sumOfPairs(A, k):
    n = len(A)
    result = 0
    
    quickSort(A, 0, n - 1)
    uniqueNumbers = [A[0]]

    for i in range(1, n):
        if uniqueNumbers[-1] != A[i]:
            uniqueNumbers.append(A[i])

    m = len(uniqueNumbers)

    for j in range(m):
        if binarySearch(uniqueNumbers, 0, m - 1, uniqueNumbers[j] + k) is not None:
            result += 1

    return result


def binarySearch(A, i, j, x):
    if i > j:
        return None
    half = (i + j) // 2

    if A[half] == x:
        val = binarySearch(A, i, half - 1, x)
        if val is None:
            return half
        return val
    elif A[half] < x:
        return binarySearch(A, half + 1, j, x)
    else:
        return binarySearch(A, i, half - 1, x)


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

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


A = [7, 11, 3, 7, 3, 9, 5]
k = 4

print(sumOfPairs(A, k))
