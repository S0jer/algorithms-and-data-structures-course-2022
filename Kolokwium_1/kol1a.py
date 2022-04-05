from kol1atesty import runtests

# Paweł Jaśkowiec, 406165

# Pomysł polega na podzieleniu słów względem długości oraz drugiej litery słowa,
# oraz zliczeniu siły dla elementów podzielonych względem danych zależności

#

def g(T):
    n = len(T)
    maxL = 0
    for i in range(n):
        if len(T[i]) > maxL:
            maxL = len(T[i])

    buckets = [[] for _ in range(maxL + 1)]

    for i in range(n):
        buckets[len(T[i])].append(T[i])

    # for i in range(len(buckets)):
    #     if len(buckets[i]) > 1:
    #         if len(buckets[i][0]) > 2:
    #             buckets[i] = buc(buckets[i])



    result = -1
    for bucket in buckets:
        m = len(bucket)
        if m > 0:
            for i in range(m):
                x = 0
                for j in range(m):
                    if bucket[i] == bucket[j] or bucket[i] == bucket[j][::-1]:
                        x += 1
                if x > result:
                    result = x

    return result

def buc(T):
    n = len(T)
    maxL = 0
    for i in range(n):
        if ord(T[i][1]) > maxL:
            maxL = len(T[i])

    buckets = [[] for _ in range(maxL + 1)]

    for i in range(n):
        buckets[len(T[i])].append(T[i])
    r = []
    for bucket in buckets:
        r += bucket

    return r

runtests( g, all_tests=True )
