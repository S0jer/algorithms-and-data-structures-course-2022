# Dana jest struktura Node opisująca listę jednokierunkową:
# struct Node { Node * next; int value; };
# Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
# wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
# powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
# wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
# wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
# najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
# wejściowej.


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def fixSortedList(curr):
    head = Node()
    head.next = curr
    curr = head
    prev = head
    curr = curr.next
    repaired = False

    while curr.next is not None:
        if curr.value > curr.next.value:
            prev.next = curr.next
            tmp = curr
            tmp.next = None
            curr = prev.next
            break

        curr = curr.next
        prev = prev.next

    while curr.next is not None:
        if prev.value is not None and prev.value <= tmp.value and tmp.value <= curr.value:
            prev.next = tmp
            tmp.next = curr
            repaired = True
            break

        curr = curr.next
        prev = prev.next

    if not repaired:
        curr.next = tmp

    return head.next


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


head = tab2list([8, 3, 4, 4, 5, 6, 7])
printlist(head)
head = fixSortedList(head)
printlist(head)
