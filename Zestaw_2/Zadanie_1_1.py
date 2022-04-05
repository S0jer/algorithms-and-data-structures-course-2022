# Zadanie 1. Proszę zaimplementować:
# 1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
# 2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
# 3. Co się stanie, jeśli w powyższym algorytmie będziemy łączyć poprzednio posortowaną listę z kolejną,
# zamiast łączenia dwóch kolejnych list?


class Node:
    def __init__(self):
        self.next = None
        self.val = None


def mergeSortedLL(head1, head2):
    p = Node()
    first = p

    while head1 is not None and head2 is not None:
        if head1.val > head2.val:
            tmp = head2
            head2 = head2.next
            first.next = tmp
            tmp.next = None
            first = first.next
        else:
            tmp = head1
            head1 = head1.next
            first.next = tmp
            tmp.next = None
            first = first.next

    if head1.next is None:
        first.next = head2
    else:
        first.next = head1

    return p.next


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.val, "->", end=" ")
        L = L.next
    print("|")


head_1 = tab2list([8, 9, 31, 37, 40])  # , 13, 45, 60, 88, 92])
head_2 = tab2list([1, 9])  # , 6, 47, 50, 71, 90, 91, 93])

head = mergeSortedLL(head_1, head_2)

printlist(head)
