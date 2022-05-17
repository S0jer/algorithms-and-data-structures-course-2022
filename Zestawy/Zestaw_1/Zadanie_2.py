# Zadanie 2. (sortowanie listy jednokierunkowej) Proszę zaimplementować algorytm sortowania listy
# jednokierunkowej. W szczególności należy:
# 1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
# 2. Zaimplementować wstawianie do posortowanej listy.
# 3. Zaimplementować usuwanie maksimum z listy.
# 4. Zaimplementować sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyższych funkcji

from math import inf


class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val


def insertIntoList(head, value):
    newNode = Node(value)

    first = head
    if first is None:
        return Node(value)

    if first.val >= newNode.val:
        newNode.next = first
        return newNode

    while first is not None:
        if first.next is None and newNode.val >= first.val:
            first.next = newNode
            return head

        elif first.val <= newNode.val and newNode.val < first.next.val:
            tmp = first.next
            first.next = newNode
            newNode.next = tmp
            return head

        first = first.next


def printNodes(head):
    first = head
    while first is not None:
        print(first.val, end=' ')
        first = first.next
    print()


def addToList(head, value):
    first = head
    newNode = Node(value)

    while first.next is not None:
        first = first.next

    first.next = newNode

    return head


def deleteMaximum(head):
    first = Node(None)
    first.next = head
    curr = Node(-inf)

    if first.next.next is None:
        return Node(None), first.next.val

    while first.next is not None:
        if first.next.val >= curr.val:
            prev = first
            curr = first.next

        first = first.next

    prev.next = curr.next

    return head


def insertionSortLinkedList(head):
    newHead = Node(head.val)
    head = head.next

    while head is not None:
        newHead = insertIntoList(newHead, head.val)
        head = head.next

    return newHead


def selectionSortLinkedList(head):
    newHead = Node(head.val)
    head = head.next

    while head.next is not None:
        head, maxVal = findMaximum(head)
        newHead = insertIntoList(newHead, maxVal)

    newHead = insertIntoList(newHead, head.val)

    return newHead
def findMaximum(head):
    first = Node(None)
    first.next = head
    curr = Node(-inf)

    if head is not None and head.next is None:
        return Node(None), head.val

    while first.next is not None:
        if first.next.val >= curr.val:
            prev = first
            curr = first.next
            tmp = curr.val

        first = first.next

    prev.next = curr.next

    return head, tmp


head = Node(10)
head = insertIntoList(head, 8)
head = insertIntoList(head, 13)
head = insertIntoList(head, 11)
head = insertIntoList(head, 15)
head = insertIntoList(head, 17)
head = insertIntoList(head, 13)
head = addToList(head, 15)
head = addToList(head, 16)

printNodes(head)

newHead = selectionSortLinkedList(head)

printNodes(newHead)
