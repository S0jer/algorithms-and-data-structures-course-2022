from egzP2btesty import runtests
from math import log10

class node:
    def __init__(self):
        self.left   = None
        self.right  = None
        self.x      = 0
# O(m)
def add2node(root, string):
    if string == "":
        root.x += 1
        return

    root.x += 1
    if string[-1] == "1":
        if not root.left:
            root.left = node()
        add2node(root.left, string[:-1])
    else:
        if not root.right:
            root.right = node()
        add2node(root.right, string[:-1])
    return

# O(m)
def addprefix(root, string):
    if string == "":
        return root.x
    if string[-1] == "1":
        return addprefix(root.left, string[:-1])
    else:
        return addprefix(root.right, string[:-1])

def kryptograf(D, Q):    
    root = node()
    output = 0
    # O(nm)
    for i in D:
        add2node(root, i)
    # O(qm)
    for i in Q:
        output += log10(addprefix(root, i))

    return output

# Zmień all_test
runtests(kryptograf, all_tests = 3)