#
#
#

def f(T, n, S1, s):
    if n < 0:
        return abs(S1 - s)

    inc = f(T, n - 1, S1 + T[n], s - T[n])
    exc = f(T, n - 1, S1, s)

    return min(inc, exc)


def kontenerowiec(T):
    n = len(T)
    s = sum(T)

    return f(T, n - 1, 0, s)


T = [1, 6, 5, 11]

print(kontenerowiec(T))
