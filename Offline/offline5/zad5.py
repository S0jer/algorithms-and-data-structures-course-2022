from zad5testy import runtests
from queue import PriorityQueue
from math import inf
from queue import Queue


# Paweł Jaśkowiec, 406165

# Pomysł polega na przechodzeniu po pierwszym wierszu i sprawdzaniu wielkości plamy kiedy mozna zatankować
# (w trakcie rrealizacji :()

def plan(T):
    n = len(T)

    result = []
    Q = PriorityQueue()
    Q.put(((-1) * T[0], 0, [0]))

    while not Q.empty():
        u = Q.get()

        for i in range(u[1] + 1, min(u[1] + (-1) * u[0] + 1, n)):

            if T[i] != 0:
                Q.put(((-1) * ((-1) * u[0] - (i - u[1]) + T[i]), i, u[2] + [i]))

            if i == n - 1:
                result.append((u[2], u[1]))

    len_min, d_max, road = inf, 0, result[0][0]

    for i in range(len(result)):
        if len(result[i][0]) < len_min:
            len_min = len(result[i][0])
            road = result[i][0]
            d_max = result[i][1]

        elif len(result[i][0]) == len_min and d_max < result[i][1]:
            d_max = result[i][1]
            road = result[i][0]

    return road


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=False)
