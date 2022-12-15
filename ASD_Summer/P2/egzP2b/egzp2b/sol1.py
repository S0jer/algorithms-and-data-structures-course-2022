from math import log10
from egzP2btesty import runtests

def kryptograf(D, Q):
    output = 1
    for i in Q:
        temp = 0
        if len(i) == 0:
            temp = len(D)
        else:
            # O(n * m)
            for j in D:
                if len(i) <= len(j):
                    # O(m)
                    if i == j[len(j) - len(i):]:
                        temp += 1
        output *= temp
    return log10(output)
# O(qnm)
runtests(kryptograf, all_tests = 1)