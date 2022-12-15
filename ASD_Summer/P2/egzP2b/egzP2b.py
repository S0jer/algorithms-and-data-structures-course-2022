from egzP2btesty import runtests
from math import log10
import bisect


# Sol 1
def kryptograf1(D, Q):
    n, m = len(D), len(Q)

    for i in range(n):
        D[i] = D[i][::-1]
    for j in range(m):
        Q[j] = Q[j][::-1]

    D.sort()

    result = 1
    for i in Q:
        lo = bisect.bisect_left(D, i)
        hi = bisect.bisect_right(D, i + "2")
        result *= hi - lo

    return log10(result)


def kryptograf2(D, Q):
    n, m = len(D), len(Q)
    maxi = 0

    for i in range(n):
        D[i] = D[i][::-1]
        maxi = max(maxi, len(D[i]))
    for j in range(m):
        Q[j] = Q[j][::-1]

    D = radixSort(D, maxi)

    result = 0
    for i in Q:
        lo = bisect.bisect_left(D, i)
        hi = bisect.bisect_right(D, i + "2")
        result += log10(hi - lo)

    return result


def radixSort(tab, x):
    if x == -1:
        return tab

    idx, r0, r1 = x, [], []

    for el in tab:
        if len(el) <= idx:
            r0 = [el] + r0
        elif el[idx] == "0":
            r0.append(el)
        else:
            r1.append(el)

    return radixSort(r0 + r1, x - 1)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf2, all_tests=3)
