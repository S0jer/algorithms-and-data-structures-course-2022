from zad1testy import runtests
from queue import PriorityQueue, Queue


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.right = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa jesli istnieje
        self.value = None  # przechowywana wartosc


def ConvertTree(p):
    Q = PriorityQueue()
    Q2 = Queue()

    Q2.put(p)

    while not Q2.empty():
        u = Q2.get()

        u.parent = None
        if u.left is not None:
            Q2.put(u.left)
            u.left = None
        if u.right is not None:
            Q2.put(u.right)
            u.right = None

        Q.put((u.value, u))

    _, r = Q.get()
    Q2.put(r)

    while not Q.empty():
        u = Q2.get()
        u1 = None
        u2 = None
        if len(Q.queue) >= 1:
            _, u1 = Q.get()
        if len(Q.queue) >= 1:
            _, u2 = Q.get()

        if u1 is not None:
            u.left = u1
            u1.parent = u
            Q2.put(u1)
        if u2 is not None:
            u.right = u2
            u2.parent = u
            Q2.put(u2)

    return r


runtests(ConvertTree)
