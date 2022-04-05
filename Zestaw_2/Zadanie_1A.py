# Zadanie 1a. Proszę zaimplementować algorytm MergeSort sortujący tablicę, opierający się na złączaniu
# serii naturalnych.


from random import randint, seed


def mergesort(T):
    n = len(T)
    if n <= 1:
        return T

    idx = 0
    while idx + 1 < n and T[idx] <= T[idx + 1]:
        idx += 1
    if idx + 1 < n:
        idx += 1

    Left = mergesort(T[idx:])
    Right = mergesort(T[:idx])

    return merge(Left, Right)


def merge(Left, Right):
    i, j, lengthLeft, lengthRight = 0, 0, len(Left), len(Right)
    result = []

    if lengthLeft < 1:
        return Right
    elif lengthRight < 1:
        return Left

    while i < lengthLeft and j < lengthRight:
        if Left[i] <= Right[j]:
            result.append(Left[i])
            i += 1
        else:
            result.append(Right[j])
            j += 1

    if i >= lengthLeft:
        while j < lengthRight:
            result.append(Right[j])
            j += 1
    else:
        while i < lengthLeft:
            result.append(Left[i])
            i += 1

    return result


seed(42)

n = 10
T = [randint(1, 100) for i in range(100)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
