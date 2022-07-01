# Krasnoludy i trolle

# Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi korytarzamia,
# W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej z pozostałych jaskiń mieszka znana
# krasnoludom ilość trolli. Krasnoludy chcą zaplanować swoją obronę na wypadek ataku ze strony trolli.
# Zamierzają w tym celu zakraść się i podłożyć ładunek wybuchowy pod jednen z korytarzy, tak aby trolle
# mieszkające za tym korytarzem nie miały żadnej ścieżki którą mogłyby dotrzeć do osaby krasnoludów.

# Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej
# liczbie trolli?


# Szukamy mostów oraz zliczamy ile trolli znajduje się po drugiej stronie mostu
# Usuwamy ten który odetnie największa lizbę trolli

from math import inf


def krasnoludy(G, o, trollNumber):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [-1 for _ in range(n)]
    low = [inf for _ in range(n)]
    vertNumber = [-1 for _ in range(n)]
    newTrollsNumber = 0
    trollMax = -inf
    number = 0

    low, vertNumber, parents, number, newTrollsNumber = DFS(G, o, visited, low, vertNumber, parents, number,
                                                            trollNumber, newTrollsNumber)

    for i in range(n):
        if low[i] == vertNumber[i] and parents[i] != -1 and trollNumber[i] > trollMax:
            result = (parents[i], i)
            trollMax = trollNumber[i]

    return result, trollMax


def DFS(G, u, visited, low, vertNumber, parents, number, trollNumber, newTrollsNumber):
    visited[u], vertNumber[u], low[u] = True, number, number
    n = len(G)

    for i in range(n):
        if visited[i] is True and G[u][i] and i != parents[u]:
            low[u] = min(vertNumber[u], vertNumber[i])

        if visited[i] is False and G[u][i]:
            number += 1
            parents[i] = u
            low, vertNumber, parents, number, newTrollsNumber = DFS(G, i, visited, low, vertNumber, parents, number,
                                                                    trollNumber, 0)
            trollNumber[u] = newTrollsNumber + trollNumber[u]

    for i in range(n):
        if visited[i] is True and G[u][i] == 1 and i != parents[u]:
            low[u] = min(low[u], low[i])

    return low, vertNumber, parents, number, trollNumber[u]


G = [[0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0]]

trollNumber = [2, 0, 13, 7, 5, 3, 5, 2, 2]

print(krasnoludy(G, 1, trollNumber))
