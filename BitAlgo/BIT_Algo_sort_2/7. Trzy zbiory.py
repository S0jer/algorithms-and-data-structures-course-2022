# Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie, czy istnieje
# taka trójka a, b, c z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!


# Sortujemy A i B, i dla każdego elementu C, przeprowadzamy szukanie idąc dwoma wskaźnikami: jednym z początku A,
# drugim z końca B. w zależności od tego, czy suma elementów wskazywanych przez wskaźniki w A i B jest większa
# lub mniejsza niż element z C, to przesuwamy odpowiedni wskaźnik. Jak natrafimy na równą sumę, to raportujemy o sukcesie.
#
# Inne podejście polega na posortowaniu C i dla każdej pary z A i B szukamy sumy binarnie.
#
# Złożoności: dla wielkości tablic odpowiednio a, b i c:
# pierwsze podejście: O(alog(a) + blog(b) + c(a+b))
# drugie podejście: O(clog(c) + a*b*log(c)) = O(log(c) * (a*b + c))


def threeSets(A, B, C):
    a, b, c = len(A), len(B), len(C)

    quickSort(C, 0, c - 1)

    for i in range(a):
        for j in range(b):
            if binarySearch(C, 0, c - 1, A[i] + B[j]) is not None:
                return True

    return False


def binarySearch(A, i, j, x):
    if i > j:
        return None
    half = (i + j) // 2

    if A[half] == x:
        val = binarySearch(A, i, half - 1, x)
        if val is None:
            return half
        return val
    elif A[half] < x:
        return binarySearch(A, half + 1, j, x)
    else:
        return binarySearch(A, i, half - 1, x)


def quickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        p = q + 1


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1
