from zad1testy import runtests


def tanagram(x, y, t):
    n = len(x)
    mm = 65
    if n != len(y):
        return False
    X = [[] for _ in range(59)]
    Y = [[] for _ in range(59)]

    for i in range(n):
        xo, yo = ord(x[i]), ord(y[i])
        X[xo - mm].append(i)
        Y[yo - mm].append(i)

    for j in range(59):
        if len(X[j]) != len(Y[j]):
            return False
        for k in range(len(X[j])):
            if abs(X[j][k] - Y[j][k]) > t:
                return False

    return True


runtests(tanagram)
