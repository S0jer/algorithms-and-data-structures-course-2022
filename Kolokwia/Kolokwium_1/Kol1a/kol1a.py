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
        if T[i][len(T[i]) - 1] < T[i][0]:
            T[i] = T[i][::-1]
        buckets[len(T[i])].append(T[i])

    result = -1
    for bucket in buckets:
        m = len(bucket)
        if m > 0:
            qsort(bucket)
            x = 1
            for i in range(m - 1):
                if bucket[i] == bucket[i + 1] or bucket[i] == bucket[i + 1][-1]:
                    x += 1
                else:
                    x = 1
                if x > result:
                    result = x

            if x > result:
                result = x
    return result


def qsort(T):
    n = len(T)
    mm = 65

    for j in range(len(T[0]) // 2, -1, -1):

        values = [[] for _ in range(59)]
        for i in range(n):
            values[ord(T[i][j]) - mm].append(T[i])
        idx = 0
        for k in range(59):
            for el in values[k]:
                T[idx] = el
                idx += 1


runtests(g, all_tests=True)
