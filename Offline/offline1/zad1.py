from zad1testy import Node, runtests


# Paweł Jaśkowiec, 406165

# Algorytm bierze wycinek listy długości 2*k oraz sortuje go za pomocą sortowania quicksort
# następnie przesuwa się o k elementów do przodu ponieważ z faktu iż lista jest k-chaotyczna, k elementów
# znajdzie się na swojej pozycji.

# Złożoność: Quicksort - 2k*log(2k) dla n//k odcinków --> (n//k)*2k*log(2k)

# Dla:
# k = 0(1) -> n*2log(2)
# k = O(log(n)) -> (n//log(n))*2*log(n)*log(2*log(n))
# k = O(n) -> n*log(n)

def SortH(p, k):
    start, prev, end = p, Node(), p
    prev.val = None
    prev.next = start
    p = prev

    # Wyznaczam odcinek długości 2*k
    cnt = 0
    while cnt < 2 * k + 1 and end.next is not None:
        end = end.next
        cnt += 1

    while start.next is not None:

        if end.next is not None:
            endNext = end.next
            end.next = None
            start = qsort(start)
        else:
            start = qsort(start)
            prev.next = start
            break

        prev.next = start
        end = start
        while end.next is not None:
            end = end.next
        end.next = endNext

        # Przesuwam listę o k elementów do przodu ponieważ są one już na swoim miejscu,
        cnt = 0
        while cnt < k + 1 and start.next is not None and end.next is not None:
            prev = prev.next
            start = start.next
            end = end.next
            cnt += 1

    return p.next


def partition(L, end):
    pivot = L  # pivot to pierwszy element, nie ma sensu przechodzic calej listy i brac ostatniego
    head = L  # przechowuje wskaznik na 1 element
    while L.next != end:
        if L.next.val < pivot.val:
            tmp = L.next
            L.next = L.next.next
            tmp.next = head
            head = tmp
        else:
            L = L.next
    return (head, pivot)


def quicksort(L, end):
    if L != end:
        L, p = partition(L, end)
        L = quicksort(L, p)
        p.next = quicksort(p.next, end)
    return L


def qsort(L):
    return quicksort(L, None)


runtests(SortH)
