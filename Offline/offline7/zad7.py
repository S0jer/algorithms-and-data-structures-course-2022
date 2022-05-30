from zad7testy import runtests


# Paweł Jaśkowiec 406165

# Pomysł polega na utworzeniu grafu gdzie jeden wierzchołek dzielimy na 3 z których 2 symbolizują bramy a jeden miasto
# oraz zastosowania algorytmu DFS w taki sposób aby realizował sortowanie topologiczne oraz sprawdzeniu czy otrzymany
# ciąg wierzchołków spełnia założenia zadania

# Algorytm nie dokończony bo coś nie działa


def droga(G):
    n = len(G)
    result = None
    indexes = [-1 for _ in range(3 * n)]
    graph = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    gates = [(n + i, n + i + 1) for i in range(0, 2 * n, 2)]
    vertId = n

    for i in range(n):
        for gate in G[i]:
            graph[i][vertId] = 1
            indexes[i] = i
            indexes[vertId] = i
            for exit in gate:
                graph[vertId][exit] = 1
                if i in G[exit][0]:
                    graph[gates[exit][0]][vertId] = 1
                elif i in G[exit][1]:
                    graph[gates[exit][1]][vertId] = 1
                graph[i][exit] = 0
                graph[exit][i] = 0
            vertId += 1

    for i in range(n):
        sortedTp = DFSTp(graph, [-1 for _ in range(3 * n)], indexes, i, [-1])
        sortedTp.pop(0)
        sortedTp.append(sortedTp[0])

        if len(sortedTp) == n + 1 and canTraverse(G, sortedTp):
            sortedTp.pop(-1)
            result = sortedTp

    return result


def canTraverse(G, road):
    n = len(G)
    idx = 0
    gates = [[-1 for _ in range(2)] for _ in range(n)]

    while idx < len(road) - 1:
        canGo = False
        for i in range(2):
            if road[idx + 1] in G[road[idx]][i] and gates[road[idx]][i] == -1:
                for j in range(2):
                    if road[idx] in G[road[idx + 1]][j] and gates[road[idx + 1]][j] == -1 and canGo is False:
                        gates[road[idx]][i] = 1
                        gates[road[idx + 1]][j] = 1
                        canGo = True
        if canGo is False:
            return False
        idx += 1

    return True


def DFSTp(G, visited, indexes, u, sortedTp):
    n = len(G)
    visited[u] = 1
    for i in range(n):
        if G[u][i] == 1 and visited[i] == -1:
            DFSTp(G, visited, indexes, i, sortedTp)

    if u < n // 3:
        sortedTp.append(indexes[u])

    return sortedTp


# zmien all_tests na True zeby uruchomic wszystkie testy

runtests(droga, all_tests=True)
