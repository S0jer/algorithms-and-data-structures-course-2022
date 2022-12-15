import bisect
from math import log10
from egzP2btesty import runtests    

# O(nm)
def radixSort(tab, x):
    if x == -1:
        return tab
  
    it = x
    output_0 = []
    output_1 = []

    for i in tab:
        if len(i) <= it:
            output_0 = [i] + output_0
        elif i[it] == "0":
            output_0.append(i)
        else:
            output_1.append(i)

    return radixSort(output_0 + output_1, x - 1) 


def kryptograf(D, Q):
    maxi = 0
    for i in range(len(D)):
        D[i] = D[i][::-1]
        maxi = max(maxi, len(D[i]))
    for i in range(len(Q)):
        Q[i] = Q[i][::-1]
    
    D = radixSort(D, maxi)

    output = 0
    for i in Q:
        lo = bisect.bisect_left(D, i)
        hi = bisect.bisect_right(D, i + "2")
        output += log10(hi - lo)
    return output

# Zmień all_test
runtests(kryptograf, all_tests = 3)