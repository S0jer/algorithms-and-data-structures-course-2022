from egzP7atesty import runtests
from edmondsKarp import edmonds_karp
from fordFulkerson import FordFulkerson


def akademik(T):
    n = len(T)
    rooms, withNone = 0, 0

    for p in T:
        check = 0
        for tmp in p:
            if tmp is not None and tmp > rooms:
                rooms = tmp
            if tmp is None:
                check += 1
        if check == 3:
            withNone += 1

    lastRoom = rooms + 1
    rooms += 3 + n
    G = [[0 for _ in range(rooms)] for _ in range(rooms)]

    for i in range(n):
        for p in T[i]:
            if p is not None:
                G[lastRoom][p] = 1
                G[p][rooms - 1] = 1
                G[rooms - 2][lastRoom] = 1
        lastRoom += 1

    result = FordFulkerson(G, rooms - 2, rooms - 1)
    # result = edmonds_karp(G, rooms - 2, rooms - 1)

    return n - withNone - result


runtests(akademik)
