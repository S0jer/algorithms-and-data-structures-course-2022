# Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
# struct Node{ Node* next; double value; }
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
# liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
# przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
# jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
# zaimplementowanej funkcji.


MY_seed = 42
MY_a = 134775813
MY_c = 1
MY_modulus = 2 ** 32


def MY_random():
    global MY_seed, MY_a, MY_c, MY_modulus
    MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
    return MY_seed


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def bucketSortNode(head):
    start = head.next
    n, minV, maxV = 0, 0, 0

    while start is not None:
        if start.value > maxV:
            maxV = start.value
        if start.value < minV:
            minV = start.value

        n += 1
        start = start.next
    maxV += 1
    minV -= 1
    rangee = (maxV - minV) / n

    buckets = [[Node(), None] for _ in range(n)]

    start = head.next
    while start is not None:
        startNext = start.next

        idx = int((start.value - minV) / rangee)
        if buckets[idx][1] is None:
            buckets[idx][0].next = start
            start.next = None
            buckets[idx][1] = buckets[idx][0].next
        else:
            buckets[idx][1].next = start
            start.next = None
            buckets[idx][1] = buckets[idx][1].next

        start = startNext

    result = Node()
    head = result
    for i in range(len(buckets)):
        if buckets[i][1] is not None:
            buckets[i][0] = insertionSort(buckets[i][0].next)
            result.next = buckets[i][0]

            while result.next is not None:
                result = result.next

    return head


def insertionSort(f):
    if f == None:
        return None
    sortedlist = f
    f = f.next
    sortedlist.next = None
    while f != None:
        curr = f
        f = f.next
        if curr.value < sortedlist.value:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.value > search.next.value:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist


def makeList(T):
    n = len(T)
    head = Node()
    start = head

    for i in range(n):
        tmp = Node()
        tmp.value = T[i]

        start.next = tmp
        start = start.next

    return head


def gentest(N, k):
    C = []
    span = [0] * k
    for i in range(k):
        c = MY_random() % 10 + 1
        C += ([i] * c)
        span[i] = c

    clen = len(C)
    P = [None] * k
    for i in range(k):
        while True:
            a = MY_random() % N + 1
            b = MY_random() % N + 1
            if a > b:
                tmp = a
                a = b
                b = tmp
            if a < b: break

        c = span[i] / clen
        P[i] = (a, b, c)

    T = [None] * N
    for i in range(N):
        u = MY_random() % clen
        u = C[u]

        a, b, _ = P[u]
        x = MY_random() / (2 ** 32)
        T[i] = a + (b - a) * x

    return T, sorted(T)


def printLinkedList(head):
    while head is not None:
        print(head.value, end='->')
        head = head.next
    print()


T, sortedT = gentest(100, 20)

head = makeList(T)

head = bucketSortNode(head)

printLinkedList(head)
