# Wieżowiec ma 100 pięter i n wind, nie ma natomiast schodów. Każda winda posiada listę pięter do których dojeżdża
# i prędkość w sekundach na piętro.
# Jesteśmy na piętrze i, chcemy się dostać na piętro j. Ile minimalnie sekund musimy spędzić w windach aby tam dotrzeć?


# Tworzymy graf o minimalnych czasach przejazdu z piętra i na piętro j bezpośrednio (uwzględniamy każdą możliwą windę,
# wybieramy z najlepszym czasem), na tak powstałym grafie uruchamiamy algorytm Dijkstra


from math import inf
from queue import PriorityQueue


def elevator(L, a, b):
    n = len(L)
    graph = [[inf for _ in range(n)] for _ in range(n)]

    for l in L:
        for x in range(len(l[0])):
            for y in range(x + 1, len(l[0])):
                graph[l[0][x]][l[0][y]] = min(graph[l[0][x]][l[0][y]], abs(l[0][x] - l[0][y]) * l[1])
                graph[l[0][y]][l[0][x]] = min(graph[l[0][y]][l[0][x]], abs(l[0][x] - l[0][y]) * l[1])

    dp = [inf for _ in range(n)]
    Q = PriorityQueue()
    dp[a] = 0

    Q.put((dp[a], a))

    while not Q.empty():
        _, u = Q.get()

        for i in range(n):
            if graph[u][i] != inf and dp[i] > dp[u] + graph[u][i]:
                dp[i] = dp[u] + graph[u][i]
                Q.put((dp[i], i))

    return dp[b]


L = [([1, 2, 5], 1),
     ([0, 3, 5], 2),
     ([0, 3], 2),
     ([1, 2, 4], 3),
     ([3, 5], 1),
     ([0, 1, 2, 3, 4, 5], 5)]

print(elevator(L, 0, 4))
