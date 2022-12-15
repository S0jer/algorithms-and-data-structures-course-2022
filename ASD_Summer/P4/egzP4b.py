from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def sol(root, T):
    result = 0
    for h in T:
        h1, h2 = h, h

        p = pop(h1)
        n = nast(h2)

        if p is not None and n is not None and (p.key + n.key) / 2 == h.key:
            result += h.key

    return result


def pop(T):
    if T.left is not None:
        T = T.left
        while T.right is not None:
            T = T.right
        return T
    else:
        while T.parent is not None and (T.parent.right is None or T.parent.right.key != T.key):
            T = T.parent

        return T.parent


def nast(T):
    if T.right is not None:
        T = T.right
        while T.left is not None:
            T = T.left
        return T
    else:
        while T.parent is not None and (T.parent.left is None or T.parent.left.key != T.key):
            T = T.parent

        return T.parent


runtests(sol, all_tests=True)
