from zad2testy import runtests
from math import ceil, inf


def highway(A):
    n = len(A)
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                G[i][j] = hLen(A, i, j)
                G[j][i] = G[i][j]

    for i in G:
        print(i)
    dp = kruskal(G)

    l_min = inf
    l_max = 0
    for a in range(len(dp)):
        l_c = hLen(A, dp[a][0], dp[a][1])
        print(l_c)
        if l_c > l_max:
            l_max = l_c
        if l_min > l_c:
            l_min = l_c

    print(l_min, l_max)

    return l_max - l_min


def kruskal(G):
    n = len(G)
    E = []
    A = []

    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                E.append(((i, j), G[i][j]))
                G[i][j] = -1
                G[j][i] = -1

    E.sort(key=lambda E: E[1])

    m = len(E)
    v_p = [i for i in range(m)]
    rank = [0] * m

    for i in range(m):
        if find(E[i][0][0], v_p) != find(E[i][0][1], v_p):
            union(E[i][0][0], E[i][0][1], v_p, rank)
            A.append(E[i][0])

    return A


def union(x, y, v_p, rank):
    x = find(x, v_p)
    y = find(y, v_p)

    if x == y: return 1
    if rank[x] > rank[y]:
        v_p[y] = x
    else:
        v_p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find(x, v_p):
    if x != v_p[x]:
        v_p[x] = find(v_p[x], v_p)
    return v_p[x]


def hLen(A, a, b):
    length = ceil(((A[a][0] - A[b][0]) ** 2 + (A[a][1] - A[b][1]) ** 2) ** (1 / 2))

    return length
        

runtests( highway ) 
