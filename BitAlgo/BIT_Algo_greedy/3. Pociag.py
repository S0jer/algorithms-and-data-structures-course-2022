# Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time), przy czym są one
# posortowane niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie
# bezkonfliktowo obsłużyć te pociągi, tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
# Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.

# Lekko zmodyfikowane https://www.techiedelight.com/minimum-number-of-platforms-needed-avoid-delay-arrival-train/
# Sortujemy po arrival_time, idziemy po kolei - jak poprzedni pociąg “zachodzi” na poprzednie i mamy już tyle pociągów,
# ile peronów, to zwracamy False. Jeżeli kolejny pociąg przyjeżdża, a któryś z poprzednich już odjechał, to możemy
# zmniejszyć counter przed sprawdzeniem tego warunku.
#
# Rozw.2: Skoro pociągi są już posortowane, wystarczy zdjąć pierwsze m z nich, wstawić do kopca min. po departure time
# i dla każdego kolejnego pociągu na liście patrzyć czy ma arrival time >= od najmniejszego departure time na kopcu.
# Jak tak to zdejmujemy szczyt kopca i wstawiamy ten nowy pociąg do kopca, O(n log m).

def trains(schedule, m):
    n = len(schedule)
    heap = []
    quickSort(schedule, 0, n - 1, 0)

    for i in range(m):
        heap.append(schedule[i])
    buildHeap(heap)

    for i in range(m, n):
        print(heap)
        if schedule[i][1] >= heap[0][1]:
            delete(heap, heap[0])
            insert(heap, schedule[i])
        else:
            return False

    return True


def buildHeap(A):
    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    maxId = i

    if l < n and A[l][1] < A[maxId][1]:
        maxId = l
    if r < n and A[r][1] < A[maxId][1]:
        maxId = r
    if maxId != i:
        A[i], A[maxId] = A[maxId], A[i]
        heapify(A, n, maxId)


def insert(A, num):
    A.append(num)
    n = len(A) - 1
    p = parent(n)

    while p >= 0:
        if A[n][1] < A[p][1]:
            A[n], A[p] = A[p], A[n]
            n = p
            p = parent(n)
        else:
            break


def delete(A, num):
    A.remove(num)
    for i in range(len(A)):
        heapify(A, len(A), i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def quickSort(A, p, r, idx):
    while p < r:
        q = partition(A, p, r, idx)
        quickSort(A, p, q - 1, idx)
        p = q + 1


def partition(A, p, r, idx):
    x = A[r][idx]
    i = p - 1

    for j in range(p, r):
        if A[j][idx] < x:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


A = [(2.00, 2.30), (2.10, 3.40), (3.00, 3.20), (3.20, 4.30), (3.50, 4.00), (5.00, 5.20)]
n = 3

print(trains(A, 1))
