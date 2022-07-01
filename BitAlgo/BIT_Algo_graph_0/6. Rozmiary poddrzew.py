# Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń.
# Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.vertexes = 0


def countVertex(head):
    if head.left is not None:
        countVertex(head.left)
    if head.right is not None:
        countVertex(head.right)

    if head.parent is not None:
        head.parent.vertexes += head.vertexes + 1

    return head.vertexes


head = Node(10)
a = Node(7)
b = Node(8)
c = Node(9)
d = Node(5)
e = Node(4)

head.left = a
head.right = b
a.parent = head
b.parent = head

a.left = c
c.parent = a

a.right = d
d.parent = a

d.left = e
e.parent = d

print(countVertex(head))
