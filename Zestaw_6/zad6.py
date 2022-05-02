# Zadanie 6 (ścieżka w drzewie) Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma—
# potencjalnie ujemną—wartość value(v). Proszę zaproponować algorytm, który znajduje wartość najbardziej
# wartościowej ścieżki w drzewie T.

# Raczej poglądowa implementacja

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.f = 0


def f(v):
    if v is None: return (0, 0)
    (L, ML) = f(v.left)
    (R, MR) = f(v.right)

    v.f = max(0, v.val, v.val + L, v.val + R)
    M = max(ML, MR, v.f)

    return (v.f, M)
