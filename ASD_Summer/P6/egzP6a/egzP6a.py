from egzP6atesty import runtests


def google(H, s):
    n = len(H)

    maxlength = 0
    for i in H:
        if len(i) > maxlength:
            maxlength = len(i)
    maxlength += 1

    lengthsCounter = [0 for _ in range(maxlength)]

    for j in H:
        lengthsCounter[len(j)] += 1

    expectedLength = -1
    for k in range(maxlength - 1, -1, -1):
        if lengthsCounter[k] >= s:
            expectedLength = k
            break
        else:
            s -= lengthsCounter[k]

    G = []
    for l in H:
        if len(l) == expectedLength:
            letters = 0
            for w in l:
                if 0 <= ord(w) - 97 <= 26:
                    letters += 1

            G.append((l, letters))

    quicksort(G, 0, len(G) - 1)

    return G[s - 1][0]


def partition(A, p, r):
    x = A[r][1]
    i = p - 1

    for j in range(p, r):
        if A[j][1] > x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


runtests(google, all_tests=True)
