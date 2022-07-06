from zad1testy import runtests


def mr(X):
    n = len(X)
    for i in range(n):
        X[i] = (X[i], i)
    XR = X[::-1]
    FI, PI, FIR, PIR = lis(X)
    FD, PD, FDR, PDR = lis(XR)

    ID = [0 for _ in range(n)]
    DI = [0 for _ in range(n)]

    for i in range(n):
        ID[i] = FI[i] + FIR[i] - 1
        DI[i] = FD[i] + FDR[i] - 1
    print(ID, FI, FIR)
    print(DI, FD, FDR)
    # longestDec = getPath(X, pLeft, maxiLeft)
    # longestInc = getPath(XR, pRight, maxiRight)

    return [max(max(ID), max(DI))]


def getPath(G, p, idx):
    L = [G[idx]]
    while p[idx] != -1:
        L.append(G[p[idx]])
        idx = p[idx]

    return L


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    FR = [1 for _ in range(n)]
    PR = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i][0] > A[j][0] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if A[i][0] > A[j][0] and FR[j] + 1 > FR[i]:
                FR[i] = FR[j] + 1
                PR[i] = j

    return F, P, FR, PR


runtests(mr)
