import time
from math import inf

TEST_SPEC = [
    # m (liczba rzędów), k (ilość osób w najniższym rzędzie), maxdiff
    (3, 4, 10),
    (6, 15, 20),
    (8, 75, 10),
    (8, 500, 7),
    (9, 750, 6),
    (10, 850, 5),
    (10, 1000, 4),
    (11, 1250, 3),
    (11, 1500, 3),
    (14, 2750, 2),
]

MY_seed = 42
MY_a = 134775813
MY_c = 1
MY_modulus = 2 ** 32


def MY_random():
    global MY_seed, MY_a, MY_c, MY_modulus
    MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
    return MY_seed


def limit(L, lim=160):
    x = str(L)
    if len(x) < lim:
        return x
    else:
        return x[:lim] + " [za dlugie] ..."


def runtests(f, all_tests=False):
    global TEST_SPEC

    total = 0
    zaliczone = 0
    kod = ""
    testy = 0
    i = 0
    for el in TEST_SPEC:
        m = el[0]
        k = el[1]
        n = int(m * (((m - 1) / 2) + k))

        TMP1 = [0 for _ in range(n)]
        TMP2 = [0 for _ in range(n)]
        itAlb = 1 + int(MY_random() % el[2])
        itWzr = 1 + int(MY_random() % el[2])

        for j in range(n):
            TMP1[j] = itAlb
            TMP2[j] = itWzr
            itAlb += int(MY_random() % el[2]) + 1
            itWzr += int(MY_random() % el[2]) + 1

        for j in range(1, n):
            rand1 = int(MY_random() % j)
            rand2 = int(MY_random() % j)
            TMP1[j], TMP1[rand1] = TMP1[rand1], TMP1[j]
            TMP2[j], TMP2[rand2] = TMP2[rand2], TMP2[j]

        T = [(TMP1[i], TMP2[i]) for i in range(n)]
        Tstart = [x[:] for x in T]

        MM = [0 for _ in range(m)]
        MM2 = [0 for _ in range(m)]
        MAXM = [0 for _ in range(m)]

        count = k + m - 1
        ind = 0
        for j in range(m):
            MM[j] = ind
            MM2[j] = ind
            ind += count
            count -= 1

        for j in range(m - 1):
            MAXM[j] = MM[j + 1] - 1
        MAXM[len(MAXM) - 1] = n - 1

        T2 = [0 for _ in range(n)]

        ind = 0
        level = 0
        while ind < n:
            if MM[level] <= MAXM[level]:
                T2[MM[level]] = ind
                MM[level] += 1
                ind += 1
            level += 1
            if level >= m:
                level = 0

        start = time.time()
        sol = f(T, m, k)
        end = time.time()
        total += (end - start)
        testy += 1

        minLast = inf
        maxLast = inf

        flag = True
        msg = ""

        for j in range(len(MAXM)):
            minnLevel = inf
            maxxLevel = 0
            for kk in range(MM2[j], MAXM[j] + 1):
                maxxLevel = max(maxxLevel, T[T2[kk]][1])
                minnLevel = min(minnLevel, T[T2[kk]][1])
            if maxxLevel > minLast and flag == True:
                flag = False
            minLast = minnLevel
            maxLast = maxxLevel

        timedout = 0
        wrong = 0

        if flag == False:
            print("------------")
            print("Test #", i)
            print("Dane wejściowe: ", limit(Tstart))
            print("Wynik algorytmu: ", limit(T))
            print("Test NIEZALICZONY!")
            print("Czas trwania: %.2f sek." % float(end - start))
            kod += "W "
            wrong += 1
        elif end - start > 1:
            print("------------")
            print("Test #", i)
            print("Dane wejściowe: ", limit(Tstart))
            print("Wynik algorytmu: ", limit(T))
            print("Test NIEZALICZONY")
            print("(!!!) Przekroczono dozwolony czas")
            print("Czas trwania: %.2f sek." % float(end - start))
            kod += "T "
            timedout += 1
        else:
            print("------------")
            print("Test #", i)
            print("Dane wejściowe: ", limit(Tstart))
            print("Wynik algorytmu: ", limit(T))
            print("Test zaliczony!")
            print("Czas trwania: %.2f sek." % float(end - start))
            kod += "A "
            zaliczone += 1

        i += 1
    print("------------")
    print("Liczba zaliczonych testów: ", zaliczone, "/", testy, sep="")
    print("Liczba testów z przekroczonym czasem: ", timedout, "/", testy, sep="")
    print("Liczba testów z błędnym wynikiem ", wrong, "/", testy, sep="")
    print("Orientacyjny łączny czas: %.2f sek." % float(total))
    print("Status testów:", kod)
