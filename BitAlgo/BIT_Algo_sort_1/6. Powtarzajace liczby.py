# Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej, zaledwie O(log(n))
# liczb jest unikatowe (reszta to powtórzenia). Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.


from random import randint


def sameNumbersCorrect(A):
    n = len(A)
    uniqueNumbers = []
    for i in range(n):
        insert(uniqueNumbers, A[i])

    result = []

    for num in uniqueNumbers:
        result += [num[0]] * num[1]
    return result


def insert(uniqueNumbers, param):
    idx = binarySearch(uniqueNumbers, 0, len(uniqueNumbers) - 1, param)

    if idx is not None:
        uniqueNumbers[idx][1] += 1
    else:
        tmp = [param, 1]
        i = 0
        while i < len(uniqueNumbers):
            if tmp[0] < uniqueNumbers[i][0]:
                t = uniqueNumbers[i]
                uniqueNumbers[i] = tmp
                tmp = t
            i += 1
        uniqueNumbers.append(tmp)


def binarySearch(A, i, j, x):
    if i > j:
        return None

    half = (i + j) // 2
    if A[half][0] == x:
        val = binarySearch(A, i, half - 1, x)
        if val is None:
            return half
        return val
    if A[half][0] > x:
        return binarySearch(A, i, half - 1, x)
    else:
        return binarySearch(A, half + 1, j, x)


def sameNumbers(A):
    n = len(A)
    maxN = 0
    for i in range(n):
        maxN = max(maxN, A[i])

    numbersCounter = [0 for _ in range(maxN + 1)]
    toSortList = []

    for j in range(n):
        if numbersCounter[A[j]] == 0:
            numbersCounter[A[j]] += 1
            toSortList.append(A[j])
        else:
            numbersCounter[A[j]] += 1

    quicksort(toSortList, 0, len(toSortList) - 1)
    result = []

    for k in range(len(toSortList)):
        result += numbersCounter[toSortList[k]] * [toSortList[k]]

    return result


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
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


A = [randint(1, 10) for _ in range(40)]

print(sameNumbersCorrect(A))
print()
print(sameNumbers(A))
