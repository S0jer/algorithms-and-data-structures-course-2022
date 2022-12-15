from queue import PriorityQueue

from egzP8btesty import runtests


def robot(G, P):
    n, m = len(G), len(P)
    controlPoints = {}
    Q = PriorityQueue()

    for j in range(m):
        controlPoints[P[j]] = j

    for i in range(n):
        T = [0] * m
        if controlPoints.get(i) is not None:
            T[controlPoints.get(i)] = 1
            Q.put((0, i, T, -1))
        else:
            Q.put((0, i, T, -1))

    while not Q.empty():
        cost, v, cp, last = Q.get()
        if sum(cp) == m:
            return cost

        for move in G[v]:
            T = cp[:]
            if controlPoints.get(move[0]) and T[controlPoints.get(move[0])] != 1 and last != move[0]:
                T[controlPoints.get(move[0])] = 1
                Q.put((cost + move[1], move[0], T, v))
            elif controlPoints.get(move[0]) is None and last != move[0]:
                Q.put((cost + move[1], move[0], T, v))

    return -1


runtests(robot, all_tests=False)
