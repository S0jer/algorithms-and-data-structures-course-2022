from zad2testy import runtests


# Paweł Jaśkowiec, 406165


# Do listy L dodajemy indeksy na jakich znajdują się pierwotnie przedziały, następnie algorytm
# sortuje listę L ze względu na początki przedziałów oraz listę L jako sortedByEnd
# ze względu na końce przedziałów za pomocą sortowania Quicksort,
# z indeksów posortowanych list odczytujemy liczbę przedziałów które zaczynają/kończą się
# na pozycji początku/końca i-tego przedziału bądź wcześniej i zapisujemy w tablicy result
# Wynikiem jest max z tablicy result.

# Złożoność: O(n*logn)


def depth(L):
    n = len(L)

    for i in range(n):
        L[i].append(i)

    # sortowanie po początkach i końcach przedziałów
    sortedByEnd = quicksortEnd(L[::], 0, n - 1)
    L = quicksortStart(L, 0, n - 1)
    result = [0 for _ in range(n)]

    # cntStart dla elementów o tych samych początkach przedziałów
    cntStart = 0
    for j in range(n):
        if j >= 1 and L[j - 1][0] == L[j][0]:
            cntStart += 1
        else:
            cntStart = 0

        result[L[j][2]] += n - j + cntStart
        result[sortedByEnd[j][2]] -= n - j

    return max(result)


def partitionStart(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j][0] == A[r][0]:
            if A[j][1] >= A[r][1]:
                i += 1
                A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksortStart(T, p, l):
    while p < l:
        q = partitionStart(T, p, l)
        if q - p < l - q:
            quicksortStart(T, p, q - 1)
            p = q + 1
        else:
            quicksortStart(T, q + 1, l)
            l = q - 1
    return T


def partitionEnd(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j][1] == A[r][1]:
            if A[j][0] >= A[r][0]:
                i += 1
                A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksortEnd(T, p, l):
    while p < l:
        q = partitionEnd(T, p, l)
        if q - p < l - q:
            quicksortEnd(T, p, q - 1)
            p = q + 1
        else:
            quicksortEnd(T, q + 1, l)
            l = q - 1
    return T


runtests(depth)
