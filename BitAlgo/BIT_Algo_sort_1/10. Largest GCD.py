# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n].
# Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich GCD jest różny od 1.
# Algorytm powinien działać jak najszybciej.

from random import randint


def findGCD(A):
    n = len(A)
    conds = []

    for i in range(2, n + 1):
        if isPrime(i):
            conds.append(i)

    k = len(conds)
    buckets = [[] for _ in range(k)]

    for i in range(n):
        for j in range(k):
            if A[i] % conds[j] == 0:
                buckets[j].append(A[i])
                break
    result = 0

    for bucket in buckets:
        if len(bucket) > result:
            result = len(bucket)

    return result


def isPrime(x):
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    j = 5
    while j < x:
        if x % j == 0:
            return False
        j += 2

    return True


A = [randint(1, 20) for _ in range(20)]
print(findGCD(A))
