# Dana jest klasa :
# class Node:
# 	val = 0
# 	next = None
# reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val poszczególnych węzłów zostały
# wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b]. Napisz procedurę sort(first), która sortuje
# taką listę. Funkcja powinna być jak najszybsza.


# Bucket na linked list :)
from math import inf


class Node:
    def __init__(self):
        self.val = 0
        self.next = None


def sortNode(head, a, b):
    n = (b - a) // 2
    diff = (b - a) / 2

    bucketsRange = [a for _ in range(n + 1)]
    buckets = [Node() for _ in range(n + 1)]

    for i in range(1, n + 1):
        bucketsRange[i] = bucketsRange[i - 1] + diff
    curr = head

    while curr.next is not None:
        next = curr.next
        for i in range(1, n + 1):
            if bucketsRange[i - 1] <= curr.val <= bucketsRange[i]:
                tmp = buckets[i]
                while tmp.next is not None:
                    tmp = tmp.next
                curr.next = None
                tmp.next = curr
                break
        curr = next

    for i in range(1, n + 1):
        if bucketsRange[i - 1] <= curr.val <= bucketsRange[i]:
            tmp = buckets[i]
            while tmp.next is not None:
                tmp = tmp.next
            curr.next = None
            tmp.next = curr
            break
    result = Node()
    head = result
    for bucket in buckets:
        bucket = insertionSort(bucket)

        while result.next is not None:
            result = result.next
        result.next = bucket.next

    return head.next


def insertionSort(head):
    if head is None or head.next is None:
        return head

    curr = head.next
    prev = head
    sortedList = Node()
    result = sortedList

    while head.next is not None:
        minValue = inf

        while curr is not None:
            if curr.val < minValue:
                minValue = curr.val
                minCurr = curr
                minPrev = prev
            curr = curr.next
            prev = prev.next

        minPrev.next = minCurr.next
        minCurr.next = None
        sortedList.next = minCurr
        sortedList = sortedList.next
        curr = head.next
        prev = head

    return result


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


A = [0, 1, 3, 2, 5, 5, 1.22, 3.44, 4.51, 4.12]
A = tab2list(A)
printlist(A)
A = sortNode(A, 0, 5)
printlist(A)
