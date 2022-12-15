from egzP5btesty import runtests


def koleje(B):
    n = len(B)
    idxMax = 0

    for i in range(n):
        idxMax = max(idxMax, B[i][0], B[i][1])
    idxMax += 1

    graph = [{_} for _ in range(idxMax)]

    for edge in B:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    result, vertexes = 0, []
    visited = [-1] * idxMax
    visited[0] = 1
    DFSTp(graph, 1, visited, vertexes)
    if len(vertexes) != idxMax - 1:
        result += 1

    for k in range(1, idxMax):
        vertexes = []
        visited = [-1] * idxMax
        visited[k] = 1
        DFSTp(graph, 0, visited, vertexes)

        if len(vertexes) != idxMax - 1:
            result += 1

    return result


def DFSTp(G, u, visited, vertexes):
    visited[u] = 1

    for s in G[u]:
        if visited[s] == -1:
            DFSTp(G, s, visited, vertexes)

    vertexes.append(u)


runtests(koleje, all_tests=True)
