from kol3atesty import runtests

from math import inf
from queue import PriorityQueue


# Paweł Jaśkowiec, 406165

# Z listy E oraz listy S tworzę graf zgodnie z opisem zadania, to znaczy z listy E o elementach: (u, v, t) powstają
# mi drogi łączące u i v oraz v i u o wadze t, a następnie z list S tworzę drogi między każdym elementem o wadze 0
# ponieważ są to osobliwości między którymi poruszamy się w czasie 0

# Idąc za daną w treści podpowiedzią zmieniłem sposób tworzenia grafu na taki gdzie osobliwości stanowią jeden punkt
# i na tej reprezetnacji uruchamiam algorytm Dijkstra

# Na tak powstałym grafie stosuję algorytm Dijkstra który oblicz najkrótszą drogę między wierzchołkiem a i b,
# pod warunkiem że taka istnieje, jeśli nie to wartość drogi do b będzie równa inf a wtedy zwracamy None.


# Złożoność: O(n^2)

# def spacetravel(n, E, S, a, b):
#     graph = [[-1 for _ in range(n)] for _ in range(n)]
#     dp = [inf for _ in range(n)]
#     m = len(S)
#     dp[a] = 0
#
#     Q = PriorityQueue()
#     Q.put((0, a))
#
#     for e in E:
#         graph[e[0]][e[1]] = e[2]
#         graph[e[1]][e[0]] = e[2]
#
#     for x in range(m):
#         for y in range(x + 1, m):
#             graph[S[x]][S[y]] = 0
#             graph[S[y]][S[x]] = 0
#
#     while not Q.empty():
#         _, u = Q.get()
#         for i in range(n):
#             if graph[u][i] >= 0 and dp[i] > dp[u] + graph[u][i]:
#                 dp[i] = dp[u] + graph[u][i]
#                 Q.put((dp[i], i))
#
#     if dp[b] == inf:
#         return None
#     return dp[b]

def spacetravel(n, E, S, a, b):
    indexes = [-1 for _ in range(n)]

    for s in S:
        indexes[s] = 0
    tmp = 1
    for i in range(n):
        if indexes[i] != 0:
            indexes[i] = tmp
            tmp += 1

    graph = [[inf for _ in range(tmp)] for _ in range(tmp)]
    dp = [inf for _ in range(tmp)]

    for e in E:
        graph[indexes[e[0]]][indexes[e[1]]] = min(graph[indexes[e[0]]][indexes[e[1]]], e[2])
        graph[indexes[e[1]]][indexes[e[0]]] = min(graph[indexes[e[1]]][indexes[e[0]]], e[2])

    dp[indexes[a]] = 0
    Q = PriorityQueue()
    Q.put((0, indexes[a]))

    while not Q.empty():
        _, u = Q.get()
        for i in range(tmp):
            if graph[u][i] != inf and dp[i] > dp[u] + graph[u][i]:
                dp[i] = dp[u] + graph[u][i]
                Q.put((dp[i], i))

    if dp[indexes[b]] == inf:
        return None
    return dp[indexes[b]]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
