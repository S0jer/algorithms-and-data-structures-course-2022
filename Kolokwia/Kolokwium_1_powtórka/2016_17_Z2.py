# . Proszę zaimplementować funkcję:
# int SumBetween(int T[], int from, int to, int n);
# Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
# tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
# liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
# Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
# czasową (oraz bardzo krótko uzasadnić to oszacowanie).


def sumBetween(T, fom, to):
    n = len(T)

    result = 0
    for i in range(fom, to + 1):
        result += select(T, 0, i, n - 1)

    print(T)

    return result


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def select(A, p, k, r):
    if p == r: return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, q + 1, k, r)
        else:
            return select(A, p, k, q - 1)


T = [10, 7, 2, 1, 4, 5, 11, 9, 14, 2, 4]

result = sumBetween(T, 3, 7)
print(result)

T.sort()
print(T)
