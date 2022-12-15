import bisect
from math import log10
from egzP2btesty import runtests

def kryptograf(D, Q):
    # O(nm)
    for i in range(len(D)):
        D[i] = D[i][::-1]
    # O(qm)
    for i in range(len(Q)):
        Q[i] = Q[i][::-1]
    # O(nmlog(nm)) < O(n^2log(n))
    D = sorted(D)

    output = 0
    # O(qmlog(n))
    for i in Q:
        # O(m*log(n))
        lo = bisect.bisect_left(D, i)
        hi = bisect.bisect_right(D, i + "2")
        output += log10(hi - lo)
    return output

# Zmień all_test
runtests(kryptograf, all_tests = 3)

# D = ['0', '001', '0011', '1011', '1111']
# Q = ["", "1", "11", "0", "1011"]