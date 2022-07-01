# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka,
# która w liczbie występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B,
# jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo
# to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455,
# liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
#
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T), która sortuje
# elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm powinien  być  możliwie  jak  najszybszy.
# Proszę  w  rozwiązaniu  umieścić  1-2  zdaniowy  opis algorytmu oraz proszę oszacować jego złożoność czasową.


# sortujemy najpierw malejąco po liczbie cyfr wielokrotnych, potem stabilnie rosnąco po liczbie cyfr jednokrotnych. O(n)


def prettySort(T):
    n = len(T)

    for i in range(n):
        toCountNumbers = [0 for _ in range(10)]
        T[i] = [T[i], 0, 0]
        tmp = T[i][0]
        S = str(tmp)
        for s in S:
            toCountNumbers[int(s)] += 1

        for j in range(10):
            if toCountNumbers[j] == 1:
                T[i][1] += 1
            elif toCountNumbers[j] > 1:
                T[i][2] += 1

    quickSort(T, 0, n - 1, 2)
    quickSort(T, 0, n - 1, 1)

    for i in range(n):
        T[i] = T[i][0]

    return T


def quickSort(A, p, r, idx):
    while p < r:
        q = partition(A, p, r, idx)
        quickSort(A, p, q - 1, idx)
        p = q + 1


def partition(A, p, r, idx):
    x = A[r][idx]
    i = p - 1

    for j in range(p, r):
        if A[j][idx] > x and idx == 1:
            i += 1
            A[j], A[i] = A[i], A[j]
        if A[j][idx] < x and idx == 2:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


T = [123, 455, 1266, 114577, 2344, 67333]

print(prettySort(T))
