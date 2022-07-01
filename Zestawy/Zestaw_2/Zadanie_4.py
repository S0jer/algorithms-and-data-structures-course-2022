# Zadanie 4. (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
# przez współrzędne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
# pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def waterBottles(A, wV):
    n = len(A)
    capacities = [0 for _ in range(n)]
    bottlesCap = 0
    quicksort(A, 0, n - 1)
    # printT(A)
    for i in range(n):
        capacities[i] = capacity(A[i])
        bottlesCap += capacities[i]

    if wV >= bottlesCap:
        return n
    result, i = 0, 0
    while i < n and wV > 0:
        z = i + 1
        capOfNextBott = capacities[i]
        while z < n and A[i][0].y > A[z][1].y:
            pA = Point(A[z][0].x, min(A[i][0].y, A[z][0].y))
            point = (pA, A[z][1])
            tmp = capacity(point)
            capOfNextBott += tmp
            capacities[z] -= tmp
            z += 1

        wV -= capOfNextBott
        if wV >= 0:
            result += 1
        i += 1
    return result


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


def partition(A, p, r):
    x = A[r][1].y
    i = p - 1

    for j in range(p, r):
        if A[j][1].y < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def printT(A):
    for a in A:
        print((a[0].x, a[0].y, a[1].x, a[1].y), end=" | ")
    print()


def capacity(point):
    return abs(point[0].x - point[1].x) * abs(point[0].y - point[1].y)


if __name__ == '__main__':
    A = [(Point(-1, 7), Point(1, 0)), (Point(2, 2), Point(6, -2)), (Point(7, 4), Point(12, 1)),
         (Point(-4, 2), Point(-2, 0))]
    w_v = 29
    print(waterBottles(A, w_v))
