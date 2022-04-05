# zad3test_spec.py

ALLOWED_TIME = 1


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# N, k
  (100, 20),
  (1000, 100),
  (10000, 10000),
  (100000, 10000),
  (100000, 100000),
  (200000, 1000),
  (200000, 10000),
  (400000, 100),
  (550000, 1000),
  (550000, 10000),
]


def gentest(N, k):
    from testy import MY_random

    C = []
    span = [0]*k
    for i in range(k):
        c = MY_random() % 10 + 1
        C += ([i]*c)
        span[i]=c

    clen = len(C)
    P = [None]*k
    for i in range(k):
        while True:
            a = MY_random() % N + 1
            b = MY_random() % N + 1
            if a > b:
                tmp = a
                a = b
                b = tmp
            if a < b: break

        c = span[i] / clen
        P[i] = (a, b, c)

    T = [None]*N
    for i in range(N):
        u = MY_random() % clen
        u = C[u]

        a, b, _ = P[u]
        x = MY_random() / (2**32)
        T[i] = a + (b-a)*x

    return [T, P], sorted(T)

