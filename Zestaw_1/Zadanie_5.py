# Zadanie 5. (odwracanie listy) Proszę zaimplementować funkcję odwracającą listę jednokierunkową.


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


def reverseLinkedList(head):
    prev = head
    curr = head.next

    prev.next = None

    while curr.next is not None:
        currNext = curr.next
        curr.next = prev
        prev = curr
        curr = currNext

    curr.next = prev
    return curr


head = Node(10)
head = insertIntoList(head, 8)
head = insertIntoList(head, 13)
head = insertIntoList(head, 11)
head = insertIntoList(head, 15)
head = insertIntoList(head, 17)
head = insertIntoList(head, 13)

printNodes(head)

newHead = reverseLinkedList(head)

printNodes(newHead)
