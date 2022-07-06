from zad2testy import runtests
from math import inf


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.TreeW = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)

    def TreeWeight(self):
        for i in range(len(self.edges)):
            self.edges[i].TreeW += self.weights[i]
            self.TreeW += self.edges[i].TreeW


def list2tree(L):
    X = Node()
    for CH in L:
        Y = list2tree(CH[2])
        X.addEdge(Y, CH[1], CH[0])

    return X


def balance(T):
    CountTree(T)
    # TreeW_Print(T)
    result = findIdx(T.TreeW, T, 0, inf)

    return result[0]


def findIdx(Base, A, min_id, min_R):
    for i in range(len(A.edges)):
        if Base == A.TreeW:
            diff = abs(A.edges[i].TreeW - abs(A.TreeW - A.edges[i].TreeW + A.weights[i]))
        else:
            diff = abs(Base - A.edges[i].TreeW)

        if diff < min_R:
            min_id = A.ids[i]
            min_R = diff

    for j in range(len(A.edges)):
        min_id, min_R = findIdx(Base, A.edges[j], min_id, min_R)

    return min_id, min_R


def TreeW_Print(A):
    print(A.TreeW)
    for j in A.weights:
        print(j)
    print("-----------")
    for i in A.edges:
        TreeW_Print(i)


def CountTree(A):
    for i in A.edges:
        CountTree(i)
    A.TreeWeight()


runtests(balance)
